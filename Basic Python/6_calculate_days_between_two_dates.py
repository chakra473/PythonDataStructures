"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for Calculating number of days between two days
"""
from datetime import date
import logger_config


def calculate_no_of_days_between_dates(year1, month1, day1, year2, month2, day2):
    f_date = date(year1, month1, day1)
    l_date = date(year2, month2, day2)
    delta = l_date - f_date
    logger_config.logger.info(f"Difference between these two dates \"{a}-{b}-{c}\" and \"{x}-{y}-{z}\" is {delta.days}")
    return delta.days


if __name__ == "__main__":
    try:
        title_name = "Python Code for Calculating number of days between two days"
        user_name = input("enter your name: ")
        logger_config.logger.info(f"TITLE\n{title_name}")
        logger_config.logger.info(f"user name who is running the code is {user_name}")
        a, b, c = (input("enter the first date in YYYY MM DD format: ").split())
        x, y, z = (input("enter the last date in YYYY MM DD format: ").split())
        x, y, z = [int(i) for i in [x, y, z]]
        a, b, c = [int(j) for j in [a, b, c]]
        logger_config.logger.info("input is correct")
        calculate_no_of_days_between_dates(a, b, c, x, y, z)
    except ValueError as err:
        logger_config.logger.error(f"The error is :{err}")
