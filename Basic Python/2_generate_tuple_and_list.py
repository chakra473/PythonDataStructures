"""
    @Author: Chakravarthy
    @Date: 2022-06-23 14:13:07
    @Last Modified by: Chakravarthy
    @Last Modified time: 2022-06-23 14:13:15
    @Title : Python Code for generating tuple and list
"""


def generate_tuple_and_list(user_input):
    """
This function generates string into list and tuple
    :param user_input: string of numbers separated by comma
    :return: tuple and list
    """
    list_1 = user_input.split(",")
    tuple_1 = tuple(list_1)
    print('List : ', list_1)
    print('Tuple : ', tuple_1)
    return list_1, tuple_1


if __name__ == "__main__":
    values = input("Input some comma separated numbers : ")
    a, b = (generate_tuple_and_list(values))
    print(type(a))
    print(type(b))
