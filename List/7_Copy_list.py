"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to copy list from another list
"""
import logger_config
import create_list

title_name = "Python Code to copy list from another list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def copy_list_using_slicing(list1):
    """
    This method copy the list by using slicing
    :param list1: list of elements
    :return:copied list from list1
    """
    copy_list = list1[:]
    logger_config.logger.info(copy_list)
    return copy_list


def copy_list_using_extend_method(list1):
    """
    This method copy the list by using extend method
    :param list1: list of elements
    :return:copied list from list1
    """
    copy_list = []
    copy_list.extend(list1)
    logger_config.logger.info(copy_list)
    return copy_list


def copy_list_using_copy_method(list1):
    """
    This method copy the list by using copy method
    :param list1: list of elements
    :return:copied list from list1
    """
    list_copy = list1.copy()
    logger_config.logger.info(list_copy)
    return list_copy


if __name__ == "__main__":
    list_element = create_list.create_string_list()
    logger_config.logger.info("\nOriginal List : ")
    logger_config.logger.info(list_element)
    logger_config.logger.info("\nCopy list : ")
    copy_list_using_slicing(list_element)
    copy_list_using_extend_method(list_element)
    copy_list_using_copy_method(list_element)
