import pymongo
import mongoengine

# Connect to client (specified) and create database named BROWNIEDB
def start_BrownieDB():
    BROWNIEDB_HOST = 'localhost'
    BROWNIEDB_PORT = 27017
    BROWNIEDB_NAME = "BROWNIEDB"

    client = pymongo.MongoClient(BROWNIEDB_HOST,BROWNIEDB_PORT)
    db = client[BROWNIEDB_NAME]

    USERS = db.USERS
    EVENTS = db.EVENTS
    DEALS = db.DEALS
    BUSINESSES = db.BUSINESSES
