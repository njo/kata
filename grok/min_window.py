def min_window(str1, str2):
    l = r = i = 0
    ret = ""
    while l < len(str1) - len(str2):
        if str1[l] != str2[i]:
            l += 1
            continue
        r = l + 1
        i = 1
        while r < len(str1):
            if str1[r] != str2[i]:
                r += 1
                continue
            # Letters match
            if i != len(str2) - 1:
                i += 1
                r += 1
                continue
            # Finished matching string
            if ret == "" or len(ret) > (r - l) + 1:
                ret = str1[l:r+1]
            break
        l += 1
        i = 0

        
    return ret


print(min_window("abcdebdde","bde"))
print(min_window("fgrqsqsnodwmxzkzxwqegkndaa","kzed"))
print(min_window("michmznaitnjdnjkdsnmichmznait","michmznait"))