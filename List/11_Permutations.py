'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 02:24:31
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 02:24:31
    @Title : Permutations of list
'''
import itertools
from createlist import *

def permutations(list_element, result=[]):
    """ 
        Description: 
            This function is printing all the permutations
        Parameter:
            Two List as argument second one is for result list
        Return:
            Nothing
    """
    if(len(list_element) == 0):
        logger.info(result)
    else:
        for i in range(len(list_element)):
            permutations(list_element[:i] + list_element[i+1:], result + list_element[i:i+1])

from LoggingFile import *
logger  = func()
if __name__ == "__main__":
    list_element = create_string_list()
    # Method 1
    list_of_permutations = list(itertools.permutations(list_element))
    logger.info("\nList of all permutations : ")
    logger.info(list_of_permutations)
    # Method 2
    logger.info("\nList of all permutations : ")
    permutations(list_element)
    
            
