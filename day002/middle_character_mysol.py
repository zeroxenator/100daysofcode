def get_middle(s):
    #your code here

    strLen = len(s)

    if not (0 < strLen < 1000):
        return ""
    
    div = strLen // 2

    #Even
    if strLen % 2 == 0:
        return s[div-1:div+1]
    elif strLen % 2 !=0:
        return s[div]

res = get_middle('A')
print(res)


    
