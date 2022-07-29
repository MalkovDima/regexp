import re
import collections

def SaveFullName(list):
    n = 0
    for k in list:
        if n != 0:
            list[n][0] = k[0]+' '+k[1]+' '+k[2]
            list[n][1] = ''
            list[n][2] = ''
        n += 1

def FullNameColumbs(list):
    k = 0
    for n in list:
        if k != 0:
            list[k][1] = n[0].split()[1]
            if len(n[0].split()) != 2:
                list[k][2] = n[0].split()[2]
            list[k][0] = n[0].split()[0]
        k += 1


def units(list1, list2):
    list3 = []
    for q in range(7):
        if list1[q] != '':
            list3.append(list1[q])
        else:
            list3.append(list2[q])

    return list3

def search_double(list):

    for k in list:
        end = True
        searchlist = []
        searchlist.append(k[0])
        searchlist.append(k[1])
        for item in list:
            if item[0] == searchlist[0] and item[1] == searchlist[1] and collections.Counter(item) != collections.Counter(k) and end:
                list.append(units(item, k))
                list.remove(k)
                list.remove(item)
                end = False

def telnote(list):
    pattern = r'(\+7|8)?(-|\s)*\(*(\d{3})\)*(-|\s)*(\d{3})-*(\d{2})-*(\d{2})\s*\(*(\w+\.)*\s*(\d+)*\)*'
    n = 0
    for t in list:
        res = re.sub(pattern, r'+7(\3)\5-\6-\7 \8\9', t[5])
        if res[-1] == ' ':
            list[n][5] = res[:-1]
        else:
            list[n][5] = res
        n += 1