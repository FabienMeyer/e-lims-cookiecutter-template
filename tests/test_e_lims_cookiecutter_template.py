"""`e_lims_cookiecutter_template` tests."""

import pytest

from e_lims_cookiecutter_template import e_lims_cookiecutter_template


@pytest.fixture()
def name() -> str:
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return 'World'


def test_content(name: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert 'Hello World' in e_lims_cookiecutter_template.hello(name)
