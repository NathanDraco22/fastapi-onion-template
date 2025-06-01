from string import Template


mongo_service_template = Template(
    """import os
from typing import Literal, get_args, Any

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from pymongo import ASCENDING, IndexModel

CollectionName = Literal["here names"]

DatabaseName = Literal["here database name"]


class MongoService:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(MongoService, cls).__new__(cls)
        return cls.instance

    client: AsyncIOMotorClient[dict[str, Any]]

    async def init_service(self):
        url: str = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        self.client = AsyncIOMotorClient(url)
        await self.create_indexes()

    async def create_indexes(self):
        collection_names = get_args(CollectionName)

        for collection_name in collection_names:
            collection = self.get_collection(collection_name)

            await collection.create_indexes(
                [
                    IndexModel([("id", ASCENDING)], unique=True),
                ]
            )

    def get_collection(
        self,
        collection_name: CollectionName,
        database_name: DatabaseName = "here database name",
    ) -> AsyncIOMotorCollection[dict[str, Any]]:
        db = self.client.get_database(database_name)
        return db.get_collection(collection_name)
"""
)


def get_mongo_service_template() -> str:
    return mongo_service_template.template
