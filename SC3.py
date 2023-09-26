student = {
    "nama" : "sava",
    "umur" : "bntar lagi",
    "tinggi" : "7000mdpl"
}

print(student)
student.update({"hobi" : "coding"})
for key in student:
    print(key, student.get(key))