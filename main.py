
def add_dict1(dict1,dict2):
    ans = dict1
    for key in dict2:
        if ans.get(key) != None:
            ans[key] = dict1.get(key) + dict2.get(key)
        else:
            ans[key] = dict2.get(key)
    return ans


dict1 = {'a':10, 'b':20}
dict2 = {'b':30, 'c':40}
res = add_dict1(dict1,dict2)
print(res)