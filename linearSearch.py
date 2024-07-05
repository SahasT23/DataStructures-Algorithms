def linear_search(array, target):
  for i in range(len(array)):
    if array[i] == target:
      return i
  return -1

array = [2, 8, 3, 5, 1]
target = 1
index = linear_search(array, target)
if index != -1:
  print(f"Element found at index {index}")
else:
  print("element not found")

# Time complexity is O(n) as this is a linear function
# Space complexity is O(1) as the same amount of memory to store each index of the element

  