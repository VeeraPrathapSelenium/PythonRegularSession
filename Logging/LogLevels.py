import logging

logging.basicConfig(filename="Features.log",
                    format="%(asctime)s:%(levelname)s:%(funcName)s:%(message)s:%(lineno)d:%(filename)s")


logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
a=10
b=20

print("The Sum of two number is {}".format(a+b))
logger.debug("The Sum of two number is {}".format(a+b))
logger.info("The Sum of two number is {}".format(a+b))
logger.warning("The Sum of two number is {}".format(a+b))
logger.error("The Sum of two number is {}".format(a+b))
logger.critical("The Sum of two number is {}".format(a+b))