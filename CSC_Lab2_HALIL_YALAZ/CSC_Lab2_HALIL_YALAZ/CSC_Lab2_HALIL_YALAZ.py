import numpy

# the semi - annual sales data by region and district
# January - June
regA_dist1 = [3.2, 4.3, 5.1, 4.7, 3.8, 6.9]
regA_dist2 = [1.7, 2.4, 2.4, 6.1, 4.3, 5.7]
regA_dist3 = [3.3, 5.0, 4.1, 3.4, 5.1, 4.1]

regB_dist1 = [1.8, 5.8, 2.6, 1.8, 4.3, 2.6]
regB_dist2 = [6.2, 6.0, 5.3, 6.2, 6.0, 5.3]
regB_dist3 = [5.1, 3.9, 2.4, 5.1, 3.9, 4.4]

# creating the lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
months += ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print ("the calendar year")
print (months)
print ("")
regions = ["Region A", "Region B"]
print ("the designated regions")
print (regions)
print ("")
districts = ["District 1", "District 2", "District 3"] 
print ("the defined districts")
print (districts)
print ("")
qrts = ["first", "second", "third", "fourth"]

# [ first quarter sales summary ]

# first quarter sales for Region A, District 1
sumFirstA1 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[0], "quarter sales")
msgPart = regions[0] + " , " + districts[0] + " "
print ("(", msgPart, ")")

for index in range(n) :
    sumFirstA1 += regA_dist1[index]  

print ("first quarter sales: $%0.2f" % sumFirstA1)
print ("\n")

# first quarter sales for Region A, District 2
sumFirstA2 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[0], "quarter sales")
msgPart = regions[0] + " , " + districts[1] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumFirstA2 += regA_dist2[index]  

print ("first quarter sales: $%0.2f" % sumFirstA2, "\n")
 
# first quarter sales for Region A, District 3
sumFirstA3 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[0], "quarter sales")
msgPart = regions[0] + " , " + districts[2] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumFirstA3 += regA_dist3[index]  

print ("first quarter sales: $%0.2f" % sumFirstA3 ,"\n")


# first quarter sales for Region B, District 1
sumFirstB1 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[0], "quarter sales")
msgPart = regions[1] + " , " + districts[0] + " "
print ("(", msgPart, ")")

for index in range(n) :
    sumFirstB1 += regB_dist1[index]  

print ("first quarter sales: $%0.2f" % sumFirstB1)
print ("\n")

# first quarter sales for Region B, District 2
sumFirstB2 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[0], "quarter sales")
msgPart = regions[1] + " , " + districts[1] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumFirstB2 += regB_dist2[index]  

print ("first quarter sales: $%0.2f" % sumFirstB2, "\n")

# first quarter sales for Region B, District 3
sumFirstB3 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[0], "quarter sales")
msgPart = regions[1] + " , " + districts[2] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumFirstB3 += regB_dist3[index]  

print ("first quarter sales: $%0.2f" % sumFirstB3 ,"\n")


# [ second quarter sales summary ]

# second quarter sales for Region A, District 1
sumSecondA1 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[1], "quarter sales")
msgPart = regions[0] + " , " + districts[0] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumSecondA1 += regA_dist1[index]  

print ("second quarter sales: $%0.2f" % sumSecondA1, "\n")

# second quarter sales for Region A, District 2
sumSecondA2 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[1], "quarter sales")
msgPart = regions[0] + " , " + districts[1] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumSecondA2 += regA_dist2[index]  

print ("second quarter sales: $%0.2f" % sumSecondA2, "\n")

# second quarter sales for Region A, District 3

sumSecondA3 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[1], "quarter sales")
msgPart = regions[0] + " , " + districts[2] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumSecondA3 += regA_dist3[index]  

print ("second quarter sales: $%0.2f" % sumSecondA3 ,"\n")

# second quarter sales for Region B, District 1
sumSecondB1 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[1], "quarter sales")
msgPart = regions[1] + " , " + districts[0] + " "
print ("(", msgPart, ")")

for index in range(n) :
    sumSecondB1 += regB_dist1[index]  

print ("second quarter sales: $%0.2f" % sumSecondB1)
print ("\n")

# second quarter sales for Region B, District 2
sumSecondB2 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[1], "quarter sales")
msgPart = regions[1] + " , " + districts[1] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumSecondB2 += regB_dist2[index]  

print ("second quarter sales: $%0.2f" % sumSecondB2, "\n")

# second quarter sales for Region B, District 3
sumSecondB3 = 0
n = len(months) - 9
msg = ""
print ("")
print ("computing ...", qrts[1], "quarter sales")
msgPart = regions[1] + " , " + districts[2] + " "
print ("(", msgPart, ")")

for index in range(n) :
	sumSecondB3 += regB_dist3[index]  

print ("second quarter sales: $%0.2f" % sumSecondB3 ,"\n")

		
# [ semi - annual sales summary ]

# semi - annual sales for Region A

RegionA = [] #create empty list
#populate list, index by index
RegionA.append(sumFirstA1)
RegionA.append(sumFirstA2)
RegionA.append(sumFirstA3)
RegionA.append(sumSecondA1)
RegionA.append(sumSecondA2)
RegionA.append(sumSecondA3)

sumRegionA = 0
n = len(months) - 9
msg = ""
print("")
print("computing ...", qrts[0], qrts[1], "quarter sales")
msgPart = regions[0] + " , " + districts[0], districts[1], districts[2] + " "
print("(", msgPart, ")")
for index in range(len(RegionA)):
    sumRegionA += RegionA[index]
print("semi-annual sales for Region A: $%0.2f" % sumRegionA, "\n")

# semi - annual sales for Region B

RegionB = [] #create empty list
#populate list, index by index
RegionB.append(sumFirstB1)
RegionB.append(sumFirstB2)
RegionB.append(sumFirstB3)
RegionB.append(sumSecondB1)
RegionB.append(sumSecondB2)
RegionB.append(sumSecondB3)

sumRegionB = 0
n = len(months) - 9
msg = ""
print("")
print("computing ...", qrts[0], qrts[1], "quarter sales")
msgPart = regions[1] + " , " + districts[0], districts[1], districts[2] + " "
print("(", msgPart, ")")
for index in range(len(RegionB)):
    sumRegionB += RegionB[index]
print("semi-annual sales for Region B: $%0.2f" % sumRegionB, "\n")

#Layering techniques

RegionA = (ChicagoNorth)
RegionB = (ChicagoNorthwest)

ChicagoNorth = ()

AlbanyPark = (regions[0] + district[0])
IrvingPark = (regions[0] + districts[1])
Ravenswood = (regions[0] + districts[2])

EdisonPark = (regions[1] + districts[0])
JeffersonPark = (regions[1] + districts[1]) 
NorwoodPark = (regions[1] + regions[2])

ChicagoNorth = 0
ChicagoNorthwest = 0
n = len(months) - 9
msg = ""
print("")
print("computing ...", qrts[0], qrts[1], "quarter sales")
msgPart = regions[0] + regions[1] + " , " + districts[0], districts[1], districts[2] + " "
print("(", msgPart, ")")

for index in range(len(RegionA) + len(RegionB)):
    sumRegionA = RegionA+RegionB[index]

print ("ratio of ChicagoNorth and Chicago Northwest: $%0.2f" )