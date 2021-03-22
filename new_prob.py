#!/usr/bin/python3

import os
import sys

# detect the current working directory and print it
#path = os.getcwd()
#print("The current working directory is %s" % path)



# define the name of the directory to be created

#def prob_template(num, ispy):


y = """
/*
    C++ IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 8:
        [Filler Text]

    Solution & Thinking:
        - TO-DO
*/
"""

x = """
#!/usr/bin/python3
'''
    PYTHON IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 8:
        The foud ajacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 - 5832.
        Find the thirteen adjacent digits in 1000-digit number that have the greatest product. What is the value of this product?

    Solution & Thinking:
        - TO-DO
'''
"""

if __name__ == "main":
    # store arguement number
    input_num = sys.argv[1]
    print("The first arguement is: ", input_num)

    # create name for the folder
    foldername = "test_%s" % (input_num)
    print("Test output: " + foldername)
    filename = "prob_" + input_num
    access_rights = 0o777

    # create name for the files
    

    # try creating the folder
    try:
        os.mkdir(foldername, access_rights)
    except OSError:
        print("Creation of the directory %s failed" % foldername)
    else:
        print("Succesfully created the directory %s" % foldername)


'''
    # Create the python file in the previously created folder - write the template into the file
    with open(foldername+"/"+ filename + ".py", "w+") as f:
        f.writelines(x)

    print("The first arguement is: ", input_num)
    print("Test output: ", foldername)
'''