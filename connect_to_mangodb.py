import os
from pymongo import MongoClient

# Get MongoDB credentials from environment variables
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')
host = os.getenv('MANGODB_CLUSTER_ADDRESS', 'localhost')  # Default to localhost if not set
port = os.getenv('MONGODB_PORT', '3000')  # Default MongoDB port
database_name = os.getenv('MONGODB_DATABASE')

print(f"Connecting to MongoDB at {host}:{port}...")
print(f"Database: {database_name}")
print(f"Username: {username}")
print(f"Password: {password}")


# Construct the MongoDB connection string
connection_string = f"mongodb://{username}:{password}@{host}:{port}/{database_name}"

# Create a MongoClient object
client = MongoClient(connection_string)

# Access the specific database
db = client[database_name]

# Access a specific collection
collection = db['mycollection']

# Example: Insert a document into the collection
document = {
    "name": "Jane Doe",
    "email": "janedoe@example.com",
    "age": 25
}
result = collection.insert_one(document)
print("Document inserted with ID:", result.inserted_id)

# Example: Find a document in the collection
user = collection.find_one({"name": "Jane Doe"})
print("Found document:", user)

# Close the connection (optional)
client.close()
