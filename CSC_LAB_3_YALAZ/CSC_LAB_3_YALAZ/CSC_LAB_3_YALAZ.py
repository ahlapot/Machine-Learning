
import numpy as np
import random as rn

# declare and initialize a single dimensional list
n = 5
L1 = [0 for index in range(n)]
print ("list elements:", L1)
print ("the first element in the list", L1[0])
print ("")
# declare and initialize a columnar list
x, y, values = 1, 2, 3
L1 = [[values] * x for iindex in range(y)]
print ("list elements:", L1)
print ("the second row element in the list", L1[1][0])

# list operations

L2 = []
letter = "a"
for index in range(5) :
    # append some list elements
    L2.append(letter)
    letter += "b"
print ("list elements:", L2)
# remove a list element
L2.remove("abb")
print ("list elements:", L2)
# determine the count of a particular list element
print (L2.count("abbb"))

# clear the list
L2.clear()
print ("list elements:", L2)

# applications with list

# find the sum of each row in a two - dimensional list 
my_List = [[2, 8, 12], [5, 7, 19], [50, 0, 0]]
print (my_List)
sum_List = []
for row in my_List :
	sum_List.append(sum(row))
	print(sum_List)

# Sample code

stores = ["Avenue Jewelers", "Avenue Restaurant", "Barney's Castle"]
stores += ["City Appliances", "Clancy's Clothiers",
           "Friendly Fast Food"]
stores += ["Hardware Corner", "Musical Planet", "Randolph's",
           "Sports and More"]

categories = ["Jewelry Store", "Family Restaurant", "Arcade Games"]
categories += ["Home Appliances", "Clothing", "Fast Food Restaurant"]
categories += ["Hardware and Tools", "Music and Movies", 
               "Books, Games and Gifts", "Sports Equipment"]

traffic = [101, 273, 108, 97, 76, 203, 306, 121, 83, 192]
sales = [60.2, 73.4, 12.7, 98.1, 18.7, 16.1, 30.9, 17.3, 19.4, 22.0]
proximity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chain = ["Yes", "No"]
anchor = ["Yes", "No"]
print ("[store listings]") 

for index in range(0, len(stores), 2) :
    print (stores[index].ljust(20), "\t",
           stores[index + 1].ljust(20))
print ("\n[store categories]") 

for index in range(0, len(categories), 2) :
    print (categories[index].ljust(20), "\t", 
           categories[index + 1].ljust(20))

    #updating the program

print("\n[Maximized store placement by zone and traffic foot print data]")

# allocate or map the stores according to traffic foot print data
# first store is placed
traffic = [101, 273, 108, 97, 76, 203, 306, 121, 83, 192]
maxi = traffic.index(max(traffic))
print (stores[maxi])

zones = [7, 6, 8, 4, 5, 9, 3, 10, 2, 1]
places = []
places += [stores[maxi], zones[0]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n") 

# second store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[1]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

# third store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[2]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

# forth store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[3]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

# fifth store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[4]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

# sixth store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[5]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

# seventh store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[6]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

# eighth store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[7]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

# ninth store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[8]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

#tenth store is allocated
maxi = traffic.index(max(traffic))
print (stores[maxi])

places += [stores[maxi], zones[9]]
stores.remove(stores[maxi])
traffic.remove(traffic[maxi])

# current leftover placements that need to be maximized
print("\n[after 2nd store added - Current remaining stores to be allocated]")
print(stores , "\n")

# current leftover placements that need to be maximized
print("\n[Current remaining stores to be allocated]")
print (stores)
print (places)
print (traffic,"\n")

