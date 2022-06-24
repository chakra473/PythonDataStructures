"""
    @Author: Chakravarthy
    @Date: 2022-06-24 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-24 14:13:15
    @Title : Python program to list all files in a directory in Python.
"""
import logger_config
import os

title_name = "Python program to list all files in a directory in Python"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def access_environmental_variable(variable):
    logger_config.logger.info(f"accessing all the environmental variables {os.environ}")
    logger_config.logger.info("**---------------------***")
    logger_config.logger.info(f"accessing particular environmental variable {os.environ[variable]}")


if __name__ == "__main__":
    variable = input("enter the environmental  variable to access")
    logger_config.logger.info(f" user entered  variable is  {variable}")
    access_environmental_variable(variable)
