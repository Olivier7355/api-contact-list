# Import FastAPI & SQLAlchemy
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import re

# Create the database (contacts.db)
engine = create_engine('sqlite:///./contacts.db')
session = sessionmaker(bind=engine)
Base = declarative_base()

# Create the database table (id, name, phone_number, email)
class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40))
    phone_number = Column(String(20))
    email = Column(String(40))

Base.metadata.create_all(engine)

app = FastAPI()

# Define the get endpoint list_all_contacts (/contacts/)
@app.get('/contacts/')
def list_all_contacts():
    db = session()
    contacts = db.query(Contact).all()
    return contacts

# Define the get endpoint read_contact (/contacts/{contact_id})
@app.get('/contacts/{contact_id}')
def read_contact(contact_id: int):
    db = session()
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail='Contact not found !')
    return contact

# Define the post endpoint create_contact (/contacts/)

# Define the put endpoint update_contact (/contacts/{contact_id})

# Define the delete endpoint delete_contact (/contacts/{contact_id})
