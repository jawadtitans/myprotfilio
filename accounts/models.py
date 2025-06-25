from django.db import models

# NOTE: A custom authentication backend is required to support role-based login (email for admin, username/ID for instructor/student).

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager;
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager

# UserManager handles user creation and role assignment for custom user model.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password=None, role=None):
        if not email:
            raise ValueError("User must have an email address.")
        if not username:
            raise ValueError("User must have a username.")
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            role=role  # Set role here if passed
        )
        user.set_password(password)
        # user.is_active = True  # No longer needed, default is True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            role=0  # Set role to ADMIN explicitly (if you defined ADMIN = 0)
        )
        user.is_admin = True
        # user.is_active = True  # No longer needed, default is True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    ADMIN = 0
    INSTRUCTOR = 1
    STUDENT = 2

    role_choices = (
    (ADMIN, "admin"),
    (INSTRUCTOR, "instructor"),
    (STUDENT, "student"),
)

    #  define the role choices in here:
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=10,blank=True)
    role = models.PositiveSmallIntegerField(choices=role_choices, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    # USERNAME_FIELD is set to email for admin login; custom backend will allow username-based login for instructors/students.
    USERNAME_FIELD ="email"
    REQUIRED_FIELDS  = ['username','first_name','last_name']
    def __str__(self):
        return self.email
    objects = UserManager()

    def has_perm(self,perm,obj = None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    
# userprofile extends User with additional profile information.
class userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    father_name = models.CharField(max_length=25,blank=True,null=True)
    MALE = "male"
    FEMALE = "female"
    SEX_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, blank=True, null=True)
    Uploaded_ID = models.FileField(upload_to="users/Uploaded_ID",blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)

    profilePicture = models.ImageField(upload_to="users/profile_avtar",blank=True,null=True)
    cover_photo = models.ImageField(upload_to="usrs/cover_photo",blank=True,null=True)
    address1 = models.CharField(max_length=50,blank=True,null=True)
    address2 =models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=50,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    city = models.CharField(max_length=15,blank=True,null=True)
    city_code = models.CharField(max_length=6,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
