"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to Sum all the items in list
"""
import logger_config

title_name = "Python Code to Sum all the items in list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def sum_items_in_list(list1):
    total = 0
    for i in list1:
        total += i
    return total


if __name__ == "__main__":
    list1 = []
    # number of elements as input
    num = int(input("Enter number of elements : "))
    # iterating till the range
    for j in range(0, num):
        ele = int(input(f"enter the value {j + 1}: "))
        list1.append(ele)  # adding the element
    logger_config.logger.info(f"list of values user enters is {list1}")
    logger_config.logger.info(f"sum of all the items in the list {list1} is {sum_items_in_list(list1)}")
