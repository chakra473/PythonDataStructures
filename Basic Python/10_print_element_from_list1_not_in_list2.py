"""
    @Author: Chakravarthy
    @Date: 2022-06-24 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-24 14:13:15
    @Title : Python Code for print out a set containing all the colors from color_list_1 which are not present in color_list_2.
"""
import logger_config

title_name = "Python Code for print out a set containing all the colors from color_list_1 which are not present in " \
             "color_list_2 "
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def set_difference(color_list1, color_list2):
    """
    This function displays elements from list1 which are not in list2
    :param color_list1: set of elements from user
    :param color_list2: set of elements from user
    :return: returns elements in list1 which is not in list2
    """
    color_list1 = set(color_list1)
    color_list2 = set(color_list2)
    logger_config.logger.info(f"color_list1 = \"{color_list1}\"")
    logger_config.logger.info(f"color_list2 = \"{color_list2}\"")
    output_list = color_list1.difference(color_list2)
    logger_config.logger.info(f"elements in color_list1 which is not in color_list1 = \"{output_list}\"")
    return output_list


if __name__ == "__main__":
    list1 = []
    # number of elements as input
    n = int(input("Enter number of elements for 1st list: "))
    # iterating till the range
    for j in range(0, n):
        ele = input(f"enter the value{j + 1}: ")
        list1.append(ele)  # adding the element
    list2 = []
    # number of elements as input
    m = int(input("Enter number of elements for 2nd list: "))
    # iterating till the range
    for j in range(0, m):
        ele = input(f"enter the value{j + 1}: ")
        list2.append(ele)  # adding the element
    set_difference(list1, list2)
