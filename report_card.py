# ===== REPORT CARD =====
# Name   : Shanti
# Marks  : [78, 85, 90, 60, 72]
# Total  : 385
# Average: 77.0
# Grade  : B
# Result : Pass
# =======================

student = {
    "name": "Shanti",
    "marks": [78, 85, 90, 60, 72],
    "total": 0,
    "average": 0,
    "grade": "",
    "result": ""
}

marks = student["marks"]
def check_grade(marks):
    total = 0
    for mark in marks:
        total = total + mark
    
    average = total / len(marks)
    student["average"] = average
    student["total"] = total

    if average>= 80:
        student["grade"]="A"
        student["result"] ="Pass"
    elif average>= 60:
        student["grade"]="B"
        student["result"] ="Pass"
    elif average>= 40:
        student["grade"]="c"
        student["result"] ="Pass"
    else:
        student["grade"]="F"
        student["result"] ="Fail"
   
check_grade(marks)  
print("===== REPORT CARD =====")
print("Name   :", student["name"])
print("Marks  :", student["marks"])
print("Total  :", student["total"])
print("Average:", student["average"])
print("Grade  :", student["grade"])
print("Result :", student["result"])
print("=======================")