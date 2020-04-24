import os #interacting with the os
import platform #information about the os
import logging #to log information

if platform.platform().startswith("Windows"): #platform.platform() checks what OS you're using
    logging_file = os.path.join(os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "test.log")
else:
    logging_file = os.path.join(os.getenv("HOME"), "test.log")
    #note: os module join() is different from string method join()

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s : %(levelname)s : %(message)s",
    filename=logging_file,
    filemode="w"
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

#once the program has run, you can check the logging file and will know what
#happened in the program, even though no information was displayed to the
#user running the program