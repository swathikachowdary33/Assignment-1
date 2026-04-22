t = (10, 20, 30, 40, 50, 20, 60)

#count occurance of 20 
t.count(20)   #counts how many times 20 occurs
print(t)

#find index 40 using index
t.index(40)
print(t)

# covert tuple to list and append 70 then convert back

lst=list(t)    #converts tuple to list
lst.append(70)   # appends 70
t=tuple(lst)    #convert back to tuple again
print(t)

# Slice from index 2 to 5

result = t[2:6]
print(result)

# Concatenate another tuple

t = t + (80, 90)
print(t)

# Repeat tuple 2 times

t = t * 2
print(t)

# Check if 50 exists

if 50 in t:
    print("50 exists in the tuple")
else:
    print("50 does not exist")
    
# Unpack into variables

a, b, c = t
print(a)
print(b)
print(c)

#Try modifying element 

t = (10, 20, 30, 40)
lst = list(t)
lst[1] = 99
t = tuple(lst)
print(t)
