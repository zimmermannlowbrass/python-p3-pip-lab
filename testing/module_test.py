from lib.versions import python_version, requests_version, pytest_version


def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 9
    assert version_info.micro == 2


def test_requests_version():
    assert requests_version() == "2.25.0"


def test_pytest_version():
    assert pytest_version() == "5.4.2"
