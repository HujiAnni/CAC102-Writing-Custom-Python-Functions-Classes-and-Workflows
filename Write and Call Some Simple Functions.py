def find_min(x,y):
    if x<y:
        min_xy=x
    else:
        min_xy=y
    return min_xy


def find_max(x,y):
    if x<y:
        max_xy=y
    else:
        max_xy=x
    return max_xy

x = 3
y = 4

min_xy=find_min(x,y)
max_xy=find_max(x,y)
print(min_xy)
print(max_xy)

a = 12.3
b = 13.7

min_ab=find_min(a,b)
max_ab=find_max(a,b)
print(min_ab)
print(max_ab)

w = -3.9
z = -4.7

min_wz=find_min(w,z)
max_wz=find_max(w,z)
print(min_wz)
print(max_wz)


