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

