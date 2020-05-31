"""
Logging is used to store all the steps taken in a log file.
It follows a specific order calles as CEWID
C - CRITICAL
E - ERROR
W - WARNING
I - INFO
D - DEBUG
The following code will store the contents in a log file named logfile.log
"""

import logging

logging.basicConfig(filename="4. logfile.log", level=logging.DEBUG)

logging.critical("Message 1")
logging.warn("Messame 3")
logging.error("Message 2")
logging.debug("Message 5")
logging.info("Message 4")
