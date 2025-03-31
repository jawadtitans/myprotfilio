from .models import Client
from .models import Profile
from django.contrib import admin
from .models import  AboutMe, HeroSection, Portfolio, Service,Resume,ContactMessage


admin.site.register(HeroSection)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('overview_title', 'education_title', 'work_experience_title', 'personal_life_title')
admin.site.register(Portfolio)
admin.site.register(Service)

admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Resume)
admin.site.register(ContactMessage)

