""" University Program that uses inheritance
Assigns a person to faculty or person and then puts them into a department
Program written by Gavin Birk
Completed 10/21/2024
This is one of the hardest Python programs I made in my IT 209 course
"""
class Person():
    # Class variable for number of people and the current year for faculty members tenure (2024 as of creating this program)
    personCount = 0
    currentYear = 2024
    def __init__(self, name, address, telephone, email, g_num = 0) :
        # Counts number of people in the program, it uses that value to generate a g number for every person in the program
        Person.personCount += 1
        # Declares g number as a self variable, it's always zero unless a g number is called in the global code
        self.g_num = g_num
        # Sets the g number as the number of the person current being added
        self.g_num = Person.personCount
       # Adds number of zeros to the g number based on how many people are added to the program
        if Person.personCount < 10:
            self.g_num = 'G00000' + str(self.g_num)
        elif Person.personCount < 100:
            self.g_num = 'G0000' + str(self.g_num)
        elif Person.personCount < 1000:
            self.g_num = 'G000' + str(self.g_num)
        else:
            self.g_num ='G00' + str(self.g_num)
        # Assigns variables names inside the class
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email
    # Returns printable information about the person (gnum, name, and address)
    def __str__(self):
        return "Person: " + self.g_num + " Name: " + self.name + " Address: " + self.address
    # Compares persons name to see if they are the same as another person
    def equals(self, inputPerson):
        # Gets the name from the Person class and sets it to a variable inside this method
        name = self.name
        gnumber = self.g_num
        # Gets the name from the global code and sets it to a variable inside this method
        inputName = inputPerson.name
        name = str(name)
        inputName = str(inputName)
        # Returns true or false for the equals method depending on if the names match or not
        if name == inputName and self.g_num == inputName.g_num:
            return True
        else:
            return False

# ------ Student Subclass ------
class Student(Person):
    def __init__(self, name, address, telephone, email, major, enrolled, credits, qpoints):
        super().__init__(name, address, telephone, email)
        # Sets varabiles from outside of class to instance variables 
        self.major = major
        self.enrolled = enrolled
        self.credits = credits
        self.qpoints = qpoints
    # Function to calculate the GPA of each student
    def gpa(self):
        # Gets number of credits and quality points the student already has
        qpoints = float(self.qpoints)
        credits = float(self.credits)
        # Caculates Students GPA
        try:
            studentGPA = qpoints / credits
        except ZeroDivisionError:
            # Returns 0 as the students GPA if they have zero quality points and zero credits
            studentGPA = 0.0
        # Sets students GPA to 4.00 if the caculated quality points / credits is greater than 4.0
        if studentGPA > 4.0:
            studentGPA = 4.00
            studentGPA = studentGPA
        else:
        # Returns students GPA back to the class
            return studentGPA
    # Gets students quality points and total credits along with the letter grade and number of credits from outside the class
    def addGrade(self, classgrade, classcredits):
        # Boolean value returned if the grade was accepted or not accepted
        validGrade = False
        # Recalculates students GPA if the letter grade from the global code is accepted
        if classgrade == 'A' and classcredits > 0:
            classQPoints = 4 * classcredits
            self.credits = self.credits + classcredits
            self.qpoints = self.qpoints + classQPoints
            validGrade = True
        elif classgrade == 'B' and classcredits > 0:
            classQPoints = 3 * classcredits
            self.credits = self.credits + classcredits
            self.qpoints = self.qpoints + classQPoints
            validGrade = True
        elif classgrade == 'C' and classcredits > 0:
            classQPoints = 2 * classcredits
            self.credits = self.credits + classcredits
            self.qpoints = self.qpoints + classQPoints
            validGrade = True
        elif classgrade == 'D' and classcredits > 0:
            classQPoints = 1 * classcredits
            self.credits = self.credits + classcredits
            self.qpoints = self.qpoints + classQPoints
            validGrade = True
        elif classgrade == 'F' and classcredits > 0:
            classQPoints = 0 * classcredits
            self.credits = self.credits + classcredits
            self.qpoints = self.qpoints + classQPoints
            validGrade = True
        else:
            # Returns false if the grade is an invalid letter and/or the credits for the course is less than or equal to zero
            validGrade = False
        return validGrade
    # Checks if student is actively enrolled
    def isActive(self):
        # Returns a boolean value of True or False depending on the students enrollment status
        activeStudent = False
        if self.enrolled == 'y':
            activeStudent = True
        else:
            activeStudent = False
        return activeStudent
    # Checks what class level the student is in depending on how many credits they have
    def classLevel(self):
        # Sets number of credits from Student class to variable for this method
        numOfCredits = int(self.credits)
        # Returns students class level depending how many credits were entered in self.credits
        if numOfCredits < 30:
            classLvl = 'Freshman'
        elif numOfCredits >= 30 and numOfCredits < 60:
            classLvl = 'Sophomore'
        elif numOfCredits >= 60 and numOfCredits < 90:
            classLvl = 'Junior'
        else: classLvl = 'Senior'
        # Returns the class level
        return classLvl
    # Uses equals method from super class, rather than having an equals method for students
    def equals(self, inputPerson):
        super().equals(inputPerson)
    # Added function for setting students Major
    def setMajor(newMajor, student):
        # Resets students major to the one of the department they're added to in the Department class
        student.major = newMajor
        return True
    # Returns strings for the student class along with overwriting the information from the super class
    def __str__(self):
        return "Student: " + super().__str__() + " Status: " + str(self.classLevel()) + " Major: " + self.major
    
