# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling and error handling,
#              Collecting data from the user, pickling it,
#              then unpickling it to present back to the user.
#              Using error handling to keep the input of the ID
#              to only numeric values.
# ChangeLog (Who,When,What):
# Bruenger,5.25.2021,Created script
# Bruenger,5.25.2021,using Lab 7-1 as a baseline
# Bruenger,5.25.2021,added error handling for user entering ID
#                    that isn't a number.

import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []


# Processing -------------------------------------- #
def pickle_file(file_name, contents):
    objFile = open(file_name, "wb")
    pickle.dump(contents, objFile)
    objFile.close()


def unpickle_file(file_name):
    objFile = open(file_name, "rb")
    contents = pickle.load(objFile)
    objFile.close()
    print(contents)


# Presentation ------------------------------------ #
# Get Customer ID and Name From user, then store it in a list object
try:
    intCustID = int(input("Enter a Customer ID: "))
    strName = str(input("Enter a Name: "))
    strDate = str(input("Enter Customer Join Date: "))
    lstCustomer = [intCustID, strName, strDate]
    # Store the list object into a binary file
    pickle_file(strFileName, lstCustomer)
    # Read the data from the file into a new list object and display the contents
    unpickle_file(strFileName)


# Error Handling----------------------------------- #
# Providing custom error code if user enters value for Customer ID that isn't a number
except ValueError as e:
    print("Customer ID must be a number")

