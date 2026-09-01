# create list
my_list = [10,20, 30,40,50,11]
# reverse the order of list
my_list.reverse()
#print the reversed list
(print(my_list))

# print common elements  in list1 and list2
empty_list = []
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
for i in list1:
     if i in list2:
       empty_list.append(i)
print(empty_list)


# hear original_list with duplicate values
#create an empty_list to store unique elements
unique_list = []
original_list = [1 ,2 ,2, 3, 4, 4, 5 ]
for i in original_list:
    # check if the elements is not in unique_list
     if i not in unique_list:
        unique_list.append(i)
print(unique_list) 


# given dublicate _list
dublicate_list = [1 ,2, 2, 3, 4, 4, 5]
empty_list = []
for i in dublicate_list:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)

# list concenation
#create two lists
fruits = ["Apple", "Banana", "Orange", "grapes"]
vegitables =["potato", "Brinjal", "Beans", "Carrot"]
items = fruits + vegitables 
print("Concatenated List:", items)

# List repetition
colors = ["Red", "BLue", "Green"]
result = []
for i in range(3):
    result.extend(colors) 
    print(result)

# create a list of numbers
numbers = [10, 20, 30, 40, 50, 60, 70]
#  create an empty_list to store odd indices
result = []
# hear take length of the number is 6 
for i in range(len(numbers)):
    #indeces should be odd
      if i % 2 != 0:
          result.append(numbers[i])
print("Original list:", numbers)
print("Updated list:", result)       

# list insertion
#create  a list
numbers = [1,2,3,4]
#inser 12 at the begining take begining of the index 0
numbers.insert(0,12)
# insert 11 at the begining 
numbers.insert(0,11)
# insert 10 at the begining
numbers.insert(0,10)
print("new list:", numbers)

#list comprehension
# create alist of squares of numbers from 1 to 10
squares = [num**2 for num in range(1,11)]
print(squares)

# genearte a list of even numbers  from 1 to 20
even_number = [num for num in range(1,21)if num % 2 == 0]
print(even_number)

#create a list containing the length of each word
words = ["apple", "banana", "cherry","date"]
# find length of the each word
# word in words means  takes one word ata time from the words list.
lengths = [len(word) for word in words]
print(lengths)