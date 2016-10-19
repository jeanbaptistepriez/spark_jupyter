Jupyter DataFrame output for PySpark
------------------------------------
 
 This library customizes some DataFrame outputs.
 
  - The method `.show()` is overloaded and outputs an html table 
    with movable columns (instead of a reStructuredText table).
  - The method `.printSchema()` is overloaded and outputs also an html
    table.
 
Dependencies
------------

The movable feature is only available using the online javascript 
library http://johnny.github.io/jquery-sortable/.

Install
-------

Run the command: `python setup.py install`

Example
-------

_cf._ `Example.ipynb`