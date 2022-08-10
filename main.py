from audioop import add
import xdrlib
from fastapi import FastAPI,Depends,HTTPException
from requests import Session
import models
from database import engine, sessionLocal
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel, Field
import math

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

# Pydantic Model for Posting Data in Table
class AddressPost(BaseModel):
    x_corr: float #= Field(gt>0) if need to take only possitive value we can use this Field option here
    y_corr: float
    house_no:str
    city:str
    state:str
    locality:str
    pincode:str

# Try to make a connection
def get_db():
    try:
        db=sessionLocal()
        yield db
    finally:
        db.close()




@app.get('/')
async def home():
    return f"Welcome to home of Address_api. Please go to documentation more API queries avaliable in docs."

# We can get all adresses or by querying through Id
@app.get('/address')
# for each get request first get_db will be executed and will make connection with database.
async def get_address(db: Session= Depends(get_db),id_to_search: Optional[int] = None):
    if id_to_search:
        addressofId=db.query(models.Address).filter(models.Address.id==id_to_search).first()
        if addressofId is not None:
            return addressofId
        raise HTTPException(status_code=404, detail="No Address found with this Id.")
    return db.query(models.Address).all()

# To get addresses with in a distance from given coordinates
@app.get('/address/{dist}')
async def get_in_radius_address( dist: int , x_corr: float , y_corr: float ,db: Session= Depends(get_db) ):
    t=db.query(models.Address).all()
    ans=[]
    for i in t:
        distance=((i.x_corr-x_corr)**2)+((i.y_corr-y_corr)**2)
        if distance<=dist*dist:
            ans.append(i)
    if len(ans)==0:
        raise HTTPException(status_code=404, detail="No Address found with i  this range.")
    return ans

# Post request Logic
@app.post("/address")
async def add_address(address: AddressPost,db: Session= Depends(get_db)):
    Addrees=models.Address()
    Addrees.x_corr=address.x_corr
    Addrees.y_corr=address.y_corr
    Addrees.house_no=address.house_no
    Addrees.locality=address.locality
    Addrees.state=address.state
    Addrees.pincode=address.pincode
    db.add(Addrees)
    db.commit()
    
    return {
        'status_code':201,
        'Post':"Successful"
    }

#put method
@app.put("/{address_id}")
async def update_address(address_id : int,address : AddressPost ,db: Session= Depends(get_db)):
    
    Addrees=db.query(models.Address).filter(models.Address.id==address_id).first()
    if Addrees is None:
        raise HTTPException(status_code=404, detail="No Address found with this Id.")
    Addrees.x_corr=address.x_corr
    Addrees.y_corr=address.y_corr
    Addrees.house_no=address.house_no
    Addrees.locality=address.locality
    Addrees.state=address.state
    Addrees.city=address.city
    Addrees.pincode=address.pincode
    db.add(Addrees)
    db.commit()
    return {
        'status_code':200,
        'Update':"Successful"
    }
  
# Delete Address by id   
@app.delete("/{address_id}")
async def delete_address(address_id: int, db: Session= Depends(get_db)):  
    Addrees=db.query(models.Address).filter(models.Address.id==address_id).first()
    if Addrees is None:
        raise HTTPException(status_code=404, detail="No Address found with this Id.")
    db.query(models.Address).filter(models.Address.id==address_id).delete()
    db.commit()
    return {
        'status_code':200,
        'Delete':"Successful"
    }
    
    

#insert into address values (2,220.22,21.333,'929','Aces_layout','Karnatka','Bangalore','500601');