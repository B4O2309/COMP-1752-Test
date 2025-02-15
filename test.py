class Student:
    def __init__(self, name='', major='', student_id=''):
        self.name = name
        self.major = major
        self.id = student_id


class FullTimeStudent(Student):
    def __init__(self, name='', major='', student_id='', joinedProject=None, researchProfile=''):
        super().__init__(name, major, student_id)
        self.joined_project = joinedProject
        self.research_profile = researchProfile


class PartTimeStudent(Student):
    count = 0

    def __init__(self, name='', major='', student_id='', minHour=0, maxHour=0):
        super().__init__(name, major, student_id)
        self.min_hour = minHour
        self.max_hour = maxHour
        PartTimeStudent.count += 1

    def count_student():
        return PartTimeStudent.count


class Lecturer:
    def __init__(self, lecturer_id='', lecturer_name='', rank='', projectLed=None, joinedProject=None, researchProfile=''):
        self.id = lecturer_id
        self.name = lecturer_name
        self.rank = rank
        self.project_led = projectLed
        self.joined_project = joinedProject if joinedProject is not None else []
        self.research_profile = researchProfile


class Project:
    def __init__(self, project_name='', budget=0.0, leader=None, members=None):
        self.name = project_name
        self.budget = budget
        self.leader = leader
        self.members = members if members is not None else []

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.lecturers = []
        self.projects = []

    def add_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < 10:
            self.lecturers.append(lecturer)

    def add_project(self, project):
        if len(self.projects) < 10:
            self.projects.append(project)