# Define a list of items to search from
items = ["Python", "AI", "Data Science", "ML"]

# Sort the list alphabetically (required for binary search to work correctly)
items.sort()
print("Sorted items:", items)

# Take input from the user for the item to search
search_item = input("Enter the item you want to search: ")

# Initialize binary search pointers
left = 0                   # Start of the list
right = len(items) - 1     # End of the list
found = False              # Flag to track if item is found

# Start binary search loop
while left <= right:
    middle = (left + right) // 2  # Find the middle index
    print(middle)                 # Optional: show current middle index
    
    if items[middle] == search_item:
        # Item found at middle index
        print(f"Item '{search_item}' found at index {middle}")
        found = True
        break
    elif search_item < items[middle]:
        # Search item is before middle, search left half
        right = middle - 1
    else:
        # Search item is after middle, search right half
        left = middle + 1

# If loop ends and item was not found
if not found:
    print(f"Item '{search_item}' not found in the list")
