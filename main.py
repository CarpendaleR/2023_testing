# Testing stuff all day


#importing
from importingtestV1 import test_one_one

def func_is_it():
    '''is it an int'''
    try:
        var5 = int(input(f"Input an integer"))
    except:
        print(f"Not an integer")
        var5 = func_is_it()
    return var5

var3 = int(input("Number"))
var4 = test_one_one(var3)
print(f"Answer= {var4}")
var5 = func_is_it()
print(var5)
