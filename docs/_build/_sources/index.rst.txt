.. BenchlingAPI documentation master file, created by
   sphinx-quickstart on Thu Sep  7 18:50:04 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

BenchlingAPI documentation
========================================

BenchlingAPI is a python3 wrapper for making Benchling requests.



**Requirements:**

* Python3
* A Benchling API key (https://api.benchling.com/docs/)


**Features:**

* Accessing Benchling sequences and folders
* Creating new sequences and folders
* Searching through sequences and folders using regular expressions
* Converting Benchling sequence JSON to genbank or FASTA files
* Opening and accessing sequences in a Benchling Share links


**Installation:**

::

   cd directory/to/benchlingapi
   pip install .

**Initialization and usage:**

.. code-block:: python

   from benchlingapi import BenchlingAPI

   api_key = "asdgkjahga7dgsd9g8sadg"
   api = BenchlingAPI(api_key)
   seq = api.sequences[0] # get metadata of first sequence
   api.get_sequence(seq["id"])

.. toctree::
   :maxdepth: 2

**File Types**

Examples:

* Example Benchling folder JSON :download:`folder.json <../tests/example_outputs/example_folder.json>`.
* Example Benchling sequence JSON :download:`folder.json <../tests/example_outputs/example_sequence.json>`.

Code
==================

.. automodule:: benchlingapi
   :members: