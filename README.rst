ip2country
==========
|travis|_ |coveralls|_ |pypibadge|_

-----
About
-----
Lookup country code (iso 3166) by IP address.

-------
Install
-------

.. code:: shell

  $ pip install ip2country

Or

.. code:: shell

  $ python setup.py install


----------
How to use
----------

First: Implement IStore Interface
---------------------------------
You must implement IStore interface in ip2country/interfaces.py.

There is a sample implementation in example/store.
This implementation is stored all records on the system memory.

Second: Store the records
-------------------------
.. code:: python

    store = Store()
    parser = Parser(store)
    with open(RECORD_FILE) as fp:
        parser.do(fp)

See examples/lookup.py:load for more detail.

Third: Lookup the IPAddress
---------------------------

.. code:: python

    store = Store()
    record = store.lookup(IP_ADDRESS)
    if record is None:
        print('Record not found')
    else:
        print('{0} is allocated to {1}'.format(IP_ADDRESS, record.cc))

See examples/lookup.py:main for more detail.


-------------
Run the tests
-------------

.. code:: shell

  $ tox

-------
License
-------
ip2country is licensed under the MIT LICENSE.  See ./LICENSE.rst.


.. _travis: https://travis-ci.org/yosida95/ip2country
.. |travis| image:: https://travis-ci.org/yosida95/ip2country.svg?branch=master

.. _coveralls: https://coveralls.io/r/yosida95/ip2country?branch=master
.. |coveralls| image:: https://coveralls.io/repos/yosida95/ip2country/badge.png?branch=master

.. _pypibadge: http://badge.fury.io/py/ip2country
.. |pypibadge| image:: https://badge.fury.io/py/ip2country.svg?dummy
