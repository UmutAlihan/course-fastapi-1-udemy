import json

def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.asd.com",
        "location": "USA,NY",
        "description": "Testing",
        "date_posted": "2022-08-01"
    }

    response = client.post("/jobs/create-job", json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200 or 307
    assert response.json()["company"] == "testhoo"
    assert response.json()["description"] == "Testing"


def test_retreive_job_by_id(client, normal_user_token_headers):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.asd.com",
        "location": "USA,NY",
        "description": "Testing",
        "date_posted": "2022-08-01"
    }

    client.post("/jobs/create-job", json.dumps(data), headers=normal_user_token_headers)
    response = client.get("/jobs/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"

    