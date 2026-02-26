def test_register_success(client):
    r = client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "password123"})
    assert r.status_code == 201

def test_register_duplicate(client):
    client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "password123"})
    r = client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "autre"})
    assert r.status_code == 400

def test_login_success(client):
    client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "password123"})
    r = client.post("/api/v1/auth/login", data={"username": "test@example.com", "password": "password123"})
    assert r.status_code == 200
    assert "access_token" in r.json()

def test_login_wrong_password(client):
    client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "password123"})
    r = client.post("/api/v1/auth/login", data={"username": "test@example.com", "password": "mauvais"})
    assert r.status_code == 401
