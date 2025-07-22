

# Take the input 
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Convert both lists to sets
school_set = set(school_friends)
college_set = set(college_friends)

# Union using | operator
all_friends = school_set | college_set
list(all_friends)
print(f"All friends :{all_friends}")

# Union using union() method
all_friends_union = school_set.union(college_set)

print(f"All friends: {list(all_friends_union)}")
