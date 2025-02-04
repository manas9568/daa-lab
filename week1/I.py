def search(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return "present"
    return "not present"


key = int(input("Enter key to find: "))
n = int(input("Enter the size of array: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

print(search(arr, key))
