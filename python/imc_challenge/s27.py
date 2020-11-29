# str_list = ['ftse', 'tse', 'ft', 'ts', 'se', 'ftse']
# str_list = ['xnv', 'nvda', 'dax']

import random

str_list = []
for _ in range(500):
    w1 = "".join([random.sample(["A", "B", "C", "D"], k=1)[0] for _1 in range(5)])
    str_list.append(w1)

def longest_substring_finder(string1, string2):
    ans = ""
    max_cnt = 0
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                cnt = 1
                while i + cnt < len(string1) and j + cnt < len(string2) and string1[i + cnt] == string2[j + cnt]:
                    cnt += 1

                if cnt > max_cnt:
                    max_cnt = cnt
                    ans = string1[i : i + cnt]

    return ans



res_str = str_list[0]

for i in range(1, len(str_list)):
    longest_match = longest_substring_finder(res_str, str_list[i])
    #print(res_str, str_list[i], longest_match)
    to_add = str_list[i].replace(longest_match, '')
    res_str += to_add

print(res_str)
