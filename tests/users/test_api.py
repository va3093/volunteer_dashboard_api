from volunteer_dashboard_api.users.models.users import User


def test_create_user(test_client, db_session):
    # Given
    body = dict(
        user_name="test",
        email="test@email.com"
    )

    # When
    res = test_client.post('/v1/users', data=body)
    saved_users = db_session.query(User).all()

    # Then
    assert res.status_code == 201
    assert len(saved_users) == 1
