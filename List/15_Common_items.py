'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 06:30:09
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 06:30:09
    @Title : Find all common element from two list
'''
from createlist import *
def find_common(list_1,list_2):    
    """ 
        Description: 
            This function is Finding common element from two list
        Parameter:
            Two List as argument
        Return:
            returns list of common element
    """
    result = [i for i in list_1 for j in list_2 if i == j]
    return result

from LoggingFile import *
logger  = func()
# Main Code
if __name__ == "__main__":
    list_1 = create_string_list()
    list_2 = create_string_list()
    result = find_common(list_1,list_2)
    logger.info(f"\n{list_1} and {list_2} have common element : {result}")
    
    