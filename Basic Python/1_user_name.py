"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for username printed backwards
"""


def reverse_order(first_name, last_name):
    """
this function returns text in backwards
    :param first_name: string
    :param last_name: string
    :return: returns string in backwards
    """
    x = first_name[::-1]  # Slice the string starting at the end of the string and move backwards
    y = last_name[::-1]
    return x, y


if __name__ == "__main__":
    first_name = input("enter your first name: ")
    last_name = input("enter your last name: ")
    x1, y1 = reverse_order(first_name, last_name)
    print(f"{x1},{y1}")
