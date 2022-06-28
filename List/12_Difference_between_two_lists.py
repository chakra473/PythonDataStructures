"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to find difference between two lists
"""
import itertools

import logger_config
import create_list

title_name = "Python Code to find difference between two lists"
logger_config.logger.info(f"TITLE\n{title_name}")


def find_difference(list_1, list_2):
    """ 
        Description: 
            This function is Finding difference from two list
        Parameter:
            Two List as argument
        Return:
            returns difference of list
    """
    difference_1 = set(list_1).difference(set(list_2))
    difference_2 = set(list_2).difference(set(list_1))

    list_difference = list(difference_1.union(difference_2))
    return list_difference


def main():
    list_1 = create_list.create_string_list()
    list_2 = create_list.create_string_list()
    result = find_difference(list_1, list_2)
    logger_config.logger.info(f"\nDifference between {list_1} and {list_2} is : {result}")


if __name__ == "__main__":
    main()
