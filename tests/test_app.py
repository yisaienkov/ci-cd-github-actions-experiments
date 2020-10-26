from src import app


def test_index():
    assert app.index() == "Hello, world!!"
