import uuid

import pytest

from conftest import load_user_data
from utils.apis import  APIS

@pytest.fixture(scope="module")
def apis():
    return APIS() #created object for APIS class this is how we create object for class through this we can access methods of common files

def test_get_user_validation(apis): # use apis object here
    response = apis.get("users") # so we pass end point here and thruogh apis object call method get
    print(response.json())
    assert response.status_code == 200 # here we are doing assertions
    assert len(response.json()) > 0

def test_create_user_validation(apis,load_user_data): # use apis object here
    #user_data = {
     #   "name" : "sameer",
     #   "username" : "QA User",
     #   "email" : "sameer@gmail.com" # real time everytime we need to change email id if not then will fail
    # }
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com" #this will generate new email id everytime so our script will not fail
    print(unique_email)
    user_data["email"] = unique_email   #with this everytime new email id will use for testing

    response = apis.post("users",user_data) # so we pass end point here and thruogh apis object call method get
    print(response.json())
    assert response.status_code == 201
    assert response.json()["name"] == "sameer"
    id = response.json()['id']
    response = apis.get("users/10")  # here we again checking through get requests that post data update or not
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == "Clementina DuBuque"

def test_update_user_validation(apis): # use apis object here
    user_data = {
        "name" : "sameer nalawade",
        "username" : "QA User",
        "email" : "sameer@gmail.com" # real time everytime we need to change email id if not then will fail
    }
    response = apis.put("users/1",user_data) # so we pass end point here and thruogh apis object call method get
    print(response.json())
    assert response.status_code == 200 #here we only updating so will get 200 ok code
    assert response.json()["name"] == "sameer nalawade"

def test_delete_user_validation(apis): # use apis object here
    #this is for delete
    response = apis.delete("users/1") # so we pass end point here and thruogh apis object call method get
    print(response.json())
    assert response.status_code == 200 #here we only updating so will get 200 ok code
