from .create_mongo_collection import create_mongo_collection
from .create_module import create_module


def create_module_with_mongo_collection(name: str, version: int) -> None:
    create_mongo_collection(name, version)
    create_module(name, version, True)
