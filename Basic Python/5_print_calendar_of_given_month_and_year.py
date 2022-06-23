"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for printing calendar of given month and year
"""
import calendar


def display_calendar(year, month):
    """
    This function displays calendar of given month and year passed in argument
    :param month: takes month as argument
    :param year:takes year as argument
    :return:returns calendar of given month and year
    """
    return calendar.month(year, month)


if __name__ == "__main__":
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    print(display_calendar(year, month))
