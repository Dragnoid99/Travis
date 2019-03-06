from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

@fixture
def add_5_2_fixture():
    return 7


def test_check_add(add_5_2_fixture):
    assert add ( 5 , 2 ) == add_5_2_fixture
    assert add ( 4 , 4 ) == 7

@fixture
def subtract_5_2_fixture():
    return 3

def test_check_subtract(subtract_5_2_fixture):
    assert subtract ( 5 , 2 ) == subtract_5_2_fixture
    assert subtract ( 5 , 3 ) == 3

@fixture
def multiply_5_2_fixture():
    return 10
    
def test_check_multiply(multiply_5_2_fixture):
    assert multiply ( 5 , 2 ) == multiply_5_2_fixture
    assert multiply ( 5 , 3 ) == 10

@fixture
def divide_5_2_fixture():
    return 2.5

def test_numbers_5_2_divide(divide_5_2_fixture):
    assert divide ( 5 , 2 ) == divide_5_2_fixture
    
