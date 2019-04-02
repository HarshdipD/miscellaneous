def fun(str1):
    str1 = [a for a in str1]
    flag,str2 = 0, ''

    for a in range(len(str1)):
        if str1[a] == "[": flag = 1
        elif str1[a] == "]": flag = 0
        if flag == 0 and str1[a] != "]":
            str2+=str1[a]
    return "".join(str2.split())
        
s1 = "S[he] be[lie]ve[d]"
ans = fun(s1)
print(ans)
