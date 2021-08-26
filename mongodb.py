import pymongo
import ssl
from GUI import Welcome_Window as ww
import GUI
class DB:

    def __init__(self):
        user={
            'username':'mydb',
            'password':'13sabSADKA',
            'database':'data'
        }
        db_url="mongodb+srv://{username}:{password}@cluster0.ba1xc.mongodb.net/{database}?retryWrites=true&w=majority".format_map(user)
        #client = pymongo.MongoClient(db_url)
        client = pymongo.MongoClient(db_url, ssl_cert_reqs=ssl.CERT_NONE)
        #print(client)


        print("DB Connection Created :)")


        self.db = client['data']
        self.collections = self.db.list_collection_names()

    def insert(self,document):
        self.collection = self.db['student']
        self.collection.insert_one(document)
        print("Document Inserted")

        return

    def fetch_collections(self): #this gives all collections in databasee
        print("Fetching Collections from DB")
        for collection in self.collections:
            print(collection)
        return



    def fetching_documennts(self,collection_name): #this gives document in specific collection
        self.collection=self.db[collection_name]
        documents=self.collection.find()

        for document in documents:
            print(document)
        return

    def conditional_fetch(self,collection_name,roll_no,email):#fectiing with document where 'id' is
        self.collection=self.db[collection_name]
        query={'roll':roll_no,'email':email}
        documents=self.collection.find(query)
        counter=False
        student_data=[]
        attribute=['name','roll','class','email','gender']
        for document in documents:
            counter=True
            print(document)
            for attributes in attribute:
                student_data.append(document[attributes])

            GUI.Show_Data(student_data)


        if counter==False:
            print('Incorrect roll no or email \nNew User?Register')
            ww.msgboxes(self)

            return



    def delete_document(self, collection_name, roll_no):
        self.collection = self.db[collection_name]
        query = {'roll': roll_no}
        document = self.collection.find_one_and_delete(query)
        print(document,"DELETED")

    def update_document(self,collection_name, roll_no):
        self.collection=self.db[collection_name]
        document={}
        query ={'roll':roll_no}
        self.collection.find_one_and_update(query,document)




