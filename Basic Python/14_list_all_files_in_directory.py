"""
    @Author: Chakravarthy
    @Date: 2022-06-24 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-24 14:13:15
    @Title : Python program to list all files in a directory in Python.
"""
import logger_config
from os import listdir
from os.path import isfile, join

title_name = "Python program to list all files in a directory in Python"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def list_all_files_in_directory(directory_name):
    """
    this method lists all the files in a directory
    :param directory_name: user input (name of directory)
    :return: list of files in directory
    """
    files_list = []
    for path in listdir(directory_name):
        if isfile(join(directory_name, path)):
            files_list.append(path)
    return files_list


if __name__ == "__main__":
    directory_name = input("enter the directory name")
    logger_config.logger.info(f"name of the directory user entered is {directory_name}")
    output_list = (list_all_files_in_directory(directory_name))
    for i in output_list:
        logger_config.logger.info(i)
