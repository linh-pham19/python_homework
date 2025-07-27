from log_decorator import logger_decorator

#task 1
@logger_decorator
def my_function_1():
    print("hello world")



@logger_decorator
def my_function_2(*args):
    return True

@logger_decorator
def my_function_3(**kwargs):
    return logger_decorator

print("Result from my_function_1():",my_function_1())
print("Result from my_function_2(1, 2, 3):",my_function_2(1, 2, 3))
print("Result from my_function_3(a=1, b=2, c=3:",my_function_3(a=1, b=2, c=3))