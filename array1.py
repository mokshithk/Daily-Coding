arr = list(map(int, input("Enter array elements: ").split()))

sum = 0

for i in arr:
    sum += i

average = sum / len(arr)

print("Sum:", sum)
print("Average:", average)