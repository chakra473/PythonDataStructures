'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 01:06:17
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 01:06:17
    @Title : Remove duplicates from list 
'''
from createlist import *
from LoggingFile import *
logger  = func()

if __name__ == "__main__":
    
    list_element = create_string_list()
    
    # Method 1
    new_list_1 = []
    [new_list_1.append(i) for i in list_element if i not in new_list_1]
    logger.info(f"\nNew List after removing duplicates : {new_list_1}")
    
    # Method 2
    new_list_2 = list(set(list_element))
    logger.info(f"\nNew List after removing duplicates : {new_list_2}") 