from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
import pprint

def createMongoClient():

    MONGODB_URI = "mongodb+srv://user:password@myatlasclusteredu.hd55ezg.mongodb.net/?retryWrites=true&w=majority&appName=myAtlasClusterEDU"

    client = MongoClient(MONGODB_URI)
    return client

client = createMongoClient()

for db_name in client.list_database_names():
    print(db_name)

db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts


# Insert one document into accounts
new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.utcnow(),
}

result = accounts_collection.insert_one(new_account)
document_id = result.inserted_id
print(f"_id of inserted document: {document_id}")


# Insert multiple documents
new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 267914296,
    },
]

result = accounts_collection.insert_many(new_accounts)
document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")


# find_one()
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)


# Query for multiple documents 
documents_to_find = {"balance": {"$gt": 4700}}

cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))


# update_one()
document_to_update = {"_id": ObjectId("62d6e04ecab6d8e130497482")}
add_to_balance = {"$inc": {"balance": 100}}

pprint.pprint(accounts_collection.find_one(document_to_update))

result = accounts_collection.update_one(document_to_update, add_to_balance)

print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(document_to_update))


# update_many()
select_accounts = {"account_type": "savings"}
set_field = {"$set": {"minimum_balance": 100}}

result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))


# delete_one()
document_to_delete = {"_id": ObjectId("62d6e04ecab6d8e130497485")}

print("Searching for target document before delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

result = accounts_collection.delete_one(document_to_delete)

print("Searching for target document after delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))
print("Documents deleted: " + str(result.deleted_count))


# delete_many()
documents_to_delete = {"balance": {"$lt": 2000}}

print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

result = accounts_collection.delete_many(documents_to_delete)

print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))
print("Documents deleted: " + str(result.deleted_count))


client.close()
