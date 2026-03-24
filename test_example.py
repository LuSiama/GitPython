def my_function(a, b):
    return a + b

print(my_function(1, 2))

def test_my_function():
    assert my_function(1,2) == 3

# тест с ошибкой
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_my_function))
#     return suite

# def test_my_function_error():
#     assert my_function(1, 2) == 5
