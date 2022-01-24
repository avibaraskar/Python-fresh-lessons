#!/usr/bin/env python
# coding: utf-8

# # Boolean Expressions:

# In[177]:


True and False


# In[178]:


True or False


# In[179]:


not True


# In[180]:


True is False


# In[181]:


True is True


# In[182]:


# (Addition,Subtraction,Multiplication, Divide in True-False i.e True = 1, False = 0)
True + False


# In[183]:


# Boolean in Data format
'b' is 'x'


# In[184]:


10 is 11


# In[185]:


10 is 10


# In[186]:


# (== means compare to)
10 ==10


# In[187]:


8 == 9


# In[188]:


True and False or True


# # Number : Use of Python in Numbers,Calculations and Variables:

# In[189]:


False + False


# In[190]:


50 - 80/40


# In[191]:


85/50-25/2000


# In[192]:


90 - (90*80)


# In[193]:


17/3


# In[194]:


# (Note : (//) floor divison discard the fraction term in the code)
17//3


# In[195]:


#(the % operator returns the remainder of the division)
17 % 3  


# In[196]:


#( With Python, it is possible to use the ** operator to calculate powers)

5**2   


# In[197]:


2**7


# In[198]:


1285**12


# In[199]:


#(The equal sign (=) is used to assign a value to a variable. Afterwards,no result is displayed before the next interactive prompt:)
    
length = 85  
breadth = 95

length * breadth


# In[200]:


# (assigning a new variable through mathmatical expressions)

a = 20
b = 30

c = a + b
print (c)


# In[201]:


c * 10


# # Strings in python :

# In[202]:


x= "Python "
y= "is a powerful "
z= "language"
type (x)


# In[203]:


print ( x + y + z )


# In[204]:


print ('wow ' + 'python ' + 'is ' + 'easy')


# In[205]:


# (you can also use ',' instead of '+' for adding any string into statement)
print ('wow ' + 'python ' + 'is ' , 'easy')


# In[206]:


# (you can convert number into string but not vice versa)
print ( "day " + str(2))


# # Data Structures
# # 1) List:

# In[207]:


# List ([]) set of instructions or data put into list
A = ["a",1,2.32,855]
A


# In[208]:


# List are mutable and it can hold all types of data(integers, String, Boolean, float)
marks = [80,90,50,100,20]
marks


# In[209]:


#copying a list - it is necessary if you do not want to share the original data to keep it intact
copy_marks = marks
copy_marks


# In[210]:


# Example
A = [2.583,8.535,652.8,89.58]
B = A
B


# In[211]:


print (B)


# In[212]:


# List function helps string characters to separate each other(In python, String is used to sequence all the characters in the data)

list('shankar')


# In[213]:


list('powerranger')


# In[214]:


# List do not separate characters in integer data type - Error
list(1345658)


# 1.1 Append : You can add(in the end) or insert an arbitrary index in a List,this is called appending 
# 
# 
# Append command =
#                       syntax.append('object')
#                     

# In[ ]:


names=['anshul','ankush','aman']
names.append('Avi')
print(names)


# In[ ]:


names.append('Adarsh')
names.append('aafreen')
names


# 1.2 Insert : To add some data in between the list (or) in starting Insert command is used.
# 
# INDEXING : assigning the data with specific no. to address them is called Indexing.
#   
#   i.e. Index is the assigned place to object data
#    
#    
#    Command used in Insert : 
#    
#    list[2000,3000,4000,5000]
# 
# Forward Index no.: 0   ,  1  ,  2   ,  3
# 
# Backward Index  : -4 ,  -3  , -2  ,  -1
#    
# 
#    Syntax.insert(Index,object)

# In[ ]:


names.insert(0,'Dimpu')
names


# In[ ]:


names.insert(4,'d souza')
names


# In[ ]:


salary =[48000,45500,42000,50000]
salary.insert(3,80000)
salary


# In[ ]:


salary =[48000,45500,42000,50000]
salary


# In[ ]:


