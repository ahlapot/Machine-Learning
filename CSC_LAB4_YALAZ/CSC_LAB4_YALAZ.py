import numpy as np
# program to read from a file
# strName = "c:\\temp\\ratings.txt"
strName = "ratings.txt"

try :
    file = open(strName, "r")
    field1 = ""; field2 = ""; field3 = ""
    field4 = ""; field5 = ""; field6 = ""; field7 = ""
  
 #variables

    count = 0; val1 = 0; val2 = 0; val3 = 0; val4 = 0

    fieldAvg=[] #set up array to hold averages for field 2  
    fieldM=[]
    fieldF=[]
    fieldAge=[]

    for line in file :

        count += 1 # increment count

        fields = line.rstrip().split(",")
        field1 = fields[0]
        field2 = fields[1]
        field3 = fields[2]
        field4 = fields[3]
        field5 = fields[4]
        field6 = fields[5]
        field7 = fields[6]
        print (field1 + "\t" + field2 + "\t" + field3 + "\t" + 
               field4 + "\t" + field5 + "\t" + field6 + "\t" + field7)
        
        if count > 1:
            # average rating
            fieldAvg.append(float(fields[1]))
           
            # male voters vs.female voters
            if(field5 == " M"):
                val2 += 1
            if(field5 == " F"):
                val3 += 1
            # voters between 40-49
            if count > 1:
               fieldAge.append(int(fields[5]))
               age40Ct = 0
            for i in range(len(fieldAge)):
              if fieldAge[i] > 39 and fieldAge[i] < 50:
                age40Ct += 1
    
    file.close()

    print("\nStats:\nAvg rating:",np.average(fieldAvg))
    print("\nStats:\n M:",(val2+1))
    print("\nStats:\n F:",(val3+1))
    print("The total reviewers in their 40's:")
    print (age40Ct)
    #ai part1
    print("Genre (M):",((len(fieldAge))/val2+1))
    print("Genre (F):",((len(fieldAge))/val3+1))
except IOError :
    print ("file appears to not exist!")

#import os
# program to write to a file
#strName = "ratings.txt" # strName = "c:\\temp\\ratings.txt"

#try :
 #   num = int(input("how many records? "))
  #  count = 0
   # if os.path.exists(strName) :
    #    file = open(strName, "a")
     #   while (count < num) :
      #      print ("record", count + 1)
       #     for index in range(0, 7) :
        #        val = input("enter a value: ")
         #       if (index < 7 - 1) :
          #          file.write(val + ", ")
           #     else :
            #        file.write(val + "\n")
            #count = count + 1
    #else :
     #   file = open(strName, "w")
      #  field1 = "Member,"
       # field2 = "Rating,"
        #field3 = "Crew,"
        #field4 = "Date,"
        #field5 = "Gender,"
        #field6 = "Age,"
        #field7 = "Demographics"
        
        #file.write(field1)
        #file.write(field2)
        #file.write(field3)
        #file.write(field4)
        #file.write(field5)
        #file.write(field6)
        #file.write(field7 + "\n")

        #while (count < num) :
         #   print ("record", count + 1)
          #  for index in range(0, 7) :
           #     val = input("enter a value: ")
            #    if (index < 7 - 1) :
             #       file.write(val + ", ")
              #  else :
               #     file.write(val + "\n")
            #count = count + 1
            
    #file.close()
#except IOError :
 #   print ("file appears to not exist!")

