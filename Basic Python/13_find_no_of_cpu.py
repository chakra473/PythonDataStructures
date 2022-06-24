"""
    @Author: Chakravarthy
    @Date: 2022-06-24 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-24 14:13:15
    @Title : Python Code for finding number of CPUs used.
"""
import logger_config
import multiprocessing

title_name = "Python Code for finding number of CPUs used"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def find_no_of_cpu():
    """
    this function finds number of CPUs used
    :return: number of CPUs
    """
    return multiprocessing.cpu_count()


if __name__ == "__main__":
    logger_config.logger.info(f"number of CPUs used is/are {find_no_of_cpu()}")
