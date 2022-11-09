import os

from azure.cosmos import CosmosClient, DatabaseProxy

from infrastructure.db.database_provider import DatabaseProvider


class CosmosDatabaseProvider(DatabaseProvider):
    def __init__(self):
        self.db_url = os.environ['COSMOS_URI']
        self.db_key = os.environ['COSMOS_SECRET']

    def get_database(self) -> DatabaseProxy:
        client = CosmosClient(self.db_url, credential=self.db_key, consistency_level='Session')
        return client.get_database_client('ReportingDb')
