# Generated by ts2python on 2022-12-09 13:12:05.586119


import sys
from enum import Enum, IntEnum
if sys.version_info >= (3, 9, 0):
    from typing import Union, Optional, Any, Generic, TypeVar, Callable, List, Tuple, Dict
    # do not use list, tuple, dict, because contained types won't be forward ref'd
    from collections.abc import Coroutine
else:
    from typing import Union, List, Tuple, Optional, Dict, Any, Generic, TypeVar, Callable, Coroutine


try:
    from ts2python.typeddict_shim import TypedDict, GenericTypedDict, NotRequired, Literal
    # Overwrite typing.TypedDict for Runtime-Validation
except ImportError:
    print("Module ts2python.typeddict_shim not found. Only coarse-grained "
          "runtime type-validation of TypedDicts possible")
    try:
        from typing import TypedDict, Literal
    except ImportError:
        try:
            from ts2python.typing_extensions import TypedDict, Literal
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


try:
    from ts2python.singledispatch_shim import singledispatch, singledispatchmethod
except ImportError:
    print("ts2python.singledispatch_shim not found! @singledispatch-annotation"
          " imported from functools may cause NameErrors on forward-referenced"
          " types.")
    try:
        from functools import singledispatch, singledispatchmethod
    except ImportError:
        print(f"functools.singledispatchmethod does not exist in Python Version "
              f"{sys.version}. This module may therefore fail to run if "
              f"singledispatchmethod is needed, anywhere!")


source_hash__ = "4488453be62cc15e0061ad7693954885 7d045ff68ee19bd4d3ad0032abe2707f"


##### BEGIN OF LSP SPECS


class Measurement(TypedDict, total=True):
    value: str
    unit: str


##### END OF LSP SPECS
