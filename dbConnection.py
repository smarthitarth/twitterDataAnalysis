class DatabaseConnection:
   
    def createConnectionDB(self):
        
        try:
            self.myclient = MongoClient("mongodb+srv://")

            self.myclient.server_info()
            return True   
        except pymongo.errors.ServerSelectionTimeoutError as err:
            #print("Connection failed to database")
            print(err)
        return False