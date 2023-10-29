
from pymongo.mongo_client import MongoClient

print("hello")

def main():
    print("insisde main")
    uri = "mongodb+srv://vandit:vandit<password>@cluster0.9ktnsxf.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server

    client = MongoClient(uri)
    
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()