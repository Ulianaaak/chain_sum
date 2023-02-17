#chain_sum(5)() => 5
#chain_sum(5)(2)() => 7
#chain_sum(5)(100)(-10)() => 95

def chain_sum(number):
    result = number
    def wrapper(number2=None):
        nonlocal result
         #добавление доступа result для функции chain_sum
        if number2 is None:
            return result
        #если number2 нет, то выводит результат(number)
        result += number2
        return wrapper
    return wrapper

print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)() )
