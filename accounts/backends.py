from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class RoleBasedAuthBackend(ModelBackend):
    """
    Custom authentication backend:
    - Admins login via email
    - Instructors/Students login via username/ID
    - Enforces role-based login restrictions
    """
    def authenticate(self, request, username=None, password=None, email=None, **kwargs):
        user = None
        if email:
            # Admin login via email
            try:
                user = User.objects.get(email=email)
                if user.role != User.ADMIN:
                    return None
            except User.DoesNotExist:
                return None
        elif username:
            # Instructor/Student login via username/ID
            try:
                user = User.objects.get(username=username)
                if user.role not in [User.INSTRUCTOR, User.STUDENT]:
                    return None
            except User.DoesNotExist:
                return None
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None 