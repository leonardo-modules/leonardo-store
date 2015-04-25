
==========================
Oscar-Leonardo integration
==========================

Oscar Ecommerce as Leonardo module. Provide new page layout called Eshop and many feincms widgets.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_module_eshop

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["eshop"]

Add ``eshop`` to leonardo APPS list, in the ``local_settings.py``::

    APPS = [
    	...
        'eshop',
        ...
    ]

Load new template to db

.. code-block:: bash

	python manage.py sync_all
