import pytest
from volunteer_dashboard_api.users import (
    config, create_app, generate_db, init_db)

TEST_DATABASE_URI = "postgresql://user:password@localhost:5432/test_db"


@pytest.fixture(scope="session")
def app():
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    }
    test_config = {**config, **settings_override}
    app = create_app(app=None, config=test_config)
    return app


@pytest.fixture()
def test_client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def test_db(app):
    db = generate_db(app=app)
    init_db(db=db)
    yield db
    # db.drop_all()


@pytest.fixture
def db_session(test_db):
    connection = test_db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})
    session = test_db.create_scoped_session(options=options)
    test_db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
