
==========================
Leonardo Store integration
==========================

Leonardo Ecommerce built on top of Django-Oscar solution

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo_module_store

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["store"]

Add ``leonardo_store`` to leonardo APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'leonardo_store',
        ...
    ]

Load new template to db

.. code-block:: bash

    python manage.py sync_all

API
===

.. code-block:: bash

    pip install leonardo-module-eshop[api]


Payments
========

Oscar has several backends, but in this time is fully integrated only Paypal.


Paypal
------

https://github.com/django-oscar/django-oscar-paypal

.. code-block:: bash

    pip install leonardo-module-eshop[paypal]

Add ``eshop_stores`` to leonardo APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'eshop_paypal',
        ...
    ]

Read More
=========

* https://github.com/django-oscar
* https://github.com/django-leonardo
* https://github.com/leonardo-modules/leonardo-stores