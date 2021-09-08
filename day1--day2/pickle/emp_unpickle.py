"""
A file with the .dat file extension is a generic data file that stores specific  
information relating to the program that created the file. (store binary information)
"""

import emp, pickle

f = open('emp.csv','rb')
print("Employees Details : ")
while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print('End of file reached...')
        break
    
f.close()

'''
    if we write it without handling the exception we will get the EOFError: Ran out of input
    obj = pickle.load(f)
    obj.display()
'''