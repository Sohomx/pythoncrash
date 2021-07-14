# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits2))

# A set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)
