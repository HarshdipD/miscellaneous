def fun(str1, str2):
    str1 = [a for a in str1]
    str2 = [b for b in str2]

    for a in range(len(str2)):
        if str2[a] in str(str1):
            str1.remove(str2[a])
    return ''.join(str1)

s1 = "She believed"
s2 = "he lied"
ans = fun(s1.lower(), s2.lower())
print(ans)
