"""
Durante todo o ciclo de vida da aplicacao é interessante manter somente uma
instancia do mongoclient, pois a criacão da mesma é custosa
"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.server_api import ServerApi
from seed_documents import movie_list

MONGODB_URI = ""
client = MongoClient(MONGODB_URI, server_api=ServerApi(
    version='1', strict=True, deprecation_errors=True))

try:
    database = client.get_database("sample_mflix")
    movies = database.get_collection("movies")

    query = movie_list
    movie = movies.insert_many(query)

    print(movie)

    client.close()

except Exception as e:
    raise ConnectionFailure(
        message="Unable to find the document due to the following error: ") from e
