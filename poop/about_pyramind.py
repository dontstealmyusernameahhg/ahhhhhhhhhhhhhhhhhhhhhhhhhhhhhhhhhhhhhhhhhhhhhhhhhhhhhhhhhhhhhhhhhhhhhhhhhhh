print("floyd's pyramid pattern of stars")
n = int(input("Enter the number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range (1, i+ 1):
        print(num, end=" ")
        num = num + 1
    print()
# This code prints a pyramid pattern of numbers, starting from 1 and incrementing for each position in the pyramid. # The outer loop iterates through each row, while the inner loop prints the numbers in that row.
# The pattern will look like this for n = 5: