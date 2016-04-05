"""Python automatically compiles Python source code when you import a module,
 so the easiest way to create a PYC file is to import it. If you have a module mymodule.py, just do:
"""

import py_compile
# below can be used or can be ignored
# import test_file_for_compile_example
py_compile.compile("test_file_for_compile_example.py")

