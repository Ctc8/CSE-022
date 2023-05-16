from lab7 import *

def unit_tests():
    # 1
    assert heading("Heading Test") == '--------------------------------- Heading Test ---------------------------------'
    # 2
    fines = [['Jim', 100], ['Jeff', 75], ['Jane', 80], ['Juan', 110], ['Jim', 20]]
    assert summarizeFines(fines) == [['Jim', 120], ['Jeff', 75], ['Jane', 80], ['Juan', 110]]

    # 3
    assert findHighestDebtor(fines) == 'Jim'

    # 4
    weights = [('Alice', 100), ('Bob', 233), ('Cecilia', 120), ('David', 130), ('Elizabeth', 95), ('Frank', 180)]
    assert optimizeContainer(300, weights) == ('Cecilia', 'Frank')

    # 5
    newGrades = dropLowestGrade("grades.txt")
    assert newGrades == [('Alice', [54, 61]), ('Bob', [54, 53]), ('Cecilia', [85, 91]), ('David', [64, 67]), ('Elizabeth', [87, 98]), ('Frank', [55, 43])]

    # 6 
    averageGrade(newGrades)
    assert averageGrade(newGrades) == [('Alice', 57.5), ('Bob', 53.5), ('Cecilia', 88.0), ('David', 65.5), ('Elizabeth', 92.5), ('Frank', 49.0)]


if __name__ == "__main__":
    unit_tests()
