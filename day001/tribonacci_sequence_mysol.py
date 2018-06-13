def tribonacci(signature, n):
    #your code here
    if n == 0:
        return []
    
    if len(signature) != 3:
        return []
    
    #expected sequences - [0,0,1] [1,1,1] [0,1,1]
    seq = signature

    for i in range(3,n):
        tmp = seq[i-1]+seq[i-2]+seq[i-3]

        seq.append(tmp)

    return seq[0:n]

sig = [1,1,1]
res = tribonacci(sig, 1)
print(res)
