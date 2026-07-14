
students = {}
def add_student(roll, name, marks):
    students[roll] = [name, marks]
    return "Added successfully!"
def display_students():
    if not students:
        return "No student records found."
    for roll in students:
        print(f"Roll: {roll} | Name: {students[roll][0]} | Marks: {students[roll][1]}")
    return "--- End of List ---"
def search_student(roll):
    if roll in students:
        return f"Found -> Name: {students[roll][0]}, Marks: {students[roll][1]}"
    return "Not found."
def update_marks(roll, new_marks):
    if roll in students:
        students[roll][1] = new_marks
        return "Updated successfully!"
    return "Not found."
def delete_student(roll):
    if roll in students:
        del students[roll]
        return "Deleted successfully!"
    return "Not found."
def get_topper():
    if not students:
        return "No students in the system."  
    topper_roll = ""
    max_marks = -1
    for roll in students:
        if students[roll][1] > max_marks:
            max_marks = students[roll][1]
            topper_roll = roll
    return f"Topper is {students[topper_roll][0]} with {max_marks} marks!"
def get_average():
    if not students:
        return "Average Marks: 0 (No students)"
    total = 0
    for roll in students:
        total += students[roll][1]
    return f"Average Marks: {total / len(students)}"
def get_count():
    return f"Total Students: {len(students)}"
while True:
    print("\n*** STUDENT SYSTEM ***")
    print("1. Add   2. Display   3. Search   4. Update   5. Delete")
    print("6. Topper   7. Average   8. Count   9. Exit")
    choice = int(input("\nEnter choice (1-9): "))
    if choice == 9:
        print("Goodbye!")
        break
    elif choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        print(add_student(roll, name, marks))
    elif choice == 2:
        print(display_students())
    elif choice == 3:
        roll = input("Enter Roll No to search: ")
        print(search_student(roll))
    elif choice == 4:
        roll = input("Enter Roll No to update: ")
        new_marks = float(input("Enter new marks: "))
        print(update_marks(roll, new_marks))
    elif choice == 5:
        roll = input("Enter Roll No to delete: ")
        print(delete_student(roll))
    elif choice == 6:
        print(get_topper())  
    elif choice == 7:
        print(get_average()) 
    elif choice == 8:
        print(get_count())     
    else:
        print("Invalid choice! Please try again.")
