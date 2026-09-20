arr = list(map(int, input("Enter array elements: ").split()))
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i
print("Largest element:", largest)