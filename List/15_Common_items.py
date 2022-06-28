"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to find common items from two lists
"""

import logger_config as lc
import create_list as cl

title_name = "Python Code to find common items from two lists"
lc.logger.info(f"TITLE\n{title_name}")


def find_common(list1, list2):
    """ 
        Description: 
            This function is Finding common element from two list
        Parameter:
            Two List as argument
        Return:
            returns list of common element
    """
    result1 = [i for i in list1 for j in list2 if i == j]
    return result1


def main():
    list_1 = cl.create_string_list()
    list_2 = cl.create_string_list()
    result = find_common(list_1, list_2)
    lc.logger.info(f"\n{list_1} and {list_2} have common element : {result}")


if __name__ == "__main__":
    main()
