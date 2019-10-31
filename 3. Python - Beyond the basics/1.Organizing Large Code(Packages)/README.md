## Modules
- When you import a module it is represented by an object of type `module` . i.e. <class 'module'>

## Package
A package is a special type of module. It can contain other `modules` including other `packages`.
`This allows us to group modules with similar functionality together in ways they communicate their cohesiveness`

```python
import urllib
import urlib.request
type(urllib)                # <class 'module'>
type(urllib.request)        # <class 'module'>

urllib.__path__             # ['/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib']
urllib.request.__path__     # Error

# __path__ indicates a list of file system paths indicating where `urllib` searches to find nested modules.

```

This hints at the general difference in `package` and `module`.
**Packages are generally directories and modules are files**

## sys.path
python checks the path attribute of `sys` i.e. `sys.path`
`sys.path` is nothing more than a list of directories. When you ask python to import a modules it starts with a first directory in `sys.path` and checks for an appropriate file. If no match is found `import error` is raised.

```python
import sys
sys.path            # ['', '/path/', '...', '...']

sys.path[0]         # ''
"""
This first entry in sys.path is empty string. This happens when you start the python interpretor 
with no argument. It instructs python to search for modules first in the current directory
"""

sys.path[-1]        # '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages'
"""the last argument is site package directory where you can install third party modules"""

```

## PYTHONPATH
we can add a path that is not in `sys.path` list by using the command `sys.path.append(path_name)`. 
Another way to include the path in `sys.path` is to export `PYTHONPATH` using `export PYTHONPATH = path_name`. This path will be added in `sys.path` when python interpretor starts.

## Making a Package
- Make a directory with package name
- Create a `__init__.py` file in it. This file ensures that this directory will be used as a package.
- The source file when the package is imported is the `__init__.py`. we can check this by `package_name.__file__`
- `__init__.py` can be used to write code and this code will be executed as soon as the package is imported. So, we can use this to hoist classes from our module

