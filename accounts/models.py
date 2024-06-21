from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
import random

####### User Model and its Mangers with respective of their Role ##############

class User(AbstractUser):
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN","Admin"
        STUDENT = "STUDENT","Student"
        TEACHER = "TEACHER","Teacher"
        DEPARTMENT_HEAD = "DEPARTMENT_HEAD","Department Head"
        REGISTRAR = "REGISTRAR","Registrar"
    base_role = Role.ADMIN
    role = models.CharField(max_length=50,choices=Role.choices)
    middle_name=models.CharField(max_length=50,null=True,blank=True)
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args,**kwargs)
        return super().save(*args,**kwargs)
    
        
    class Meta:
        db_table = 'users'
        
class StudentManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role = User.Role.STUDENT)
    
    
class StudentManager2(models.Manager):
    
        def create_student_user(self, suffix):
            last_student = self.filter(role=User.Role.STUDENT).order_by('-id').first()
            if last_student:
                # Extracting the middle number from the last student's username
                last_username_parts = last_student.username.split('/')
                last_number = int(last_username_parts[1])
            else:
                last_number = 1000  # If there are no students, start from 1000
            username = f'UGR/{last_number + 1}/{suffix}'
            password = str(1234) 
            print(password)
            # Create user object
            user = self.model(username=username, role=User.Role.STUDENT)
            
            # Set and hash the password
            user.set_password(password)
            
            # Save the user object
            user.save(using=self._db)
            
            return user

   
class TeacherManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.TEACHER)
    
    
class RegistrarManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.REGISTRAR)

class DepartmentHeadManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=User.Role.DEPARTMENT_HEAD)


class TeacherUser(User):
    base_role = User.Role.TEACHER 
    teachers = TeacherManager()
    
    class Meta:
        proxy=True 
        
class StudentUser(User):
    base_role=User.Role.STUDENT 
    students = StudentManager()
    objects = StudentManager2()
    
    class Meta:
        proxy=True 


class RegistrarUser(User):
    base_role = User.Role.REGISTRAR 
    registrars = RegistrarManager()
    
    class Meta:
        proxy= True 

        
class DepartmentHeadUser(User):
    base_role = User.Role.DEPARTMENT_HEAD 
    department_heads = DepartmentHeadManager()
    
    class Meta:
        proxy=True 



# model to save all the student data

class Student(models.Model):
    student=models.OneToOneField(StudentUser,on_delete=models.CASCADE,related_name='student')
    status=models.BooleanField(default=True)
    profile_image = models.ImageField(default='profile_image/default.jpg',upload_to='profile_image',blank=True,null=True)
    department = models.ForeignKey('school.Department',on_delete=models.SET_NULL,blank=True,null=True)
    batch = models.ForeignKey('school.Batch',on_delete=models.SET_NULL,null=True,blank=True)
    section = models.ForeignKey('school.Section',on_delete=models.SET_NULL,blank=True,null=True,related_name='students')
    
# model to save all the teacher data
class Teacher(models.Model):
    teacher = models.OneToOneField(TeacherUser,on_delete=models.CASCADE,related_name='teacher')
    status = models.BooleanField(default=True)
    profile_image = models.ImageField(default='profile_image/default.jpg',upload_to='profile_image',blank=True,null=True)
    department = models.ForeignKey('school.Department',on_delete=models.SET_NULL,blank=True,null=True)
    

# model to save all the teacher data  
class DepartmentHead(models.Model):
    department_head=models.OneToOneField(DepartmentHeadUser,on_delete=models.CASCADE,related_name='department_head')
    status = models.BooleanField(default=True)
    profile_image= models.ImageField(default='profile_image/default.jpg',upload_to='profile_image',blank=True,null=True)
    department = models.ForeignKey('school.Department',on_delete=models.CASCADE)
