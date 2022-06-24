"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for Creating histogram from list of integers
"""
import logger_config
title_name = "Python Code for Creating histogram from list of integers"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def histogram(items):
    logger_config.logger.info(f"list of values user enters is {items}")
    for n1 in items:
        output = ''
        times = n1
        while times > 0:
            output += '*'
            times = times - 1
        print(output)


if __name__ == "__main__":
    list1 = []
    # number of elements as input
    n = int(input("Enter number of elements : "))
    # iterating till the range
    for j in range(0, n):
        ele = int(input(f"enter the value{j + 1}: "))
        list1.append(ele)  # adding the element
    histogram(list1)
