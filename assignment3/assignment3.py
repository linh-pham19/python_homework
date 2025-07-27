from type_decorator import type_converter
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


#Task2 
@type_converter("str")
def return_int():
    return 5

@type_converter("int")
def return_string():
    return "not a number"


y = return_int()
print(type(y).__name__)
try: 
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")