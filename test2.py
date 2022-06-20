from fastapi import FastAPI,Request
from pymongo import MongoClient,InsertOne
from starlette.responses import JSONResponse
 
from bson.objectid import ObjectId
inventory ={
    1:{
        "name":"Milk",
        "brand":"AMUL",
        "price":31,
        "quantity":"500 ML"
    },
    2: {
        "name":"Milk",
        "brand":"MahiSagar",
        "price":30,
        "quantity":"500 ML"
    },
    3:{
        "name":"SoftDrinks",
        "brand":"Pepsi",
        "price":85,
        "quantity":"1 L"
    },
    4:{
        "name":"SoftDrinks",
        "brand":"Coca-cola",
        "price":85,
        "quantity":"1 L"
    },
    5:{
        "name":"AC",
        "brand":"Panasonic",
        "star-rating":"4",
        "type":"split",
        "size":"1.5 ton",
        "inverter": "Yes",
        "price":35000
    },
    6:{
        "name":"AC",
        "brand":"Voltas",
        "star-rating":"5",
        "type":"split",
        "size":"1.5 ton",
        "price":45000,
        "inverter":"Yes"
    }
}
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-item/{id}")
async def get_item(id:int):
    print(len(inventory))
    return inventory[id]


@app.get("/get-item-by-name/")
async def get_item_by_name(name :str):
    search_list=[inventory[i] for i in range(1,len(inventory)+1) if inventory[i]["name"] == name]
    return search_list          

@app.post("/create-inventory/")
async def create_inventory(inventory:Request)-> JSONResponse:
    print(Request)
    item=await inventory.json()
    print("Item to be inserted",item)
    # Connect to database
    client=MongoClient("localhost",27017)
    #Access the database
    db=client['test']
    #Access the desired collection
    collection=db['inventory']

    #collection.find_one({"name":""})
    insertId=collection.insert_one(item).inserted_id
    #json_str=dumps(list(insertResponse))
    #record=json.loads(json_str)
    if insertId:
        return JSONResponse({"message":"Success","MongoDB_insert_id":str(insertId)})
    else:
        return JSONResponse({"status":"Fail","message":"Oh!!!! uh!!!!!!!!! Something went wrong"})
     
        

