"""
Jupyter DataFrame output for PySpark

AUTHORS:
- Jean-Baptiste Priez (2016-11) --  initial version

"""
# ****************************************************************************
#      Copyright (C) 2016 Jean-Baptiste Priez
#
# Distributed  under  the  terms  of  the  GNU  General  Public  License (GPL)
#                         http://www.gnu.org/licenses/
# ****************************************************************************

import sys
default_stdout = sys.stdout
default_stderr = sys.stderr
reload(sys)
sys.setdefaultencoding("utf-8")
sys.stdout = default_stdout
sys.stderr = default_stderr

import spark_jupyter.pyspark
