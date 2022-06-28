"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to Multiply all the items in list
"""
import logger_config
import create_list

title_name = "Python Code to Multiply all the items in list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def multiply_items_in_list(list1):
    """
    This method multiplies all the items in the list
    :param list1: takes list of items as an argument
    :return:returns multiplies of all items in the list
    """
    total = 1
    for i in list1:
        total *= i
    return total


if __name__ == "__main__":
    list1 = create_list.create_int_list()
    logger_config.logger.info(f"list of values user enters is {list1}")
    logger_config.logger.info(f"Multiple of all the items in the list {list1} is {multiply_items_in_list(list1)}")
