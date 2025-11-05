from typing import Any

class Readonly(object):
    """
    from readonly_wrapper import Readonly
    h=Holding('xx','12121',400,24.5)
    p=Readonly(h)
    """
    def __init__(self, obj):
        self._obj=obj

    def __getattr__(self, name):
        return getattr(self._obj, name)
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name == '_obj':
            super().__setattr__(name, value)
        else:
            raise AttributeError('Read Only!')
