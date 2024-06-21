"""`e-lims-cookiecutter-template` tests."""

import pytest

from e-lims-cookiecutter-template import e-lims-cookiecutter-template


@pytest.fixture
def name() -> str:
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return 'World'


def test_content(name: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert 'Hello World' in e-lims-cookiecutter-template.hello(name)
