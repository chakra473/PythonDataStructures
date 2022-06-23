"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for Checking Specified Value present in group of Values
"""
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def check_value_in_list(list_of_num=None, value=None):
    print(value)
    for i in range(len(list_of_num)):
        if list_of_num[i] == value:
            logger.info(f"the given value {value} is present in the group of values")
            return True

    logger.info(f"the given value {value} is not present in the group of values")
    return False


if __name__ == "__main__":
    try:
        title_name = "Python Code for Checking Specified Value present in group of Values"
        user_name = input("enter your name: ")
        logger.info(f"TITLE\n{title_name}")
        logger.info(f"user name who is running the code is {user_name}")
        list1 = []
        # number of elements as input
        n = int(input("Enter number of elements : "))
        # iterating till the range
        for j in range(0, n):
            ele = int(input(f"enter the value{j+1}: "))
            list1.append(ele)  # adding the element
        value1 = int(input("enter the value to be checked in the list: "))
        logger.info(f"list of values user enters is {list1}")
        print(check_value_in_list(list1, value1))
    except ValueError as err:
        logger.warning(err)
