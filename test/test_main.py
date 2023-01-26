import pathlib


def foo():
    print(pathlib.Path(__file__).parent.resolve())
