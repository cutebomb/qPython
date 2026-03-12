update support for numpy>2.0 

qPython
=======

qPython is a Python library providing support for interprocess communication between Python and kdb+ processes, it offers:

- Synchronous and asynchronous queries
- Convenient asynchronous callbacks mechanism
- Support for kdb+ protocol and types: v3.0, v2.6, v<=2.5
- Uncompression of the IPC data stream
- Internal representation of data via numpy arrays (lists, complex types) and numpy data types (atoms)
- Supported on Python 3.10+ and numpy 2.0+

For more details please refer to the `documentation`_.


Installation
------------

git clone https://github.com/cutebomb/qPython && cd qPython
pip install .


