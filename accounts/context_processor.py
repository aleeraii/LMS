from student.models import StudentModel


def userContext(request):
    school = ''
    roles = []
    kwargs = {}
    if request.user.is_active:
        if request.user.user_role == 'Student':
            if hasattr(request.user, "studentmodel"):
                school = request.user.studentmodel.school
                roles = school.student_function.all()
                roles = [role.role for role in roles]
        if request.user.user_role == 'Parent':
            if hasattr(request.user, 'parentmodel'):
                student = StudentModel.objects.get(
                    parent=request.user.parentmodel)
                school = student.school
                roles = school.parent_function.all()
                roles = [role.role for role in roles]
        kwargs = {
            'school': school,
            'roles': roles,
        }
    return kwargs
