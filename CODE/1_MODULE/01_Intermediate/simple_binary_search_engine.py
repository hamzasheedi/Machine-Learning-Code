# -------------------------------
# Simple Search Engine Using Binary Search
# -------------------------------

# Step 1: Define a list of items (could be book titles, names, etc.)
items = ["Python", "AI", "Data Science", "ML"]

# Step 2: Sort the list alphabetically
# Binary search requires a sorted list to work correctly
items.sort()

# Print the sorted list (optional, for user reference)
print("Sorted items:", items)

# Step 3: Take search input from the user
search_item = input("Enter the item you want to search: ")

# Step 4: Initialize left and right pointers for binary search
left = 0                     # Start of the list
right = len(items) - 1       # End of the list

# Step 5: Flag to track if item is found
found = False

# Step 6: Start the binary search loop
# Loop continues as long as the search range is valid
# i.e., left index <= right index
while left <= right:
    
    # Find the middle index
    # Integer division is important to get a valid list index
    middle = (left + right) // 2
    
    # Compare middle element with the search item
    if items[middle] == search_item:
        # Item found
        print(f"Item '{search_item}' found at index {middle}")
        found = True
        break  # Exit the loop as we found the item
    
    elif search_item < items[middle]:
        # If search item comes BEFORE middle element
        # Update the right pointer to search the left half
        right = middle - 1
    
    else:
        # If search item comes AFTER middle element
        # Update the left pointer to search the right half
        left = middle + 1

# Step 7: If loop ends and item was not found
if not found:
    print(f"Item '{search_item}' not found in the list")
