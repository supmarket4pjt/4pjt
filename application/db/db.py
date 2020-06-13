

import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://test:test@supmarket-o5fys.mongodb.net/ShoppingDB?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")
mydb = myclient["ShoppingDB"]
mycol = mydb["utilisateur"]
myart = mydb["Article"]
