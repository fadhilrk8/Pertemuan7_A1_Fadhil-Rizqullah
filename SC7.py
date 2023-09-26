student = {
    "nama" : "kesav",
    "umur" : "1300SM",
    "tinggi" : "2876mdpl"
}

print(student)
student.pop("umur")

for key in student:
    print(key, student.get(key))