# ------ Faculty subclass of the person super class ------
class Faculty(Person):
    def __init__(self, name, address, telephone, email, rank, active, teach_load, specialty, yearStarted):
        super().__init__(name, address, telephone, email)
        # Initalizes all variables 
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.specialty = specialty
        self.yearStarted = yearStarted
    # Overwrites super() with the information from the Faculty and adds info from Faculty
    def __str__(self):
        return "Faculty: " + super().__str__() + " Rank: " + self.rank + " Specialty: " \
               + self.specialty + " Tenure: " + str(self.tenure()) + " Years"
    # Calculates number of years faculty memeber has been active
    def tenure(self):
        # Subtracts current year by the year the person started
        yearsActive = Person.currentYear - self.yearStarted
        return yearsActive
    
    # ------ Department Subclass of Person ------
class Department(Person):
    univ_students = 0
    def __init__(self, d_code, d_name, capacity, minGPA):
        # Initalizes all variables for the department
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        # Creates average GPA variable and a list for the roster of students
        self.avgGPA = 0.0
        pRoster = []
        self.pRoster = pRoster
    # Prints department name, code, and number of students in the department
    def __str__(self):
        # Returns department name, code, and number of students as strings
        return "Department name: " + str(self.d_name) + " (" + str(self.d_code) + ") Capacity: " + str(self.capacity) \
    + " Minimum GPA: " + str(self.minGPA)        
    # Inherits initalized variables and the object created in the global code to add student if qualified
    def addStudent(self, student_object):
        # Checks to see if student is already in the roster by comparing their g number to the one inside the roster list
        for item in self.pRoster:
            if student_object.g_num == item.g_num:
                return False, 'dupe'
        # Local variable for counting number of students (just students, not faculty) that're being added to each department
        addStudent = 0
        # Only adds 1 to addStudent if and only if the type of person added to the roster is a student
        for s in (self.pRoster):
            if type(s) == Student:
                addStudent += 1
        # Adds a student if they're qualified and the capacity of the department is less than the number of students, plus the additional one being added
        if self.isQualified(student_object) == True and addStudent < self.capacity:
            # Adds student to the roster
            self.pRoster.append(student_object)
            # Calculates the average GPA For each department
            gpas = 0.0
            for item in self.pRoster:
                if isinstance(item, Student):
                    gpas += float(item.gpa())
                self.avgGPA = gpas / len(self.pRoster)
            # Adds the student to the total number of students in the university
            Department.univ_students += 1
            # Runs the set major method from the Student class
            Student.setMajor(self.d_code, student_object)
            # Sets a value of the number of students in the university to a local variable
            totalstudents = Department.univ_students
            # Indicates that student is qualified
            return True, 'added'        
        # If the department roster is greater than the capacity of the department return false
        if addStudent >= self.capacity:
            print(addStudent)
            # Prints value returned from isQualified method to explain why student isn't qualified
            return False, 'Department at capacity'
        # Runs if the student object qualifies, and there's enough room in the department
        else:
            # Pritns reason student isn't qualified
            return False, self.isQualified(student_object) 
    # Inherits initialized variables and student object, and determines if student is qualified for department (by default the method is False)
    def isQualified(self, student_object):
        # Prints student isn't active if the isActive method from the Student class returns false
        if Student.isActive(student_object) == False:
            return 'not enrolled'
        # If the students GPA (taken as a float) is less than the minimum GPA of the department it gives an explination as to why student isn't qualified
        if float(student_object.gpa()) < float(self.minGPA):
                return 'GPA too low'
        # Returns True if above critera aren't met
        else:
                return True
    # Adds faculty memebers to the pRoster if the person is a faculty member (not a student)
    def addFaculty(self, faculty_object):
        if type(faculty_object) == Faculty:
            self.pRoster.append(faculty_object)
            return True, 'added'
        else:
            return False, 'Not faculty'   
    # Displays the students and their GNumber that are in the roster along with the average GPA for that department
    # It does this by iterating through the list depending on what a user wants
    def dispRoster(self, letter = "b"):
        if str(letter) == "s":
            for i in self.pRoster:
                if isinstance(i, Student):
                    print(i)
        elif str(letter) == "f":
            for i in self.pRoster:
                if isinstance(i, Faculty):
                    print(i)
            print('\n')
        else:
            str(letter) == "b"
            for i in self.pRoster:
                print(i)

