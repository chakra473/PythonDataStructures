'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-18 22:25:10
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-18 22:25:10
    @Title : Circularly Identical
'''
from createlist import *
from LoggingFile import *
logger  = func()

if __name__ == "__main__":
    list_1 = create()    
    list_2 = create()
    logger.info(f"\nList 1 : {list_1}")
    logger.info(f"\nList 2 : {list_2}")
    str_1 = ' '.join(map(str, list_1*2))
    logger.info(str_1)
    str_2 = ' '.join(map(str, list_2))
    logger.info(str_2)
    if str_2 in str_1:
        logger.info(f"\n{list_1} and {list_2} are circularly identical\n")
    else:
        logger.info(f"\n{list_1} and {list_2} are not circularly identical\n")
    
    
    
    