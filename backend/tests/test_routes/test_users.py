import json
 
 
def test_create_user(client):
    data = {"username":"testuser123","email":"testuseasdasdr@nofoobar.com","password":"testing"}
    response = client.post("/user",json.dumps(data))
    assert response.status_code == 200 or 307
    assert response.json()["is_active"] == True
    assert response.json()["email"] == "testuseasdasdr@nofoobar.com"
