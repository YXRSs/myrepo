def build_marks_dict(input_file):
    student_to_marks = {}
    input_line = input_file.readline()
    while(not input_line.startswith("---")):
        course_to_grade = {}
        input_line = input_line.strip()
        (student, course, grade) = input_line.split(',')
        if(student in student_to_marks):
            course_to_grade = student_to_marks[student]
            course_to_grade[course] = float(grade)            
        else:
            student_to_marks[student] = course_to_grade
            course_to_grade[course] = float(grade)
        input_line = input_file.readline()
    return student_to_marks

def calculate_averages(student_to_marks):
    course_to_average = {}
    course_to_marks_list = {}
    for next_student in student_to_marks:
        course_to_grade = student_to_marks[next_student]
        for next_course in course_to_grade:
            next_grade = course_to_grade[next_course]
            if(next_course in course_to_marks_list):
                course_to_marks_list[next_course].append(next_grade)
            else:
                course_to_marks_list[next_course] = [next_grade]
    for next_course in course_to_marks_list:
        marks_list = course_to_marks_list[next_course]
        average = sum(marks_list)/len(marks_list)
        course_to_average[next_course] = average
    return course_to_average

if(__name__ == "__main__"):
    input_file = open("grades.txt")
    student_to_marks = build_marks_dict(input_file)
    course_to_average = calculate_averages(student_to_marks)
    input_file.close()
class Vehicle:
    def __init__(self,max_passengers, num_wheels, max_speed):
        self._max_passengers = max_passengers
        self._num_wheels = num_wheels
        self._max_speed = max_speed
class Car(Vehicle):
    def __init__(self,max_passengers, max_speed):
        CAR_WHEELS = 4        
        Vehicle.__init__(self,max_passengers, CAR_WHEELS, max_speed)
class SportsCar(Car):
    def __init__(self,max_passengers, num_wheels, max_speed):
        SPORTS_CAR_SEATS=2
        SPORTS_CAR_MAX_SPEED=300
        Car.__init__(self,SPORTS_CAR_SEATS,SPORTS_CAR_MAX_SPEED)
    