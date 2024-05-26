from pymongo import MongoClient
from pymongo.server_api import ServerApi


URI = "mongodb://davidade300:220498@192.168.124.64:27017/admin"
client = MongoClient(URI, server_api=ServerApi(
    version='1', strict=True, deprecation_errors=True))

try:
    database = client.get_database("sample_mflix")
    movies = database.get_collection("movies")

    # Query for a movie that has the title 'Back to the Future'
    query = {"title": "Back to the Future"}
    movie = movies.delete_one(query)

    print(movie)

    client.close()

except Exception as e:
    raise Exception(
        "Unable to find the document due to the following error: ", e) from e
