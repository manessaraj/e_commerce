# conftest.py
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment(monkeypatch):
    monkeypatch.setenv("DB_NAME", "test_db")
