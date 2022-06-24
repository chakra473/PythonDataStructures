"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for printing documents of python inbuilt functions
"""


def print_docs_inbuilt_func(*args):
    """
    This function prints documents of inbuilt functions in python
    :param args: takes multiple arguments
    :return: returns nothing
    """
    for number in args:
        print(number)


if __name__ == "__main__":
    d = abs.__doc__
    print_docs_inbuilt_func(d)
