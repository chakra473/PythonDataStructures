"""
    @Author: Chakravarthy
    @Date: 2022-06-24 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-24 14:13:15
    @Title : Python Code for calling external command in pyton.
"""
import logger_config
import os

title_name = "Python Code for calling external command in pyton "
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def call_external_command(command):
    os.system(command)


if __name__ == "__main__":
    command = input("enter the external command to be executed in python")
    logger_config.logger.info(f"user entered command is {command}")
    call_external_command(command)
