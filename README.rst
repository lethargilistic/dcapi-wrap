Wrapper for dcapi
-----------------
.. image:: https://img.shields.io/pypi/v/dcapi.svg
    :target: https://img.shields.io/pypi/v/dcapi.svg

.. image:: https://img.shields.io/pypi/l/dcapi.svg
    :target: https://img.shields.io/pypi/l/dcapi.svg

.. image:: https://img.shields.io/pypi/pyversions/oam-dl.svg
    :target: https://img.shields.io/pypi/pyversions/oam-dl.svg

A Python wrapper for the commands available in the dcapi REST API.

Usage
~~~~~

.. code:: python

    import dcapi

    character_by_name = dcapi.character('Ai Haibara')
    character_by_id = dcapi.character(1)

If you are using a self-hosted version of the api, you can specify your own
endpoint and port.

.. code:: python

    import dcapi

    api = dcapi.set_url('127.0.0.1:8000')

