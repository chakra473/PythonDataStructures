"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to find word by length from list
"""
import logger_config
import create_list

title_name = "Python Code to find word by length from list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def find_words(list1):
    """
    This method gives elements which are longer than length
    :param list1:list of elements
    :return:list with elements longer than length
    """
    length = int(input("Enter any length value : "))
    new_list = [i for i in list1 if len(i) > length]
    logger_config.logger.info(f"All element having length longer than {length} are : {new_list}")
    return new_list


if __name__ == "__main__":
    list_element = create_list.create_string_list()
    logger_config.logger.info(f"list of values user enters is {list_element}")
    find_words(list_element)
