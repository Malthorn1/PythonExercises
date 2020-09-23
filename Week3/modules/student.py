import random

class Student (): 
    def __init__ (self,studentID,  name, gender,  dataSheet, image_url): 
        self.studentID = studentID
        self.name = name 
        self.gender = gender
        self.dataSheet = dataSheet
        self.image_url = image_url

    def averageGrade(self): 
        grades =  dataSheet.getGrades_as_list(self.dataSheet)
        average = sum(grades) /len(grades)

        return average
        



class dataSheet (): 
    def __init__ (self, courses=[] ): 
        self.courses = courses    
    

    def getGrades_as_list (self): 
        listOfGrades = []
        for course in self.courses:
            listOfGrades.append(course.grade) 
        return listOfGrades




class courses () : 
    def __init__ (self, name, classroom, teacher, ECTS, grade): 
        self.name = name 
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade



c1 = courses ("English", "305", "Bente", 10, 7)
c2 = courses ("Danish", "306", "Anne", 10, 4)
c3 = courses ("Sports", "0", "Claus", 15, 10)

dataSheet1  =  [c1,c2,c3]

d1 = dataSheet (dataSheet1)


s1 = Student (2, "Mikkel", "Male", d1, "img url") 


print(Student.averageGrade(s1))




## OPGAVE  7 
def randomStudentToCSV  () :
    names = [ "Pelle", "Aske", "Rasmus", "Mads", "julie", "Sofie"]
    gender = ["Male", "Female"]
    
    c1 = courses ("English", "305", "Bente", 10, 7)
    c2 = courses ("Danish", "306", "Anne", 10, 4)
    c3 = courses ("Sports", "0", "Claus", 15, 10)
    dataSheet1  =  [c1,c2,c3]

    
    grade = [-3, 0, 2, 4,7,10,12]
    studentID = 0
    
    Numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for n in Numbers:
        randomName = random.choice(names)
        randomGender = random.choice(gender)
        randomClass = random.choice(dataSheet1)
        randomgrade = random.choice(grade)
        

        
        s2 = Student (studentID, randomName, randomGender, randomClass, "img url") 
        studentID = studentID+1
        print(s2.name)
        print(s2.studentID)
        print(s2.dataSheet.name)
        listOfStudents.append(s2)


    return listOfStudents

listOfStudents = []
listOfStudents= randomStudentToCSV()

 
import csv
with open('student.csv', 'w',) as csvfile:
    fieldnames = ['stud_name', 'course_name', 'teacher', 'ects', 'classroom', 'grade', 'img_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for s in listOfStudents:
        writer.writerow({  'stud_name':  s.name, 'course_name': s.dataSheet.name, 'teacher': s.dataSheet.teacher, 'ects': s.dataSheet.ECTS, 'classroom': s.dataSheet.classroom, 'grade': s.dataSheet.grade , 'img_url': s.image_url})


def read_file_to_list(file) : 
    with open (file, newline='') as f : 
       reader = csv.reader(f)
       header_row = next(reader)
       student_list = []
       for row in reader: 
         student_list.append(row)
    return student_list

def printlist (liste):
    newlist = []
    for s in liste: 
        tempStudent = [s[0], s[6], s[5]]
        newlist.append(tempStudent)


newlistOfstudents = read_file_to_list("student.csv")
printlist(newlistOfstudents)


