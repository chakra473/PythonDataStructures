"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to  generate all permutations of a list
"""
import itertools

import logger_config
import create_list

title_name = "Python Code to  generate all permutations of a list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def permutations(list_element, result=[]):
    """ 
        Description: 
            This function is printing all the permutations
        Parameter:
            Two List as argument second one is for result list
        Return:
            Nothing
    """
    if len(list_element) == 0:
        logger_config.logger.info(result)
    else:
        for i in range(len(list_element)):
            print(result + list_element[i:i + 1])
            permutations(list_element[:i] + list_element[i + 1:], result + list_element[i:i + 1])


def main():
    list_element = create_list.create_string_list()
    # Method 1
    list_of_permutations = list(itertools.permutations(list_element))
    logger_config.logger.info("\nList of all permutations : ")
    logger_config.logger.info(list_of_permutations)
    # Method 2
    logger_config.logger.info("\nList of all permutations : ")
    permutations(list_element)


if __name__ == "__main__":
    main()
