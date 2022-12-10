import sys
from enum import Enum, IntEnum
if sys.version_info >= (3, 9, 0):
    from typing import Union, Optional, Any, Generic, TypeVar, Callable, List, Tuple, Dict
    # do not use list, tuple, dict, because contained types won't be forward ref'd
    from collections.abc import Coroutine
else:
    from typing import Union, List, Tuple, Optional, Dict, Any, Generic, TypeVar, Callable, Coroutine


try:
    from typing import TypedDict, Literal
except ImportError:
    try:
        from typing_extensions import TypedDict, Literal
    except ImportError:
        print(f'Please install the "typing_extensions" module via the shell '
                f'command "# pip install typing_extensions" before running '
                f'{__file__} with Python-versions <= 3.7!')
try:
    from typing_extensions import NotRequired
except ImportError:
    NotRequired = Optional
if sys.version_info >= (3, 7, 0):  GenericMeta = type
else:
    from typing import GenericMeta
class _GenericTypedDictMeta(GenericMeta):
    def __new__(cls, name, bases, ns, total=True):
        return type.__new__(_GenericTypedDictMeta, name, (dict,), ns)
    __call__ = dict
GenericTypedDict = _GenericTypedDictMeta('TypedDict', (dict,), {})
GenericTypedDict.__module__ = __name__