#--------------------------------------------------------------------------------
# IT209_A5_F24_testscript.py - A5 Testscript
#
# Department/Person/Faculty/Student classes
#
# Author:  Gene Shuman  10/14/2024  
#--------------------------------------------------------------------------------

        
# Global Code test script starts here ----------------------------------------        
# Copy the following code into your code file and run it to test your
# classes prior to submission.  



print('\nStart of A5 Test Script ********************************')

#====================================================================
input('\nTest1. Hit "Enter" to create 17 student, 2 Faculty objects for use in the demo ')

s1 = Student('David Miller', '321 Maple Lane, Vienna, VA',
      '571-285-4567', 'dmiller8@gmu.edu',major = 'Hist', enrolled = 'y',
      credits = 30, qpoints = 90)           
s2 = Student('Emma Maria Vicente', '53A Sautier Str, Burke, VA',
      '571-235-7911', 'emvicente@aol.com', major = 'Math',
      enrolled = 'y', credits = 90, qpoints = 315)
s3 = Student('Chris Squire', '4567 Park Lane, London, UK',
      '425-285-4567', 'csquire8@gmu.edu', major = 'Musc', enrolled = 'y',
      credits = 45, qpoints = 160)
s4 = Student('Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
      '524-485-5674', 'twilkenfeld@AU.gov', major = 'Musc', enrolled = 'y',
      credits = 75, qpoints = 250)    
s5 = Student('Larry Graham', '66 pacific Coast Hwy, Los Angeles, CA',
      '231-44-2596', 'dholland@jazz.net', major = 'CHHS', enrolled = 'y',
      credits = 105, qpoints = 320)           
s6 = Student('Dave Holland', '6 Stable Way, Leeds, UK',
      '416-223-1967', 'johnwho@apple.com', major = 'CSci', enrolled = 'y',
      credits = 15, qpoints = 35)
s7 = Student('Esperanza Spalding', '9122 King Hwy, Upper Marlboror, MD',
      '310-247-1954', 'esperanza@jazzy.org', major = 'ENGR', enrolled = 'y',  
      credits = 65, qpoints = 250)           
s8 = Student('Tim Bogert', '2713 Santa Monica Blvd, Venice, CA',
      '912-333-1968', 'vfudge@yahoo.net', major = 'Hist', enrolled = 'y',
      credits = 45, qpoints = 160)
s9 = Student('Gordon Sumner', '145 Nigel Path, Manchester, U.K.',
      '011-11-0203-2202', 'sting@police.com', major = 'Musc', enrolled = 'y',
      credits = 15, qpoints = 45)           
s10 = Student('Paul McCartney', '422 Hagis Road, Edinburgh, U.K.',
      '481-221-1970', 'paullinda@wings.org', major = 'ARTS', enrolled = 'y',
      credits = 110, qpoints = 275)
s11 = Student('Tina Weymouth', '2215 Yonge Street, Toronto, CA',
      '416-676-2983', 'esmythe12@ontario.gov', major = 'ENGR', enrolled = 'y',
      credits = 85, qpoints = 250)
