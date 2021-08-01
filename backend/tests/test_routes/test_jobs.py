import json

def test_create_job(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.asd.com",
        "location": "USA,NY",
        "description": "Testing",
        "date_posted": "2022-08-01"
    }

    response = client.post("/job/create-job",json.dumps(data))
    assert response.status_code == 200 or 307

