"""

Purpose: P1 assignment - learning python

Author: Bambee Garfield



"""
import math  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# get the info from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
dogs_count = int(input("\nEnter the number of dogs you have: "))

cats_count = int(input("\nEnter the number of cats you have: "))

# calculate the total number of pets
pets_count = dogs_count + cats_count

# log the results
logger.info(f"The total number of pets you have is {pets_count}.")
logger.info("Pets are the best!")


# get the average number of pets
pets_average = (dogs_count * cats_count) / 2

# log the results
logger.info(f"The average number of pets you have is {pets_average}.")
logger.info("This could be higher!")

# calculate the product
pets_product = dogs_count * cats_count

# log the results
logger.info(f"If you multiply your cats and dogs together, you get {pets_product}.")
logger.info("This is a weird calculation.")

#calculate the smaller number
if dogs_count < cats_count:
    logger.info(f"The smallest pet number you have is dogs at {dogs_count}.")

if dogs_count > cats_count:
    logger.info(f"The smallest pet number you have is cats at {cats_count}.")

if dogs_count == cats_count:
    logger.info(f"You have the same number of dogs and cats.")

#calculate the larger number
if dogs_count < cats_count:
    logger.info(f"The largest pet number you have is cats at {cats_count}.")

if dogs_count > cats_count:
    logger.info(f"The Largest pet number you have is dogs at {dogs_count}.")

if dogs_count == cats_count:
    logger.info(f"You have the same number of dogs and cats.")

#calculate the range

# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())