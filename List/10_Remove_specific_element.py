'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 02:13:37
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 02:13:37
    @Title : Clone or copy list
'''
from createlist import *
from LoggingFile import *
logger  = func()
if __name__ == "__main__":
    list_element = create_string_list()
    logger.info(list_element)
    # removing the 0th, 4th and 5th elements.
    list_element.pop(0)
    logger.info(list_element)
    list_element.pop(3)
    logger.info(list_element)
    list_element.pop(3)
    logger.info(f"List after removing 0th,4th and 5th index element : {list_element}")
