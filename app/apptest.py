from main import app

def client_test():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Test App" in response.data