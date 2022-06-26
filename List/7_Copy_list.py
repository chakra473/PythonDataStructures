'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 01:21:39
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 01:21:39
    @Title : Clone or copy list
'''
from createlist import *
from LoggingFile import *
logger  = func()

if __name__ == "__main__":
    list_element = create_string_list()
    logger.info("\nOriginal List : ")
    logger.info(list_element)
    logger.info("\nCopy list : ")
    # Method 1 Using slicing
    copy_list = list_element[:] 
    logger.info(copy_list)
    # Method 2 Using extend method
    copy_list = []
    copy_list.extend(list_element)
    logger.info(copy_list)
    # Method 3 Using copy method
    list_copy = list_element.copy()
    logger.info(list_copy)
    
    