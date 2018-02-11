

def test_index(test_client):
    test_client.get('/')
    assert True
