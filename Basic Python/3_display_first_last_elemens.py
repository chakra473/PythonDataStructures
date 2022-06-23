"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for displaying first and last colours in the given list
"""


def display_first_and_last_element(color_list):
    """
    This method displays first and last element of the given list
    :param color_list: list of colors
    :return: returns nothing
    """
    print(f"the first color in the list is \"{color_list[0].upper()}\"\nthe last color in"
          f" the list is \"{color_list[-1].upper()}\"")


if __name__ == "__main__":
    color_list = ["Red", "Green", "White", "Black"]
    display_first_and_last_element(color_list)
