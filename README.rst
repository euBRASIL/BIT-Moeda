euBRASIL( CryptoREAL )
=======================================

Este é o Projeto para a criação de uma crypto-moeda no Brasil.

BIT-Moeda

https://bit-moeda.readthedocs.io/pt/latest/

Python Code Analyzer
====================

The `code_analyzer.py` script provides a way to analyze and execute Python code snippets.
Its primary purpose is to check for syntax and runtime errors in a given string of Python code.

The script first uses the `ast` module to parse the code and check for any `SyntaxError` exceptions.
If the syntax is valid, it then proceeds to execute the code. If any exceptions occur during
execution, they are caught and reported.

**Usage**

To analyze a Python code string from the command line:

.. code-block:: bash

   python code_analyzer.py "your python code here"

**Example**

.. code-block:: bash

   python code_analyzer.py "print('Hello')\na = 1/0"

This will output:

.. code-block:: text

   Error: division by zero
