import re

def findmul(input_str):
    pattern =  r'mul\(\d{1,3}\,\d{1,3}\)'  # the regex pattern "written in another language"
    return re.findall(pattern, input_str)

def findint(input_str):
    pattern = r'\d{1,3}'
    return re.findall(pattern, input_str)

def question3(mem:str):
    sops = 0
    muls = findmul(mem)
    print(muls)
    for i in range(len(muls)):
        factors = findint(muls[i])
        print(factors)
        product = 1
        for j in range(len(factors)):
            product = product*int(factors[j])
        sops += product
    return sops

print(question3('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'))

# OLD MANUAL VERSION WITHOUT REGEX (TOO LONG)

# def question3(mem:str):
#     comp = 'mul'
#     result = 0
#     for i in range(len(mem)-7): # iterating through length of string
#         # print(mem[i:i+4],end=" ")
#         # print(mem[i+5], end=" ")
#         # print(mem[i+7], end=" ")
#         # print(mem[i+4], end = " ")
#         # print(mem[i+6])
        
#         # iterate through loop, until find mul(
#         if (mem[i:i+4] == 'mul('):
#             #  and (mem[i+5] == ',') and (mem[i+7]) == ')'
#             print("found")
#             result += int(mem[i+4])*int(mem[i+6])
#         # if(is_number_regex(mem[i+4])):
#         #     if(is_number_regex(mem[i+5])):
#         #         if(is_number_regex(mem[i+6])):
#         #             if(is_number_regex(mem[i+7])):
#         #                 # break
#         #                 pass # temp

#     return result