from math import sqrt

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(scores, average):
    variance = 0
    for each in scores:
        variance += ((average - each) ** 2)
    a = (variance / len(scores))
    return a

def grades_std_deviation(variance):
    var = grades_variance(grades, grades_average(grades))
    std_dev = sqrt(var)
    return std_dev

print grades_std_deviation(grades_variance(grades, grades_average(grades)))    
