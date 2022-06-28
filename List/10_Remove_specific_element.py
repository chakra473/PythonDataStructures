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


if __name__ == "__main__":
    list_element = create_list.create_string_list()
    logger_config.logger.info(list_element)
    # removing the 0th, 4th and 5th elements.
    list_element.pop(0)
    logger_config.logger.info(list_element)
    list_element.pop(3)
    logger_config.logger.info(list_element)
    list_element.pop(3)
    logger_config.logger.info(f"List after removing 0th,4th and 5th index element : {list_element}")
