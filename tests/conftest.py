import pytest
from volunteer_dashboard_api.app import app


@pytest.fixture()
def test_client():
    return app.test_client()