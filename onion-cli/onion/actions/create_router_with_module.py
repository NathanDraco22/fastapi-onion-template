from .create_module import create_module
from .create_router import create_router


def create_router_with_module(name: str, version: int) -> None:
    create_module(name, version, False)
    create_router(name, version, True)
