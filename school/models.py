from django.db import models

########   Department Model Start ############

class Department(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)

    class Meta:
        db_table='departments'
    
    def __str__(self):
        return f"{self.name} ({self.code})"

########## Department Model Ends ###########



######### Course Model Start   ##############
       
class Course(models.Model):
    name = models.CharField(max_length = 200)
    code = models.CharField(max_length=50)
    credit_hour = models.PositiveIntegerField()
    prerequisites = models.ManyToManyField('self',blank=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
     
    class Meta:
        db_table='courses'
        
    def __str__(self):
        return self.name
    
######## Course Models End #################

####### Batch Model Start ###########

class Batch(models.Model):
    name = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course,through="Batch_course")
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='batches')
    
    class Meta:
        db_table='batches'
    
    def __str__(self):
        return f" Batch of {self.name} ({self.department.code})"
 
###########   Batch Model Ends ########## 
########## Section Model Start #############

class Section(models.Model):
    name = models.CharField(max_length = 20)
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,related_name='sections')
    
    
    class Meta:
        db_table = "sections"
    
    def __str__(self):
        return f"{self.batch.department.code} {self.name} batch of ({self.batch.name})"

########## Section Model Ends #############

###### Academic Year #########

class AcademicYear(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = "academic_years"
        
    def __str__(self):
        return self.name

########## Academic Year Ends ############

######### Semester Model Start ############

class Semester(models.Model):
    name = models.CharField(max_length = 20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    AcademicYear = models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "semesters"
        
    def __str__(self):
        return self.name
    
######### Semester Model Ends ############

class Batch_course(models.Model):
    batch= models.ForeignKey(Batch,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    
    # teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return f"{self.course.name} for batch {self.batch.name} ({self.batch.department.code})"
    
    class Meta:
        db_table='batch_courses'
    

class Registration(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.StudentUser',on_delete=models.CASCADE,related_name='courses')
    teacher = models.ForeignKey('accounts.TeacherUser',on_delete=models.SET_NULL,null=True,blank=True,related_name='course_teach')
    
    def __str__(self):
        return f"{self.student.username} taking course {self.course.name}"
    
class Section_teacher(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    teacher = models.ForeignKey('accounts.TeacherUser',on_delete=models.SET_NULL,null=True,blank=True)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
        
    
    
    class Meta:
        db_table='section_teachers'
        unique_together = ('course', 'semester', 'teacher', 'section')
        
    def __str__(self):
        return f"{self.teacher.username} teaches {self.course.name} on {self.semester.name} {self.semester.AcademicYear.name}"
    
    
    

from django.core.validators import MaxValueValidator, MinValueValidator

class CourseGrades(models.Model):
    registration = models.OneToOneField('Registration', on_delete=models.CASCADE,related_name='grade')
    mid_exam_result = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    class_assessment = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    final_exam_result = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    grade = models.CharField(max_length=2)

    def calculate_grade(self):
        total_score = self.mid_exam_result + self.class_assessment + self.final_exam_result
        # Define the grade boundaries based on the total score
        if total_score >= 90:
            return 'A+'
        elif total_score >= 85 and total_score <90:
            return 'A'
        elif total_score >= 80 and total_score <85:
            return 'A-'
        elif total_score >= 75 and total_score <80:
            return 'B+'
        elif total_score >= 70 and total_score <75:
            return 'B'
        elif total_score >= 65 and total_score <70:
            return 'B-'
        elif total_score >= 60 and total_score <65:
            return 'C+'
        elif total_score >= 55 and total_score <60:
            return 'C'
        elif total_score >= 50 and total_score <55:
            return 'C-'
        elif total_score >= 45 and total_score <50:
            return 'D'
        else:
            return 'F'

    def save(self, *args, **kwargs):
        self.grade = self.calculate_grade()
        super().save(*args, **kwargs)

    
    
