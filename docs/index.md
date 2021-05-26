Mike Bruenger
May 25, 2021
Introduction to Python
Assignment07
https://github.com/Bruengerjr/IntroToProg-Python-Mod07.git

#     Picking and Exception Handling
##    Introduction
The purpose of this document is to describe the steps taken to complete Assignment07, which consists of researching Pickling and Exception Handling and applying the learned knowledge.  It will consist of 4 steps, researching pickling and error handling, creating the Assignment07 script, adding additional capabilities to the script, and preparing them for submission.
##    Researching Pickling and Exception Handling
I began by a simple google search for Pickling, this led me to the Python.org site https://docs.python.org/3/library/pickle.html# which helped me understand that pickling is simply the changing of stored data from a human readable todolist.txt file to a binary appdata.dat file similar to how many cell phone apps and computer programs use.

My next google search for Error Handling again led me to the Python.org site https://docs.python.org/3/c-api/exceptions.html this helped to add clarity to what exception handling is all about.  Trying to pre-emptively determine all the possible ways user based failures can occur, and writing useful error messages that can be understood by users without a development background (and in some cases understood specifically by users with a development background.) With the intent of ensuring that your code runs exactly the way you want and guiding the user if they step outside of the lines.
##    Creating the Assignment07 Script
I started off referencing some of the code from the lab, sticking with requesting user input, pickling that data, then un-pickling it and providing it to the user.  This keeps things simple, while still conveying the concept of storing data in the pickled format, and retrieving it from the pickled format back to the application.
##    Adding Additional Capabilities to the Script
I used a try except to provide the user with an easily understood error message that the Customer ID must be a number if input that is not an Integer is entered.
##    Preparing for Submission
In preparation for submission I created the desired folder hierarchy, named the files appropriately, and took the required screenshots of the code in action (Figure 1) , the created dat file (Figure 2), and the custom error message (Figure 3).
         
##    Summary
I have described the process of completing Assignment07 and the steps I took researching pickling and error handling, creating the Assignment07 script, adding additional capabilities to the script, and preparing them for submission.
