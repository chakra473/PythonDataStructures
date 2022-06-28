"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to append a list to the second list
"""

import logger_config as lc
import create_list as cl

title_name = "Python Code to append a list to the second list"
lc.logger.info(f"TITLE\n{title_name}")


def append_list_in_list(no_of_list):
    new_list = [cl.create_string_list() for i in range(no_of_list)]
    lc.logger.info(f"\nList of list : {new_list}")


def main():
    no_of_list = int(input("\nHow many number of list you want to append : "))
    append_list_in_list(no_of_list)


if __name__ == "__main__":
    main()
