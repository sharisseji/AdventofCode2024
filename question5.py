def load_matrices_from_file(filename):
    rules = []
    updates = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            elif "|" in line:
                # parts = line.split()
                rules.append(list(map(int, line.split("|"))))
            elif "," in line:
                updates.append(list(map(int, line.split(","))))

    return rules, updates

def check_update(rules, update):
    passed = True
    for i in range(len(rules)): # goes through each rule
        firstfound = False
        firstpos = 0
        for j in range(len(update)): # goes through the update to check if it follows rule[i]
            if rules[i][0] == update[j]: # looks for first num
                firstfound = True
                firstpos = j
        if firstfound == True:
            for j in range(len(update)): # goes through update to check if it 
                if rules[i][1] == update[j]:
                    if (j < firstpos):
                        # print("incorrect, broke rule "+ str(i) +": "+ str(rules[i][0])+"|"+str(rules[i][1]))
                        passed = False
                    # else:
                        # print("passed rule "+ str(i) +": "+ str(rules[i][0])+"|"+str(rules[i][1]))
    if passed == True:
        mid_index = len(update)//2
        return update[mid_index]
    return 0

def question5(rules, updates):
    """takes the rules as a list of lists"""
    middles = 0
    for i in range(len(updates)): # goes through each update
        # print("UPDATE NUMBER " + str(i)+ "---------")
        # print("")
        # print(check_update(rules, updates[i]))
        middles += check_update(rules, updates[i])
      
    return middles
    

if __name__ == "__main__":
    filename = "q5_input.txt"
    rules, updates = load_matrices_from_file(filename)

    # # Example
    # rules = [[47,53], [97,13], [97,61], [97,47], [75,29], [61,13], [75,53], [29,13], [97,29], [53,29], [61,53], [97,53], [61,29], [47,13], [75,47], [97,75], [47,61], [75,61], [47,29], [75,13], [53,13]]
    # updates = [[75,47,61,53,29], [97,61,53,29,13], [75,29,13], [75,97,47,61,53], [61,13,29], [97,13,75,29,47]]
    print(question5(rules, updates))