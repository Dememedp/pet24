def split_by_index(s, indexes):
    lenght = len(s) - 1
    i = 0
    j = 0
    array = list()
    newstr = ""
    l = len(indexes)
    while i < lenght:
        if j < l and i == indexes[j]:
            array.append(newstr)
            newstr = s[i]
            j += 1
        else:
            newstr += s[i]
        i += 1 
    array.append(newstr)
    return array

s = "pythoniscool,isn'tit?"
indexes = [6, 8, 12, 13, 18]
print(split_by_index(s, indexes))