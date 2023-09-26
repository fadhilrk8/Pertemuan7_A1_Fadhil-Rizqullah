student = {
"nama" : "ardan",
"umur" : "530",
"tinggi" : "2km"
}

print(student)
student["hobi"] = "mancing"

for key in student:
    print(key, student.get(key))