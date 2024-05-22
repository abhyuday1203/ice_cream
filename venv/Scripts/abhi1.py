#string = "python is powerful"
#length= len(string)
#print(length)
#string = "Hello, Python!"
#uppercase_string = string.upper()
#print(uppercase_string)
#n=int(input ("enter a number :"))  <----- if else topic begins
#if (n>0):
   # print(n , 'is positive')
#if (n<0):
   # print(n , 'is negative')
#if (n%6 == 0):
    #if(n%3 == 0):
      #print('divisible by 6 and 3')
#else:
    #print('not divisible by 6 and 3')
#if ((n%9 == 0) and (n%18 == 0)): <----- this is using 'and' function
    #print('divisible')
#else:
    #print('not divisible')
#per=int(input("enter marks :"))  <--------------example prob if else
#if (per > 90):
 #   print('Grade A')
#if ((per > 80) and (per <= 90)):
 #   print('Grade B')
#if ((per >= 60) and (per <= 80)):
 #   print('Grade C')
#if (per < 60):
 #   print('Grade D')
#num=int(input("enter any number :")) <-------------- example
#if (num % 3 == 0):
    #print('last digit of num divisible by 3')
#else:
    #print('last digit of num not divisible by 3')

#Cost = int(input("enter the cost price of the bike :")) <------------ example
#if (Cost > 100000):
 #   tax = Cost * 0.015
#elif (Cost > 50000) and (Cost <= 100000):
 #   tax = Cost * 0.01
#else :
  #  tax = Cost * 0.005
#print(" tax to be paid ",tax)
# new topic - 'for Loop'______________________________________________________
#for i in range (1,7):
 #   for j in range (1,7):
  #      print(i , j)
   # print(' - ')
#print("+++++++")
#for i in range (1,7): ---------------> for loop example with condition
 #   for j in range (1,7):
  #      if (i + j == 5):
   #         print(i , j)
    #print(' - ')
#print("+++++++")
#num=int(input("enter any number:")) ---------------> table of a given number
#for i in range (1,11):
 #   print(num*i)
#num=int(input("enter any number:"))
#def getproduct(n):
 #   product = 1
  #  num = str(n)
   # for i in num :
    # product = product * int(i)

   # return product

#n = 4513
#print (getproduct(n))
#------------------------------------------ new topic > lists
#lst = [3,6,7,9,10,77,45,1,2,] example
#print(lst)
#for i in range (len(lst)):
 #   print(i,lst[i])
#num = [1,5,6,6,6,] -------------------------- example
#for i in range (len(num)):
 #   print(num[i] , end = " ")
#fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'] ------------------------> example
# print([fruit for fruit in fruits if len(fruit) >5 ])
#fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']--------E.g
#print([len(fruit) for fruit in fruits ])
#fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange' ]-- eg vowels in fruits
#vowels = ['a', 'e', 'i', 'o', 'u']
#for vowels in fruits :
    #if vowels in fruits:
     #   print(fruits)
# DICTIONARY PROBLEMS #
#dct = {"Name":"Ram" , "Age":23}  --------- Example
#print(dct)
#dct.update({"City":"Salem"})
#print(dct)
#dct["Gender"] = "Male"
#print(dct)
#import datetime -_--------------
#print(datetime.datetime.now())
#import string _________________
#print (string.punctuation)
