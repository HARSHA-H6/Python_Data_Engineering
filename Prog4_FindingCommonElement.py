# Input
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Finding common friends using iteration
common_friends = []
for friend in school_friends:
    if friend in college_friends:
        common_friends.append(friend)

print("Common friends (Iterative method):", common_friends)

# Converting to sets
school_set = set(school_friends)
college_set = set(college_friends)

# Using & operator
common_set = school_set & college_set
print("Common friends (Set & operator):", list(common_set))


# Using set intersection method
common_set_intersection = school_set.intersection(college_set)
print("Common friends (Set intersection method):", list(common_set_intersection))
