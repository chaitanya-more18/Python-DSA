# #create a dictionary with students marks
# students={
#     101: {"Name": "Aditi", "Scores": [78, 85, 90]},
#     102: {"Name": "Karan", "Scores": [70, 65, 80]},
#     103: {"Name": "Priya", "Scores": [55, 82, 80]},
#     104: {"Name": "Amol", "Scores": [67, 85, 60]},
#     105: {"Name": "Ramesh", "Scores": [36, 45, 58]},
# }

# #calculate avg score and flag pass/fail
# for sid, details in students.items():
#     avg = sum(details["Scores"]) / len(details["Scores"])
#     details["Average"] = avg
#     details["Passed"] = avg >= 50   #boolean flag

# #prnt names of passed students
# print("Students who passed: ")
# for sid, details in students.items():
#     if details["Passed"]:
#         print(details["Name"])


