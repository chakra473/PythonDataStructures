'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 01:56:16
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 01:56:16
    @Title : Find atleast one common element from two list
'''
from createlist import *
def find_common(list_1,list_2):    
    """ 
        Description: 
            This function is Finding atleast one common element from two list
        Parameter:
            Two List as argument
        Return:
            returns True or False
    """
    result = [i for i in list_1 for j in list_2 if i == j]
    if len(result) > 0:
        return True
    else:
        return False

from LoggingFile import *
logger  = func()
# Main Code
if __name__ == "__main__":
    list_1 = create_string_list()
    list_2 = create_string_list()
    result = find_common(list_1,list_2)
    logger.info(f"\nIs {list_1} and {list_2} have atleast one common element : {result}")
    
    