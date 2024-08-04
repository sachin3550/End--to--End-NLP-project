from Hate.logger import logging
from Hate.exception import CustomException


#logging.info("welcome to our project")


try:
    a = 7 / "0"

except Exception as e:
    raise CustomException(e,sys) from e
