from django.db import models

from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='hero_images/')
    hero_image = models.ImageField(upload_to='hero_images/')
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=100, default='#')

    def __str__(self):
        return self.title

from django.db import models

class AboutMe(models.Model):
    # Overview Section
    overview_title = models.CharField(max_length=200)
    overview_text = models.TextField()

    # Education Section
    education_title = models.CharField(max_length=200)
    education_text = models.TextField()

    # Work Experience Section
    work_experience_title = models.CharField(max_length=200)
    work_experience_text = models.TextField()

    # Personal Life Section
    personal_life_title = models.CharField(max_length=200)
    personal_life_text = models.TextField()

    def __str__(self):
        return self.overview_title




class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients_logos/')
    website = models.URLField(blank=True, null=True)  # Optional link to their website

    def __str__(self):
        return self.name

class Profile(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    # Statistics
    years_of_experience = models.PositiveIntegerField()
    happy_customers = models.PositiveIntegerField()
    projects_finished = models.PositiveIntegerField()
    digital_awards = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project_image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title




class Resume(models.Model):
    title = models.CharField(max_length=100)
    cv_file = models.FileField(upload_to='cv/', null=True, blank=True)

    def __str__(self):
        return self.title

    
class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    icon_class = models.CharField(max_length=100)  # This will store the icon class (e.g., 'bi-globe')

    def __str__(self):
        return self.name
    
#  contact section:

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.BooleanField(default=False)
    branding = models.BooleanField(default=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
