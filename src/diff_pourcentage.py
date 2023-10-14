
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

min_n = min(a, b)
max_n = max(a, b)

# get the pourcentage of the diff
pourcentage = abs(max_n - min_n) / min_n * 100
print("The pourcentage of the diff is: ", pourcentage, "%")