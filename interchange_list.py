list=[12,35,9,56,24]
print(list)
def swaplist(newlist):
    size=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
print("after swap..")
print(swaplist(list))