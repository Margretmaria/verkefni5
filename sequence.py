# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# ætla fyrst að setja inn input

# ætla svo að setja output

n = int(input("Enter the length of the sequence: ")) # Do not change this line

tala1 = 1
tala2 = 2
tala3 = 3
sum = 0

for i in range (1, n +1):
    if i == 1 or i == 2 or i == 3:
        print (i)
    else:  
        sum = tala1 + tala2 + tala3
        print(sum)
        tala1 = tala2
        tala2 = tala3
        tala3 = sum 


