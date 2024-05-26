"""testing pymongo
    """
from pymongo import MongoClient

URI = "mongodb://davidade300:220498@192.168.124.64:27017/admin"
client = MongoClient(URI)

try:
    database = client.get_database("sample_mflix")
    movies = database.get_collection("movies")

    # Query for a movie that has the title 'Back to the Future'
    query = {"title": "Back to the Future"}
    movie = movies.insert_one(query)

    print(movies.find_one({"title": "Back to the Future"}))

    client.close()

except Exception as e:
    raise Exception(
        "Unable to find the document due to the following error: ", e) from e
