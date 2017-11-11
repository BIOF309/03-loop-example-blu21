#Billy Lu, Loop example HW

#A for loop can used in a fluorescence assay for example to find the sample with the highest and lowest fluorescence signal. The loop can take in a list of all the fluorescence values and determine the largest and smallest values from the list.

print ("This program uses a for loop to find the highest and lowest fluorescence values from a list of fluorescence values obtained from some sort of fluorescence assay.")
#Allows users to input numbers as string types, which will then be split into a list of strings by the split method. The float function will convert the numbers to the float type.
Fval = [float (x) for x in input ('Enter your fluorescence values (separate each value by a space):' ).split()]

maxF = 0 #Set maxF as the variable representing the largest fluorescence value
minF = 9999999999 #Set minF as the variable representing the smallest fluorescence value. I made the current value an integer that is higher than any of the integers in the List.

#loop
for i in Fval:
    if i > maxF:
        maxF = i
    if i < minF:
        minF = i

print ("Your fluorescence values are ", Fval)
print ("The highest fluorence value is " + str(maxF)) #prints out highest value
print ("The lowest fluorescence value is " + str (minF)) #prints out lowest value
