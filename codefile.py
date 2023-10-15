# Get the number of rows for the triangle
num_rows = int(input("Enter the number of rows for the triangle: "))

# Initialize a counter for the rows
row = 1

# Outer loop for each row
while row <= num_rows:
    # Inner loop to print asterisks in each row
    column = 1
    while column <= row:
        print("*", end=" ")
        column += 1
    # Move to the next row
    print()  # Print a newline to start a new row
    row += 1