salary =[48000,45500,42000,50000]
salary.insert(2,850000)
salary


# **Length calculation Command: to check how many elements are there in the list
# 
# Command: len(syntax)

# In[ ]:


len(salary)


# SLICING: Finding/Fetching elements/objects based on Index no.:
# 
# Note: we can also fetch data from backward direction as well 
# 
# Ex : 
# 
#       list[2000,3000,4000,5000]
# 
# Forward Index no.: 0   ,  1  ,  2   ,  3
# 
# Backward Index  : -4 ,  -3  , -2  ,  -1
# 
# Command: syntax[Index no.]
# 

# In[ ]:


salary[2]


# In[ ]:


salary[4]


# In[ ]:


salary[-1]


# In[ ]:


salary[-5]


# Slicing Examples:
# If we need to extract data between indexes,then we can use 
# 
# command : syntax[Index a : Index z]

# In[ ]:


#Grab index 1 and everything past it
salary =[48000,45500,42000,50000]
salary[1: ]


# In[ ]:


#Grab everything before index 3(excluding Index 3)

salary[:3]


# In[ ]:


#Grab everthing between Index 1 to Index 3
salary[1:3]


# we can also use '+' to concatenate lists,just like we did for strings
# 
# (Note : Addition changes is not permanently added to list)

# In[ ]:


salary + [85000]


# In[ ]:


# Changes is not permanent in list
salary


# In[ ]:


salary =[48000,45500,42000,50000]
salary


# In[ ]:


# To make changes permanent
salary = salary + [85000]
salary


# In[ ]:


# To multiply the list to make it double,triple, or muliply with any no.(multiplication is not a permanent function in list)
salary * 4


# In[ ]:


# Doubling is not permanent
salary


# In[ ]:


# To create some design in we can use multiplication
print ('=' * 80)
print ('                               Anshul Saxena                              ')
print ('+' * 80)


# # Advance List :
# 1) Count : Counting specific data in list( for repeatative objects in List)
# 
# command : syntax.count(data)

# In[ ]:


marks = [25,85,35,45,65,82,82,32,56,49]


# In[ ]:


marks.count(82)


# 2) Index : finding the place of the data/object
# 
# Command : marks.index(object)

# In[ ]:


# Note : Even 82 is occuring twice the index defined will be of the first object
marks.index(82)


# In[ ]:


marks.index(49)


# 3) Extend : Extending the objects/data in list (or) adding the data in the list
# 
# This is different from append as append only add 1 object at a time while extend can add as many possible.
# 
# Command : syntax.extend([object 1, object 2, object 3,....So on])
# 
# print(syntax)

# In[ ]:


employee = ['shyam','pratik','Rohit','Vivek','Anshuman','kartik']


# In[ ]:


employee.extend(['Aditya','Abhishek','Parth'])
print(employee)


# In[ ]:


rollno = [1,2,8,4,5,6,9]
rollno.extend([11,12,13,14,15])
print(rollno)


#  4) Pop : popping out or deleting the data from the List
#  
#  Command: syntax.pop(Index no.)
#  
#  For the last element in list : syntax.pop()

# In[ ]:


soldier_names = ["Raj","Rajesh","Upen","Sulabh","Jayant"]


# In[ ]:


soldier_names


# In[ ]:


#For last element you do not need to define index no.
soldier_names.pop()


# In[ ]:


soldier_names.pop(3)


# 5)Remove: Remove helps in removal of duplicate elements/data from the list.
# 
# Command : syntax.remove(element)

# In[ ]:


roll_number = [11,22,44,55,44,88,99,55]


# In[ ]:


roll_number


# In[ ]:


roll_number.remove(55)


# In[ ]:


roll_number   #(Double clicked)


# In[ ]:


roll_number.remove(44)


# In[ ]:


roll_number


# 6) Reverse : Reverse order of list
# 
# Command : syntax.reverse()

# In[ ]:


First = [1,2,3,4,5]


# In[ ]:


First.reverse()


# In[ ]:


First


# 7) Sort : Sort will sort your list in place(Ascending or descending order)
# 
# Command: syntax.sort()

# In[ ]:


marks = [25,38,49,55,37,26,47,55,60,74,88,38]


# In[ ]:


marks.sort()


# In[ ]:


marks


# In[ ]:


#sort in descending order
marks.sort(reverse = True)


# In[ ]:


marks


# # 2) Tuples:
# Tuples are immutable, They are represented by ()
# 
# No possibilty or making any change
# 
# We can create tuples in mixed type of data sets

# In[ ]:


work_location = ('Bengaluru','Hyderabad','Chennai','Delhi')


# In[ ]:


work_location


# In[ ]:


# Tuple is not mutable
work_location.append('Noida')


# In[ ]:


type(work_location)


# #How we can add object in Tuple
# 1) converting into list
# 2) append the data
# 3)convert into tuple

# In[ ]:


work_location = list(work_location)


# In[ ]:


type(work_location)


# In[ ]:


work_location.append('Noida')


# In[ ]:


work_location


# In[ ]:


work_location = tuple(work_location)


# In[ ]:


work_location


# In[ ]:


# Checking length of Tuple(Same as List)
len(work_location)


# In[ ]:


#check index position of Specific object
work_location.index('Noida')


# In[20]:


#count - Similar to List
roll_number = (1,2,3,4,5,6,5,8,9,8,7)


# In[21]:


roll_number


# In[22]:


roll_number.count(8)


# # 3) Sets:
# 
# A set is an unordered collection data type that is iterable,mutable and has no duplicate element.
# whenever a tuple or list is converted into set, it remove all the repeatative terms and will sequence them
# 

# In[24]:


roll_number = set(roll_number)


# In[25]:


roll_number


# In[26]:


roll_number.add(11)


# In[27]:


roll_number


# In[28]:


# In set, the addition does not happen in end, It actually happens according to the sequence and set structure
roll_number.add(10)


# In[29]:


roll_number


# # Dictionaries : 
# 
# We have learned types of data structure earlier (i.e. List,Tuple,Set), Now these data structure when combined to form a meaningful structure with multiple data like in Tabular form is considered as Dictionaries.
# Dictionaries are denoted by '{}' Curly brackets.
# 
# Keys :          
# Name 
# Salary
# Gender
# 
# Values
# : Akash, Anirudh, Anshul
# : 50000, 60000, 70000
# : M , M , M
# 
# 
# 
# 

# In[30]:


#constructing a Dictionary
my_dict = {'key 1' : 'value 1','key 2' : 'value 2'}


# In[31]:


my_dict


# In[220]:


# Calling values by their key . Always use [Key]
my_dict['key 2']


# In[34]:


# Note: Dictionaries are very flexible in the data types they can hold.
# you can hold up data in any form of data (list,tuple,set)
my_dict = {'roll_number': 123,'subjects': ['computer','science','maths','social'],'marks': [23,82,45,35]}


# In[35]:


my_dict


# In[36]:


# Calling items in dictionaries
my_dict['subjects']


# In[37]:


# Calling index of the items
my_dict['subjects'][3]


# In[38]:


# To get the data in Uppercase or lowercase(methods calling)
my_dict['subjects'][2].lower()


# In[39]:


my_dict['subjects'][2].upper()


# In[40]:


#Adding/Substracting marks to the first element:
my_dict['marks'][2]= my_dict['marks'][2] + 30


# In[41]:


my_dict['marks']


# In[42]:


#This method of direct adding will not give permanent change in the Dictionary. Hence above method is mandatory for permanent change
my_dict['marks'][3] + 30


# In[43]:


my_dict['marks']


# In[44]:


my_dict['marks'][0] = my_dict['marks'][0] - 10


# In[14]:


my_dict


# In[45]:


my_dict


# In[46]:


# Another easy method for adding/substracting
my_dict['marks'][2] += 20


# In[47]:


my_dict


# In[48]:


my_dict['marks'][3] -= 13


# In[49]:


my_dict


# In[ ]:




