def test_function():
    def inner_function():
        print('Я в области видимости функции test_function()')

    inner_function()


test_function()

# Следующая строка выдает ошибку: "NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?"
# inner_function()
