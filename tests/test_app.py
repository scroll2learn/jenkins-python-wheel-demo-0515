from jenkins_python_demo.app import add


def test_add_two_positive_numbers():
    result = add(10, 20)
    assert result == 30


def test_add_negative_number():
    result = add(-5, 10)
    assert result == 5


def test_add_zero():
    result = add(0, 20)
    assert result == 20
