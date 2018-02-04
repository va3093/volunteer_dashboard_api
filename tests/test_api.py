

def test_index(test_client):
    response = test_client.get('/')
    assert response.data == b'Hello World!'
