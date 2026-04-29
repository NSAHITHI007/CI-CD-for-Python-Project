from Src.math_operations import add, subtract, multiply, divide
def test_add():
    assert add(2, 3)==5
    assert add(-1, 1)==0
def test_sub():
    assert sub(5, 2)==3
    assert sub(0, 5)==-5
    assert sub(-1, -1)==0
    assert sub(10, 5)==5
    