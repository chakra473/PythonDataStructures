"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to Count string with condition from list
"""
import logger_config

title_name = "Python Code to Count string with condition from list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def create_tuple(i):
    """ 
        Description: 
            This function is creating integer list of any length
        Parameter:
            None
        Return:
            returns list
    """
    tuple_ele = ()
    no_of_elements = int(input(f"\nEnter how many numbers you want to add in tuple {i + 1}: "))
    for i in range(no_of_elements):
        number = int(input(f"\nEnter {i + 1} th value : "))
        tuple_ele = tuple_ele + (number,)

    return tuple_ele


def get_last_of_tuple(tuple1):
    """ 
        Description: 
            This function is used to get last element of tuple
        Parameter:
            tuple
        Return:
            returns last element of tuple
    """
    return tuple1[-1]


def sort_list_with_key(list1):
    """ 
        Description: 
            This function is sorting list by key
        Parameter:
            list
        Return:
            returns sorted list
    """
    sorted_list = sorted(list1, key=get_last_of_tuple)
    return sorted_list


# Main Code
if __name__ == "__main__":
    # list =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    count = int(input("\nHow many tuple you want to add in list : "))
    list_element = [create_tuple(i) for i in range(count)]
    logger_config.logger.info(f"list of values user enters is {list_element}")
    sorted_list1 = sort_list_with_key(list_element)
    logger_config.logger.info(f"\nSorted list based on tuple last element : {sorted_list1}")