s12 = Student('John McVie', '27 Casino Lane, Monte Carlo, Monaco',
      '011-56-2233-9945', 'johnmac@blues.net', major = 'Hist', enrolled = 'y',
      credits = 45, qpoints = 120)
s13 = Student('Nawt Enrolled', '13 Failed Street, Cantenroll, AZ',
      '320-445-2938', 'nenrolled@gmu.ed', major = 'Hist', enrolled = 'n',
      credits = 45, qpoints = 120)
s14 = Student('Toolow G. Peyay', '1313 LowGrade Drive, Mustwait, NE',
      '678-901-2345','Toolowgpa@gmu.edu', major = 'Undc', enrolled = 'y',
      credits = 20, qpoints = 38)
s15 = Student('Stanley Clark', '13 Main St., Blandon, PA',
              '610-926-4987', 'sclarke@verizon.net', major = 'Chem', enrolled = 'y',
              credits = 95, qpoints = 295)
s16 = Student('Geddy Lee', '251 Younge St., Toronto, Ont',
              '416-221-1131', 'glee@gmail.com', major = 'Chem',enrolled = 'y',
              credits = 58, qpoints = 143)
s17 = Student('Charles Mingus', '119 HenryFord Ave., Detriot, MI',
              '571-321-9876', 'cmingus@jazz.org', major = 'Hist', enrolled = 'y',
              credits = 91, qpoints = 340)
f1 = Faculty('Paul Shuman', '3062 Covington Street, Fairfax, VA',
             '571-235-2345', 'pshuman@gmu.edu', 'Assistant Professor', 'y',
             18, 'teaching', 2017)     
f2 = Faculty('A. Einstein', '2741 University Blvd, Priceton, NJ',
             '212-346-3456', 'aeinstein@gmu.edu', 'Professor', 'y',
             6, 'research', 1938)
print('\nList of Students anf aculty created----------------------------:\n ')
print('s1=  ',s1)
print('s2=  ',s2)
print('s3=  ',s3)
print('s4=  ',s4)      
print('s5=  ',s5)
print('s6=  ',s6)      
print('s7=  ',s7)
print('s8=  ',s8)
print('s9=  ', s9)
print('s10= ',s10)
print('s11= ',s11)
print('s12= ',s12)      
print('s13= ',s13)
print('s14= ',s14)
print('s15= ', s15)
print('s16= ', s16)
print('s17= ', s17)
print('f1=  ', f1)
print('f2=  ', f2)

#==================================================================================
input('\n\nTest2. Hit "Enter" to see the list of 4 Department objects created ')
print('\n\nDepartments established---------------------------------:')
d1 = Department('ENGR', 'Engineering', 5, 3.0)
d2 = Department('ARTS', 'Art and Architecture', 5, 2.5)
d3 = Department('CHHS', 'College of Health and Human Sevrices', 3, 2.75)
d4 = Department('Hist', 'History', 5, 2.50)

print(d1)
print(d2)
print(d3)
print(d4)

#========================================================================================
input('\n\n\nTest3. Hit "Enter" to add s1 - s5, f1, f2, f3 to ENGR Department- print student list\n')
d1.addStudent(s1)      
d1.addStudent(s2)
d1.addStudent(s3)      
d1.addStudent(s4)
d1.addStudent(s5)
d1.addFaculty(f1)
d1.addFaculty(f2)
d1.dispRoster()

#==========================================================================================
print('\n\n\nTest4. Hit "Enter" to create+add  Turing and Von Neuman to ARTS and CHHS faculty,')
input('     then display their rosters:\n')
d2.addFaculty(Faculty('Alan Turing', '6 Stable Way, Bletchly Park, U.K.',
             '9-56-4955', 'aturing@UK.gov', 'Associate Professor', 'y',
             6, 'research', 1943))
d3.addFaculty(Faculty('J. Von Neuman', '71 Kovaletch Prad, Budapest, Hungary',
             '9-56-4955', 'hvneuman@gmail.com', 'Professor', 'y',
             6, 'research', 1948))
d2.dispRoster()
d3.dispRoster()

#==========================================================================================
input('\n\n\n\nTest5. Hit "Enter" to add additional students to various departments ---------:')
a, b = d1.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d1.d_code, '.  Should fail: over capacity.  Result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nDepartment ', d1.d_name, ' student list is now: ')
d1.dispRoster()

