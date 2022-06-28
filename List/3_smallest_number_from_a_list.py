"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to find the smallest number from a list
"""
import logger_config
import create_list

title_name = "Python Code to find the smallest number from a list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def find_smallest_number_in_list(list1):
    """
    This method finds the smallest number from a list
    :param list1: takes list of items as an argument
    :return:returns the smallest number in the list
    """
    smallest = min(list1)
    return smallest


if __name__ == "__main__":
    list1 = create_list.create_int_list()
    logger_config.logger.info(f"list of values user enters is {list1}")
    logger_config.logger.info(f"Smallest element of all the items in the list {list1} is {find_smallest_number_in_list(list1)}")
