"""
    @Author: Chakravarthy
    @Date: 2022-06-26 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-26 14:13:15
    @Title : Python Code to create integer and string list of any length
"""


def create_int_list():
    """
        Description:
            This function is creating integer list of any length
        Parameter:
            None
        Return:
            returns list
    """
    no_of_elements = int(input("\nEnter how many numbers you want to add in list : "))
    list_of_numbers = [int(input(f"\nEnter {i + 1} th value : ")) for i in range(no_of_elements)]
    return list_of_numbers


def create_string_list():
    """
        Description:
            This function is creating string list of any length
        Parameter:
            None
        Return:
            returns list
    """
    no_of_elements = int(input("\nEnter how many element you want to add in list : "))
    list_of_string = [input(f"\nEnter {i + 1} th value : ") for i in range(no_of_elements)]
    return list_of_string
