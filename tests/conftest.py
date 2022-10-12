import pytest

from app.app import app


@pytest.fixture()
def test_app(event_loop):
    """passing in event_loop helps avoid 'attached to a different loop' error"""
    app.finalize()
    app.conf.table_cleanup_interval = 1.0
    app.flow_control.resume()
    app.conf.store = "memory://"
    return app
