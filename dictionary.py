#dictionary
# info={
#     "name":"hello",
#     "subject":["python","css"],
#     "age":35,
#     "is_adult":True
# }
# print(info)
# print(type(info))

# print(info["age"])
# info["name"]="kenisha"
# print(info)
# -------------------------------------------
# null_dict={}
# print(null_dict)
# -----------------------------------------------------------
#NESTED DICT
# student={
#     "name":"rahul",
#     "subject":{
#         "phy":97,
#         "chem":78,
#         "bio":89
#     }
# }
# print(student)
# print(student["subject"])
# -------------------------------------------------------------------
#METHODS
student={
    "name":"rahul",
    "subject":{
        "phy":97,
        "chem":78,
        "bio":89
    }
}
print(student.keys())
print(student.values())
print(len(student))
print(student.items())
print(student.get("name"))

student.update({"city":"delhi"})
print(student)
