
#1
def heading(title, max_width=80, min_padding = 4):
    dash = '-'
    space = ' '
    filler = '...'
    title_space = (max_width) - min_padding * 2 - 2
    if len(title) == 0:
        return dash * max_width
    elif len(title) <= title_space:
        dashes_left = (title_space - len(title)) // 2
        dashes_right = dashes_left + (title_space - len(title)) % 2
        return dash * (min_padding + dashes_left) + space + title + space + dash * (min_padding + dashes_right)
    else:
        title = title[:title_space - 3] + filler
        return dash * min_padding + space + title + space + dash * min_padding

#2
def summarizeFines(fines):
    dict = {}
    for name, val_owed in fines:
        if name not in dict:
            dict[name] = val_owed
        else:
            dict[name] = dict[name] + val_owed
    return [[name, val_owed] for name, val_owed in dict.items()]

#3
def findHighestDebtor(debts):
    dict = {}
    max_fine = 0 
    for name in debts:
        if name[0] not in dict:
            dict[name[0]] = name[1]
        else:
            dict[name[0]] = dict[name[0]] + name[1]
        if max_fine < dict[name[0]]:
            max_fine = dict[name[0]]

    for name in dict:
        if dict[name] == max_fine:
            return name

#4
def optimizeContainer(limit, customerLimit):
    dict = {}
    for name, lbs in customerLimit:
        if limit - lbs not in dict:
            dict[lbs] = name
        else:
            return (dict[limit - lbs], name)

#5
def dropLowestGrade(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for i in range (len(lines)):
        lines[i] = (lines[i].split(','))
    for r in lines:
        r.remove(min(r))


#6
def averageGrade(gradeList):

    for name, grades in gradeList:
        grades = [float(c) for c in grades]
        output.append( (name, sum(grades)/len(grades)) )
    return output



if __name__ == "__main__":
    print(heading("Heading Test"))
    print(heading(""))
    print(heading("1"))
    print(heading("10"))
    print(heading("101"))
    print(heading("*" * 70))
    print(heading("*" * 71))
    print(heading("*" * 69))
    print()

    print(heading("Fines Summary"))
    fines = [["Jim", 100], ["Jeff", 75], ["Jane", 80], ["Juan", 110], ["Jim", 20]]
    print(fines)
    print(summarizeFines(fines))
    print()

    print(heading("Highest Debtor"))
    print(fines)
    print(findHighestDebtor(fines))
    print()

    print(heading("Container Optimization"))
    weights = [("Alice", 100), ("Bob", 233), ("Cecilia", 120), ("David", 130), ("Elizabeth", 95), ("Frank", 180)]
    print(weights)
    print(optimizeContainer(300, weights))
    print()

    print(heading("Drop Lowest Grade"))
    newGrades = dropLowestGrade("grades.txt")

    print()

    print(heading("Average Grades"))
    averages = averageGrade(newGrades)





