
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

Stores
======

* A store locator page using Google maps for geocoding. It also supports using the browser's location to show the nearest stores.
* Store detail pages including opening hours
* Store groups

Integration Oscar Stores see https://github.com/django-oscar/django-oscar-stores

Dependencies
------------

GeoDjango is used so a spatial database is required. We recommend PostGIS. Django's docs include some installation instructions although it is renowned for being tricky.

Spatialite is another option although it can be tricky to set up. On Ubuntu, you can do the following:

.. code-block:: bash
 
    sudo apt-get install spatialite-bin libspatialite3 libgeos++-dev libgdal-dev libproj0

The pysqlite python package is also required although it doesn't support C extensions by default. To work-around this, there are two options:

Download the package, edit setup.cfg to enable C extensions and install:

.. code-block:: bash

    $ pip install pysqlite --no-install
    $ vim $VIRTUAL_ENV/build/pysqlite/setup.cfg
    $ pip install pysqlite

Installation
------------

.. code-block:: bash

    pip install leonardo-module-eshop[stores]

Configuration
-------------

Add ``eshop_stores`` to leonardo APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'eshop_stores',
        ...
    ]

    STORES_GEOGRAPHIC_SRID = 3577  # This is used for distance calculations. See http://spatialreference.org for more details.
    STORES_GEODETIC_SRID = 4326
    STORES_MAX_SEARCH_DISTANCE = None  # This filters stores in queries by distance. Units can be set using distance object:

Read More
=========

* https://github.com/django-oscar