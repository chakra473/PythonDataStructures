'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 06:01:50
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 06:01:50
    @Title : Difference between two lists
'''
from createlist import *
def find_difference(list_1,list_2):    
    """ 
        Description: 
            This function is Finding difference from two list
        Parameter:
            Two List as argument
        Return:
            returns difference of list
    """
    difference_1 = set(list_1).difference(set(list_2))
    difference_2 = set(list_2).difference(set(list_1))

    list_difference = list(difference_1.union(difference_2))
    return list_difference

from LoggingFile import *
logger  = func()
# Main Code
if __name__ == "__main__":
    list_1 = create_string_list()
    list_2 = create_string_list()
    result = find_difference( list_1,list_2)
    logger.info(f"\nDifference between {list_1} and {list_2} is : {result}")
    
    