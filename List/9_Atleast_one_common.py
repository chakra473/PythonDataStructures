"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to Find at least one common element two list
"""
import logger_config
import create_list

title_name = "Python Code to Find at least one common element two list"
user_name = input("enter your name: ")
logger_config.logger.info(f"TITLE\n{title_name}")
logger_config.logger.info(f"user name who is running the code is {user_name}")


def find_common(list_1, list_2):
    """ 
        Description: 
            This function is Finding at least one common element from two list
        Parameter:
            Two List as argument
        Return:
            returns True or False
    """
    result = [i for i in list_1 for j in list_2 if i == j]
    if len(result) > 0:
        return True
    else:
        return False


# Main Code
if __name__ == "__main__":
    list_element_1 = create_list.create_string_list()
    list_element_2 = create_list.create_string_list()
    result = find_common(list_element_1, list_element_2)
    logger_config.logger.info(f"\nIs {list_element_1} and {list_element_2} have at least one common element : {result}")
