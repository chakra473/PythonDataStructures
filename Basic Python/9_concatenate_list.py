"""
    @Author: Chakravarthy
    @Date: 2022-06-24 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-24 14:13:15
    @Title : Python Code for Concatenating list into a string
"""
import logger_config

title_name = "Python Code for Concatenating list into a string"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def concatenate_list_to_string(list1):
    """
    This function concatenate list into a string
    :param list1: user input of list
    :return: string
    """
    string1 = ''
    for i in list1:
        string1 = string1 + ' ' + i
    logger_config.logger.info(f"Concatenated list is \"{string1}\"")
    return string1


if __name__ == "__main__":
    list1 = []
    # number of elements as input
    n = int(input("Enter number of elements : "))
    # iterating till the range
    for j in range(0, n):
        ele = input(f"enter the value{j + 1}: ")
        list1.append(ele)  # adding the element
    logger_config.logger.info(f"list of values user enters is {list1}")
    concatenate_list_to_string(list1)
