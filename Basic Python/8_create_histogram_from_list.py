"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for Creating histogram from list of integers
"""
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
title_name = "Python Code for Creating histogram from list of integers"
user_name = input("enter your name: ")
logger.info(f"TITLE\n{title_name}")
logger.info(f"user name who is running the code is {user_name}")


def histogram(items):
    logger.info(f"list of values user enters is {items}")
    for n in items:
        output = ''
        times = n
        while times > 0:
            output += '*'
            times = times - 1
        print(output)


if __name__ == "__main__":
    histogram([12, 3, 1, 5, 18])
