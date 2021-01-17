# Example 1
thislist = ["apple", "Banana", "Cherry"]
thislist.remove("Banana")
print(thislist)  # output : ["apple", "Cherry"]

# Example 2
thislist = ["apple", "Banana", "Cherry"]
thislist.pop(1)
print(thislist)  # output : ["apple", "Cherry"]

# Example 3
thislist = ["apple", "Banana", "Cherry"]
thislist.pop()
print(thislist)  # output : ["apple", "Banana"]

# Example 4
thislist = ["apple", "Banana", "Cherry"]
del thislist[0]
print(thislist)  # output : ["apple", "Cherry"]

# Example 5
thislist = ["apple", "Banana", "Cherry"]
thislist.clear()
print(thislist)  # output : []
