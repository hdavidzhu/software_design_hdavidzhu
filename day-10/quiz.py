# new_list = []
# def recursive_flatten(l):
#     if len(l) == 0:
#         return new_list
#     elif not isinstance(l[0],list):
#         print "1"
#         new_list.append(l[0]) 
#         recursive_flatten(l[1:])
#     elif len(l[1:]) == 0:

#     else:
#         print '3'
#         new_list.append(l[0][0])
#         recursive_flatten(l[0][1:])
#     return new_list

# print recursive_flatten([1,2,3,[4,5],6,7,6,23])

new_list = []
def recursive_flatten(l):
    if isinstance(l[0],int):
        new_list.append(l[0])
    elif isinstance(l[0],list):
        new_list.extend(l[0])
    
    if len(l) >= 2:
        recursive_flatten(l[1:])
    return new_list

# print recursive_flatten([1,1,2,4,[2,3,[122,4,4]],1,1,1])

print [1,2,3] + [1,2,3]
# if __name__ == "__main__":
#     print isinstance([1,2],list)