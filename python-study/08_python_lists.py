# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

thislist =  ["Dharmendra","Amit","Sunil","Rajesh","kunal"]
print(thislist)
print(thislist[1])

thislist[1] = "Jitendra"
print(thislist)

for x in thislist:
    print(x)

if "Sunil" in thislist:
    print("Yes, 'Sunil is in this list")

print(len(thislist))

thislist.append("Anish")
print(thislist)

thislist.insert(1,"Ravi")
print(thislist)
 
thislist.remove("kunal")
print(thislist)

thislist.pop() #The pop() method removes the specified index, (or the last item if index is not specified):
print(thislist)

del thislist[0]
print(thislist)

del thislist #The del keyword can also delete the list completely:
#print(thislist)

thislist1 = ["apple", "banana", "cherry"]
print(thislist1)
thislist1.clear()
print(thislist1)

#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)