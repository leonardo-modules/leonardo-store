
==========================
Leonardo Store integration
==========================

Leonardo Ecommerce built on top of Django-Oscar solution

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-store

.. code-block:: bash

    pip install leonardo-store[cod,api,paypal]

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["store"]

Configuration
=============

Add extra config spec into ``local_settings.py``

    LEONARDO_CONF_SPEC = {
        'store_profile_actions': [],
    }


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

    pip install leonardo-store[api]


Payments
========

Leonardo Store has simple Plugable Payment System for Django Oscar which is basically inspired from shipping method.

Inherit from ``leonardo_store.payments.PaymentMethod`` and define your Payment Method details.

call ``override_checkout`` from ``leonardo_store.payments.utils`` for example in ``app.ready`` method.

Thats all, your Payment Method will be available in payment method view

Paypal
------

.. code-block:: bash

    pip install leonardo-store[paypal]

Cash on Delivery
----------------

.. code-block:: bash

    pip install leonardo-store[cod]


Bank Transfer
-------------

.. code-block:: bash

    pip install leonardo-store[banktransfer]


Shipping
========

Leonardo Store uses ``leonardo_store.shipping.repository.ModelRepository`` as default Shipping provider. This Repository gets all ``WeightBased`` ship methods and provides it. For shipping discount uses offers which affects Basket.

Model
=====

Generate image from model::

    python manage.py graph_models --pygraphviz -g -o store.png catalogue checkout order customer brand partner address analytics basket offer payment promotions shipping voucher wishlists


Read More
=========

* https://github.com/django-oscar
* https://github.com/django-leonardo
* https://github.com/leonardo-modules/leonardo-stores