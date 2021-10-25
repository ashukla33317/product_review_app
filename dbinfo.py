from pymongo import MongoClient, mongo_client

username="admin_1"
password="qzddhFc9MJ2PA0Se"
mongo_atlas_url=f"mongodb+srv://{username}:{password}@cluster0.c698d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client=MongoClient(mongo_atlas_url)
database_name="mini_project"
database=client[database_name]