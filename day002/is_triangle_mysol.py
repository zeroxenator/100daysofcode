def is_triangle(a, b, c):
    if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
        return True
    else:
        return False

res = is_triangle(1,2,2)
print(res)

res = is_triangle(7,2,2)
print(res)