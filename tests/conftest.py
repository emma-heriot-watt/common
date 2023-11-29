import os
from pathlib import Path

import pytest


if os.getenv("_PYTEST_RAISE", "0") != "0":

    @pytest.hookimpl(tryfirst=True)
    def pytest_exception_interact(call):
        raise call.excinfo.value

    @pytest.hookimpl(tryfirst=True)
    def pytest_internalerror(excinfo):
        raise excinfo.value


# Import all the fixtures from every file in the tests/fixtures dir.
pytest_plugins = [
    fixture_file.as_posix().replace("/", ".").replace(".py", "")
    for fixture_file in Path().rglob("tests/fixtures/[!__]*.py")
]


os.environ["RUNNING_TESTS"] = "1"
