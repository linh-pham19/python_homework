def type_converter(type_of_output):
    def decorator_wrapper(func):
        def wrapper(*args, **kwargs):
            x= func(*args, **kwargs)
            if type_of_output == 'str':
                return str(x)
            elif type_of_output == 'int':
                return int(x)
            elif type_of_output == 'float':
                return float(x)
            else:
                return "Unsupported type. Type must be 'str', 'int', or 'float'."
        return wrapper
    return decorator_wrapper