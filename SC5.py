student = {
    "nama" : "tulang",
    "umur" : "bntar lagi",
    "tinggi" : "2860mdpl"
}

print(student)
student["nama"] = "pakde"
for key in student:
    print(key, student.get(key))