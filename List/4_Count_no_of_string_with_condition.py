"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to Count string with condition from list
"""
import logger_config
import create_list

title_name = "Python Code to Count string with condition from list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def count_string(list):
    """
        Description:
            This function is counting string based on condition from list
        Parameter:
            It takes list as argument
        Return:
            returns count
    """
    count = 0
    for i in list:
        if len(i) >= 2:
            if i[0] == i[-1]:
                count += 1
    return count


if __name__ == "__main__":
    list1 = create_list.create_string_list()
    logger_config.logger.info(f"list of values user enters is {list1}")
    logger_config.logger.info(f"The count of string having same first and last character and length is greater than 1 "
                              f"are :{count_string(list1)}")
