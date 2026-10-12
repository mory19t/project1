from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

mylist = [100 , 200 , 400 , 300]



@app.get("/")
def say_hello():
    return {"hello" : "world"}

@app.get("/getitems/")
def get_items():
    return {"output" : mylist}

@app.get("/lastitemlist/")
def last_item():
    return {"output" : mylist[2]}

@app.post("/additem/{new_item}")
def insert_item(new_item : int):
    mylist.append(new_item)
    return {"new output" : mylist}

@app.delete("/deleteitem/")
def delete_item(item : int):
    if item in mylist :
        mylist.remove(item)
        return {"output list after delete" : mylist}
    else :
        return {f"{item} not found in list "}

@app.delete("/deleteindexitem/")
def delete_item_index(index : int):
    mylist.pop(index)
    return {"output list after delete" : mylist}

@app.put("/updateitem/")
def update_item(index : int , new_item):
    if index >= 0 and index < len(mylist) :
        mylist[index] = new_item
        return {"update list " : mylist}

    else :
            return {f"index of {index} , not exist in my list"}


@app.put("/updateitem2/")
def update_item2( old_item : int , new_item : int):
    if old_item in mylist : 
        a =  mylist.index(old_item)
        mylist[a] = new_item
        return {"output" : mylist}
    else :
        return {f"index of {old_item} , not exist in my list"}