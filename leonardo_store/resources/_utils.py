from import_export.resources import *


@atomic()
def import_data(self, dataset, dry_run=False, raise_errors=False,
                use_transactions=None, **kwargs):
    """
    Imports data from ``dataset``.
    ``use_transactions``
        If ``True`` import process will be processed inside transaction.
        If ``dry_run`` is set, or error occurs, transaction will be rolled
        back.

    note(majklk): this method uses only copy
    """
    result = Result()
    result.diff_headers = self.get_diff_headers()

    if use_transactions is None:
        use_transactions = self.get_use_transactions()

    if use_transactions is True:
        # when transactions are used we want to create/update/delete object
        # as transaction will be rolled back if dry_run is set
        real_dry_run = False
        sp1 = savepoint()
    else:
        real_dry_run = dry_run

    try:
        self.before_import(dataset, real_dry_run, **kwargs)
    except Exception as e:
        logging.exception(e)
        tb_info = traceback.format_exc(2)
        result.base_errors.append(Error(repr(e), tb_info))
        if raise_errors:
            if use_transactions:
                savepoint_rollback(sp1)
            raise

    instance_loader = self._meta.instance_loader_class(self, dataset)

    for row in dataset.dict:
        try:
            row_result = RowResult()
            instance, new = self.get_or_init_instance(instance_loader, row)
            if new:
                row_result.import_type = RowResult.IMPORT_TYPE_NEW
            else:
                row_result.import_type = RowResult.IMPORT_TYPE_UPDATE
            row_result.new_record = new
            from django.forms.models import model_to_dict
            import copy
            original = copy.copy(instance)
            if self.for_delete(row, instance):
                if new:
                    row_result.import_type = RowResult.IMPORT_TYPE_SKIP
                    row_result.diff = self.get_diff(None, None,
                                                    real_dry_run)
                else:
                    row_result.import_type = RowResult.IMPORT_TYPE_DELETE
                    self.delete_instance(instance, real_dry_run)
                    row_result.diff = self.get_diff(original, None,
                                                    real_dry_run)
            else:
                self.import_obj(instance, row, real_dry_run)
                if self.skip_row(instance, original):
                    row_result.import_type = RowResult.IMPORT_TYPE_SKIP
                else:
                    self.save_instance(instance, real_dry_run)
                    self.save_m2m(instance, row, real_dry_run)
                    # Add object info to RowResult for LogEntry
                    row_result.object_repr = force_text(instance)
                    row_result.object_id = instance.pk
                row_result.diff = self.get_diff(original, instance,
                                                real_dry_run)
        except Exception as e:
            # There is no point logging a transaction error for each row
            # when only the original error is likely to be relevant
            if not isinstance(e, TransactionManagementError):
                logging.exception(e)
            tb_info = traceback.format_exc(2)
            row_result.errors.append(Error(e, tb_info, row))
            if raise_errors:
                if use_transactions:
                    savepoint_rollback(sp1)
                six.reraise(*sys.exc_info())
        if (row_result.import_type != RowResult.IMPORT_TYPE_SKIP or
                self._meta.report_skipped):
            result.rows.append(row_result)

    if use_transactions:
        if dry_run or result.has_errors():
            savepoint_rollback(sp1)
        else:
            savepoint_commit(sp1)

    return result
