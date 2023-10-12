
for i in range(1, 3):
    filename = f"file{i}.txt"
    with (open(filename, "w") as file):
        course1, course2, course3, course4, course5 = (
            input("Enter course grades: ").split())
        L = [course1, course2, course3, course4, course5]
        convL = list(map(int, L))
        sumGrades = 0
        for x in range(len(convL)):
            sumGrades += convL[x]
            Average = sumGrades / 5
        file.write(
            f"course1: {course1}\ncourse2: {course2}\ncourse2: {course3}\n"
            f"course2: {course4}\ncourse2: {course5}\ntotal average: {Average}"
        )
