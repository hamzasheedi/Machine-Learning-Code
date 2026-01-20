items = ["Python", "AI", "Data Science", "ML"]
items.sort()
print("Sorted items:", items)

search_item = input("Enter the item you want to search: ")

left = 0
right = len(items) - 1
found = False

while left <= right:
    middle = (left + right) // 2
    print(middle)
    
    if items[middle] == search_item:
        print(f"Item '{search_item}' found at index {middle}")
        found = True
        break
    elif search_item < items[middle]:
        right = middle - 1
    else:
        left = middle + 1

if not found:
    print(f"Item '{search_item}' not found in the list")
