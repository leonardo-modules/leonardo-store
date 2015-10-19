
def patch_tables2():

    from django_tables2.columns import linkcolumn
    from .linkcolumn import render
    linkcolumn.LinkColumn.render = render
