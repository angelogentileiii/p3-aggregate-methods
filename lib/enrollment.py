from datetime import datetime
class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")
    
    # we've already created a list for each enrollment, by returning that list's length, 
    # we effectively collect the aggregated total of the courses enrolled for that student
    def course_count(self):
        return len(self._enrollments)

    def get_enrollments(self):
        return self._enrollments.copy()
    
    def aggregate_average_grade(self):
        # assuming the grades are already in an attribute and the attribute is stored in a dictionary
        # the kye is the enrollment and the value is the grade
            # ALSO assumes the grades are stored in a protected attribute called _grades
            
        total_grades = sum(self._grades.values()) # the values method is built-in and pulls out the values of a dictionary
        num_courses = len(self._grades)
        average_grade = total_grades / num_courses

        return average_grade

class Course:
    def __init__(self, title):

        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date
    

    # this creates an empty dictionary when called
    # it then iterates through all of the enrollments to check the enrollment date
    # if a date matches, it increments the count of the date and puts it into a key/value
        # pair for the dictionary created in the line with comment below
    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1 # check the data key for each date of enrollment, if it matches, increase by one
        return enrollment_count
