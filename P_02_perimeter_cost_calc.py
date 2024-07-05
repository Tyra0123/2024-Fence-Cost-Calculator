# Ask the user for the width and height
# (assume they put in valid data)
width = float(input("Width: "))
length = float(input("Length: "))
cost = float(input("cost of fencing per meter: "))

# calculate the perimeter / cost of fencing
perimeter = 2 * (width + length)
price = perimeter * cost

# output the perimeter / price
print()
print(f"Perimeter: {perimeter} m")
print(f'Price: ${price:.2f}')
