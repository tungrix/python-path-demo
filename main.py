import pathlib
print(pathlib.Path(__file__).parent.resolve())
from test import test_main

test_main.foo()