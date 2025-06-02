from string import Template


mongo_service_template = Template(
    """import os
from typing import Literal, get_args, Any

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

DatabaseName = Literal["here database names"]


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

    def get_collection(
        self,
        collection_name: CollectionName,
        database_name: DatabaseName = "here database name",
    ) -> AsyncIOMotorCollection[dict[str, Any]]:
        db = self.client.get_database(database_name)
        return db.get_collection(collection_name)

    async def create_indexes(self):
        pass

"""
)


def get_mongo_service_template() -> str:
    return mongo_service_template.template
