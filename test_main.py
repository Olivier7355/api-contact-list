# Import TestClient
from fastapi.testclient import TestClient
from main import app, engine, Contact, Base, session

client = TestClient(app)

# Define the test_create_contact
def test_create_contact():

    # Clean the database & create a contact
    """
    WARNING :
    Do not execute these tests on the production database. It will erase all the data.
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    contact_data = {
        "name": "Jean Dupuis",
        "phone_number": "1234567890",
        "email": "jeande@etest.com"
    }
    response = client.post("/contacts/", json=contact_data)

    # Check that the contact was created successfully
    assert response.status_code == 200
    assert response.json() == {"message": "Contact with id 1 created !"}
    db = session()
    contact = db.query(Contact).filter(Contact.name == "Jean Dupuis").first()
    assert contact is not None

# Define the test_update_contact

# Define the test_delete_contact

