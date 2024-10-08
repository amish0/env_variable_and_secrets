import os
from pymongo import MongoClient

# Get MongoDB credentials from environment variables
username = os.getenv('MANGODB_USERNAME')
password = os.getenv('MANGODB_PASSWORD')
host = os.getenv('MANGODB_CLUSTER_ADDRESS', 'localhost')  # Default to localhost if not set
port = os.getenv('MONGODB_PORT', '3000')  # Default MongoDB port
database_name = os.getenv('MONGODB_DATABASE')

print(f"Connecting to MongoDB at {host}:{port}...")
print(f"Database: {database_name}")
print(f"Username: {username}")
print(f"Password: {password}")


# Construct the MongoDB connection string
# connection_string = mongodb+srv://amishkumar562:<db_password>@cluster0.vstwl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
connection_string = f'mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority&appName=Cluster0'
# print(f"Connection string: {connection_string}")
# Create a MongoClient object
client = MongoClient(connection_string)
print("Connected to MongoDB!")

# if database is not present then it will create a new database

# Access the specific database
db = client[database_name]
print("Accessed database:", db)

# Access a specific collection
collection = db['mycollection']
print("Accessed collection:", collection)

# display all data in the table
print("All data in the table:")
for x in collection.find():
    print(x)
# Example: Insert a document into the collection
document = {
    "name": "amish Kumar",
    "email": "amitest@test.com",
    "age": 45
}
result = collection.insert_one(document)
print("Document inserted with ID:", result.inserted_id)

# Example: Find a document in the collection
user = collection.find_one({"name": "Jane Doe"})
print("Found document:", user)

# Close the connection (optional)

# display all data in the table
print("All data in the table:")
for x in collection.find():
    print(x)

# display list of tables in the database
print("List of tables in the database:")
print(db.list_collection_names())
client.close()
