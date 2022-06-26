'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 01:36:43
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 01:36:43
    @Title : Find words by length
'''
from createlist import *
from LoggingFile import *
logger  = func()

if __name__ == "__main__":
    list_element = create_string_list()
    logger.info(list_element)
    length = int(input("Enter any length value : "))
    new_list = [i for i in list_element if len(i) > length ]
    logger.info(f"All element having length longer than {length} are : {new_list}")