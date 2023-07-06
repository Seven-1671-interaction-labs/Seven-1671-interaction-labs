def get_valid_mark():
    while True:
        try:
            mark=float(input("Please enter the student's midterm exam mark (0-100): "))
            if 0<=mark<=100:
                return mark
            else:
                print('Please enter a valid exam mark (0-100)')
        except ValueError:
            print('Please enter a valid exam mark (0-100)')
def get_valid_markk():
    while True:
        try:
            markk=float(input("Please enter the student's final exam mark (0-100): "))
            if 0<=markk<=100:
                return markk
            else:
                print('Please enter a valid exam mark (0-100)')
        except ValueError:
            print('Please enter a valid exam mark (0-100)')
def calculate_total_score(midterm_mark,final_mark):
    midterm_weight=0.4
    final_weight=0.6
    return midterm_mark*midterm_weight+final_mark*final_weight
def calculate_grade(total_score):
    if total_score>=80:
        return 'A'
    elif 70<=total_score<80:
        return 'B'
    elif 60<=total_score<70:
        return 'C'
    elif 50<=total_score<60:
        return 'D'
    else:
        return 'F'
def main():
    student_id=input('Please enter a student ID: ')
    while True:
        midterm_mark=get_valid_mark()
        final_mark=get_valid_markk()
        total_score=calculate_total_score(midterm_mark,final_mark)
        grade=calculate_grade(total_score)
        print(f'{student_id} has total mark as {total_score:.2f} and grade as {grade}')
        break
if __name__=='__main__':
    main()