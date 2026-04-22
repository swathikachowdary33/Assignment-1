data=[10,20,30,40,50,20,30,60,70,80,90]
#append () to add [100,110]

data.append([100,110])
print(data)

#extend() to add 120,130

data.extend([120])    # adding 120
data.extend([130])    #adding 130
print(data)

#insert 25 at index 2 using insert()

data.insert(2,25)     # inserting 20 at index 2
print(data)

# removing the  first occurance of 20

data.remove(20)      #removing 20
print(data)

#removing last element using pop and store it

last_element=data.pop()     #removes last element and stores it
print("Removed element:",last_element)
print("Updated list:",data)

# count how many times 30 appears using count()

print(data.count(30))   #counts hte number 30

#index of first 40 using index

print(data.index(40))  # knows the index value of 40

# Reversing the list

data.reverse()   #this reverse the list 
print(data)

#sorting only top-level elements using sort 

data=[10,20,30,40,50,20,30,60,70,80,90]
data.sort()
print(data)