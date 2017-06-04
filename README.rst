Wrapper for dcapi
-----------------

A Python wrapper for the commands available in the dcapi REST API.

Usage
~~~~~

.. code:: python

    from dcapi import Dcapi

    api = Dcapi()
    character_by_name = api('Ai Haibara')
    character_by_id = api(1)

If you are using a self-hosted version of the api, you can specify your own
endpoint and port.

.. code:: python

    from dcapi import Dcapi

    api = Dcapi('127.0.0.1:8000')

