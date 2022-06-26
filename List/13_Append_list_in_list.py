'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-17 06:18:03
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-17 06:18:03
    @Title : Append one list in another list
'''
from createlist import *
# Main Code
from LoggingFile import *
logger  = func()

if __name__ == "__main__":
    no_of_list = int(input("\nHow many number of list you want to append : "))
    new_list = [create_string_list() for i in range(no_of_list)]
    logger.info(f"\nList of list : {new_list}")
    