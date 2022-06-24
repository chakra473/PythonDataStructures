"""
    @Author: Chakravarthy
    @Date: 2022-06-24 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-24 14:13:15
    @Title : Python Code for checking file exists or not.
"""
import logger_config
import os.path

title_name = "Python Code for checking file exists or not "
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def check_file_exists(file_name):
    """
    this function checks whether given file name exists or not
    :param file_name:
    :return:
    """
    file_exist = os.path.exists(file_name)
    if file_exist:
        logger_config.logger.info(f"the file {file_name} exists")
    else:
        logger_config.logger.info(f"the file {file_name} does not exists")


if __name__ == "__main__":
    file_name = input("enter the file name: ")
    logger_config.logger.info(f"user entered file name is {file_name}")
    check_file_exists(file_name)
