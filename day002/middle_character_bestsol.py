def get_middle1(s):
   return s[(len(s)-1)/2:len(s)/2+1]

def get_middle2(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]