import pytest
def my_function(a, b):
    return a + b

print(my_function(1, 2))

def test_my_function():
    assert my_function(1, 2) == 3

# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_my_function))
#     return suite


# тест с ошибкой
def test_my_function_error():
    assert my_function(1, 2) == 5
