import re

def load_string_from_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
        return file_content

#---------------------------PART 1 ------------------------#
def findmul(input_str):
    pattern =  r'mul\(\d{1,3}\,\d{1,3}\)'  # the regex pattern "written in another language"
    return re.findall(pattern, input_str)

def findint(input_str):
    pattern = r'\d{1,3}'
    return re.findall(pattern, input_str)

def question3_p1(mem:str):
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

#--------------------------PART 2---------------------------#
def findmul2(input_str):
    pattern = r'do\(\)|don\'t\(\)|mul\(\d{1,3}\,\d{1,3}\)'
    return re.findall(pattern, input_str)

def question3_p2(mem:str):
    sops = 0
    muls = findmul2(mem)
    enabled = True
    print(muls)
    for i in range(len(muls)):
        if muls[i] == 'do()':
            enabled = True
        elif muls[i] == 'don\'t()':
            enabled = False
        else:    
            if enabled:
                factors = findint(muls[i])
                print(factors)
                product = 1
                for j in range(len(factors)):
                    product = product*int(factors[j])
                sops += product
    return sops

#--------------------------MAIN---------------------------#
if __name__ == "__main__":
    file_name = "q3_input.txt"
    string = load_string_from_file(file_name)
    print(question3_p2(string)) # 153469856 for p1, 77055967 for p2
    # print(question3_p2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"))


    # consider re.finditer(), returns and object that enables groups