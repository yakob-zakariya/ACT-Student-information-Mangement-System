from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.role == "ADMIN"
def is_department_head(user):
    return user.role == "DEPARTMENT_HEAD"
def is_student(user):
    return user.role == "STUDENT"

def is_registrar(user):
    return user.role == "REGISTRAR"

def is_teacher(user):
    return user.role == "TEACHER"

admin_required = user_passes_test(is_admin)
department_head_required = user_passes_test(is_department_head)
student_required = user_passes_test(is_student)
registrar_required = user_passes_test(is_registrar)
teacher_required = user_passes_test(is_teacher)

