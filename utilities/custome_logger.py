import inspect
import logging

def customLogger(loglevel=logging.DEBUG):
    #gets the name of the class / method from where the method is called
    loggerName = inspect.stack()[1][3]
    print(loggerName)
    logger = logging.getLogger(loggerName)
    #by default , log all message
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("automation.log".format(loggerName), mode='a')
    filehandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger