#decorators
#a shortcut to apply wrapper functions
#to wrap functionality with the same code over and over again
#this one is a "retry" decorator -- can be applied to any function, and if any exception
    #is thrown during a run, it is retried again to a max of 5 times with delay between each try

from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")

def retry(f)
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPS + 1):
            try:
                return f(*args, **kwargs)
            except Exception:
                log.exception("Attempt %s/%s failed : %s")