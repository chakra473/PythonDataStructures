"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to remove duplicates from list
"""
import logger_config
import create_list

title_name = "Python Code to remove duplicates from list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def remove_duplicate(list_element):
    """
    This method removes duplicates in the list
    :param list_element: list of elements without duplicates
    """
    new_list_1 = []
    [new_list_1.append(i) for i in list_element if i not in new_list_1]
    logger_config.logger.info(f"New List after removing duplicates : {new_list_1}")
    return new_list_1


def remove_duplicate_using_set(list_element):
    """
    This method removes duplicates in the list using set
    :param list_element: list of elements without duplicates
    """
    new_list_2 = list(set(list_element))
    logger_config.logger.info(f"New List after removing duplicates : {new_list_2}")
    return new_list_2


def main():
    list_element = create_list.create_string_list()
    logger_config.logger.info(f"list of values user enters is {list_element}")
    remove_duplicate(list_element)
    remove_duplicate_using_set(list_element)


if __name__ == "__main__":
    main()
