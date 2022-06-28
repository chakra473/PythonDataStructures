"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to check whether two lists are circularly identical
"""

import logger_config as lc
import create_list as cl

title_name = "Python Code to check whether two lists are circularly identical."
lc.logger.info(f"TITLE\n{title_name}")


def check_circularly_identical(list1, list2):
    str_1 = ' '.join(map(str, list1 * 2))
    lc.logger.info(str_1)
    str_2 = ' '.join(map(str, list2))
    lc.logger.info(str_2)
    if str_2 in str_1:
        lc.logger.info(f"\n{list1} and {list2} are circularly identical\n")
    else:
        lc.logger.info(f"\n{list1} and {list2} are not circularly identical\n")


def main():
    list_1 = cl.create_int_list()
    list_2 = cl.create_int_list()
    lc.logger.info(f"\nList 1 : {list_1}")
    lc.logger.info(f"\nList 2 : {list_2}")
    check_circularly_identical(list_1, list_2)


if __name__ == "__main__":
    main()
