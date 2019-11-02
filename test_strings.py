# value = "aaaabbbccccfffaaaas"
# new_value = value[-1] + value[1:len(value) - 1] + value[0]
# print(new_value)
#
# frequency_a = value.count('a') / len(value)
# print(frequency_a)
#
# pack_value = ""
# prev_c = value[0]
# count_c = 1
# for cur_c in value[1:len(value)]:
#     if cur_c == prev_c:
#         count_c += 1
#     else:
#         pack_value = pack_value + prev_c + str(count_c)
#         count_c = 1
#     prev_c = cur_c
# pack_value = pack_value + cur_c + str(count_c)
# print(pack_value)

# import re
#
# regex = "(a+)|(b+)|(c+)|(d+)|(e+)|(f+)|(g+)|(h+)|(i+)|(j+)|(k+)|(l+)|(m+)|(n+)|(o+)|(p+)|(q+)|(r+)|(s+)|(t+)|(u+)|(v+)|(w+)|(x+)|(y+)|(z+)"
#
# test_str = "aaaabbbbcccdddddeeffffffggggghhhxxxyyyyyyzzzzzzz"
# pack_str = ""
# matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)
#
# for matchNum, match in enumerate(matches, start=1):
#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
#         if match.group(groupNum) != None:
#             pack_str = pack_str + match.group(groupNum)[0] + str(len(match.group(groupNum)))
# print(pack_str)
#
value = 'aaabbccc'
value = value + '$'
start = 0
end = 0
pack_str = ""
for i in range(len(value) - 1):
    if value[i] != value[i + 1]:
        end = i + 1
        pack_str = pack_str + value[start:end][0] + str(len(value[start:end]))
        start = i + 1
print(pack_str)