from sqlalchemy import Boolean,Column,Integer,Float,String
from database import Base

# address table with specified columns and contraints will be created in
class Address(Base):
    __tablename__ ="address"
    
    id = Column(Integer,primary_key=True,index=True)
    x_corr = Column(Float(8),index=True)
    y_corr= Column(Float(8),index=True)
    house_no = Column(String)
    locality= Column(String)
    state = Column(String)
    city = Column(String)
    pincode = Column(String)
    
