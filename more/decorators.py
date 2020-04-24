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

def retry(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except Exception:
                log.exception("Attempt %s/%s failed : %s",
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10*attempt)
        log.critical("All %s attemps failed: %s",
                     MAX_ATTEMPTS,
                     (args, kwargs))
    return wrapper_function

counter = 0

@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    #this will throw an exception in the first call
    #and will work fine in the second call (i.e. a retry))
    if counter < 2:
        raise ValueError(arg)

if __name__ == "__main__":
    save_to_database("Some bad value")