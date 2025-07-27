import logging
from pathlib import Path

logger = logging.getLogger(__name__+"_parametrer_log")
logger.setLevel(logging.INFO)
logger.addHandler(
    logging.FileHandler(Path(__file__).resolve().parent / "log_decorator.log")  # Adjust the path as needed
)
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        returned_val = func(*args, **kwargs)
        logger.log(
            logging.INFO,
            f"function: {func.__name__} "
            f"positional parameters: {args or 'none'} "
            f"keyword parameters: {kwargs or 'none'} "
            f"return: {returned_val or 'none'} "
        )
        return returned_val
    return wrapper