def get_token(client):
    client.post("/api/v1/auth/register", json={"email": "admin@test.com", "password": "password123"})
    r = client.post("/api/v1/auth/login", data={"username": "admin@test.com", "password": "password123"})
    return r.json()["access_token"]

def test_list_empty(client):
    r = client.get("/api/v1/cereals/")
    assert r.status_code == 200 and r.json() == []

def test_create_cereal(client):
    token = get_token(client)
    r = client.post("/api/v1/cereals/",
        json={"name": "Mais", "region": "Ouagadougou", "price_per_kg": 0.35},
        headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 201

def test_create_unauthorized(client):
    r = client.post("/api/v1/cereals/", json={"name": "Mil", "region": "Bobo", "price_per_kg": 0.30})
    assert r.status_code == 401

def test_filter_by_region(client):
    token = get_token(client)
    h = {"Authorization": f"Bearer {token}"}
    client.post("/api/v1/cereals/", json={"name": "Mais", "region": "Ouagadougou", "price_per_kg": 0.35}, headers=h)
    client.post("/api/v1/cereals/", json={"name": "Mil", "region": "Bobo-Dioulasso", "price_per_kg": 0.30}, headers=h)
    r = client.get("/api/v1/cereals/?region=Ouaga")
    assert r.status_code == 200 and len(r.json()) == 1
