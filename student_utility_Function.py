def calculate_total(marks):
    return sum(marks)


# Function to calculate average marks
def calculate_average(marks):
    return calculate_total(marks) / len(marks)



def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def display_report(name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = assign_grade(average)

    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

def main():
    name = input("Enter student name: ")
    marks = []

    for i in range(5):
        mark = int(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    display_report(name, marks)



if __name__ == "__main__":
    main()