#=========================================================================================      
input('\n\n\n\nTest6. Hit "Enter" to add two students to the ARTS Department ')
a, b = d2.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d2.d_code, '.  Should fail: low GPA. Result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d2.addStudent(s7)
print('\nAttempting to add ', s7.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
d2.dispRoster()

#========================================================================================
input('\n\n\n\nTest7. Hit "Enter" to add two students to the CHHS Department' )
a, b = d3.addStudent(s8)
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d3.addStudent(s9)
print('\nAttempting to add ', s9.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
d3.dispRoster()

#=========================================================================================
input('\n\n\n\nTest8. Hit "Enter" to try adding a student with low GPA to CHHS')
a, b = d3.addStudent(s14)
print('\nAttempting to add ', s14.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#=========================================================================================
input('\n\n\n\nTest9. Hit "Enter" to try to add a non-enrolled student to the CHHS Department')
a, b = d2.addStudent(s13)
print('\nAttempting to add ', s13.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#========================================================================================
input('\n\n\n\nTest10. Hit "Enter" to try adding a duplicate student ')
a, b = d3.addStudent(s8)
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#========================================================================================
input('\n\n\n\nTest11. Hit "Enter" to add s10 to ENGR, s11 to ARTS, s12 to CHHS.')
print('  then print all 3 department student lists')
a, b = d1.addStudent(s10)
print('\nAttempting to add ', s10.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d2.addStudent(s11)
print('\nAttempting to add ', s11.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d3.addStudent(s12)
print('\nAttempting to add ', s12.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#=========================================================================================
print('\n\n\n\nTest12. Hit "Enter" to try to add s16, ' + s16.name + ', to ' + d2.d_name)
input('    which will fail for low gpa, which is ' + str(round(s16.gpa(), 2)))
print('\nProfile of Student ' + s16.name + ': ')
print(s16)
a, b = d2.addStudent(s16)
print('\nResult of attempt to add ', s16.name, ' gpa: ', str(round(s16.gpa(),2)), ' to ', d2.d_code)
print('\tis ', a, ', with reson code: ', b)

#==========================================================================================
##print('\n\n\n\nTest13. Adding 3 credit course with grade of "A" to ' + s16.name )
##input('    which raises the GPA and also moves him up a class level' )
##s16.addGrade("A", 3)
##print('\nStudent profile is now: ', s16)
input('\n\n\n\nTest13. Adding 3 credit course with grade of "A" to ' + s16.name )
s16.addGrade("A", 3)
print('\nStudent profile is now: ', s16)
a, b = d2.addStudent(s16)
print('\nResult of second attempt to add ', s16.name, ' to ', d2.d_code)
print('\tis ', a, ', with reason code:  ', b)
print('\nNote: ', s16.name, ' is now a ', s16.classLevel(), ' with gpa ', str(s16.gpa()))

#==========================================================================================
input('\n\n\n\nTest14.  Attempt to add ' + s16.name + ' to ' + d2.d_name + ' again')
a, b = d2.addStudent(s16)
print('\nResult of second attempt to add ', s16.name, ' to ', d2.d_code)
print('\tis ', a, ', with reason code:  ', b)
print('\nNote: ', s16.name, ' is now a ', s16.classLevel(), ' with gpa ', str(round(s16.gpa(),2)))

#==========================================================================================
input('\n\n\n\nTest15. Hit "Enter" to add s15 and s17 to ARTS.')
print('\nAttempting to add ', s15.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s15)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s17.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s17)
print('\t\t\treturn values: ', a, '  reason code: ', b)



#==========================================================================================
input ('\n\n\n\nTest16.  Hit "Enter" to see the final list of students and faculty for all departments')
print('\nExpected counts: ')
print('\tENGR: 5 students, 2 faculty')
print('\tARTS: 5 students, 1 faculty')
print('\tARTS: 2 students, 1 faculty')
print('\tHist: no output - 0 students, 0 faculty\n\n')

d1.dispRoster('s')
d1.dispRoster('f')
d2.dispRoster('s')
d2.dispRoster('f')
d3.dispRoster('s')
d3.dispRoster('f')
d4.dispRoster()

print('\n\n\n***** End of A5 F24 Output **********')


