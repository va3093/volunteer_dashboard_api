

def test_index(test_client):
    res = test_client.get('/v1/users/1')
    assert res == "a"
