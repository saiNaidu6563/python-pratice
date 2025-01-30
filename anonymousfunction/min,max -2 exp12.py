#Program for Accepting List of Values and Find Max and Min by using Anonymous Functions
# with pre-functions max() and min()
def findmax(lst):
    maxv=lst[0]
    for v in lst:
        if v>maxv:
            maxv=v
    return maxv
def findmin(lst):
    minv=lst[0]
    for v in lst:
        if v<minv:
            minv=v
    return minv
#anunymous function
max=lambda lst:findmax(lst)
min=lambda lst:findmin(lst)
#main program
print("enter a value separated by comma")
lst=[float(v) for v in input().split(",")]
maxv=max(lst)
minv=min(lst)
print(f"max value:{maxv}")
print(f"min value:{minv}")
