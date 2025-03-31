from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect

from django.contrib import messages


from .models import Client, ContactMessage, Resume
from .models import HeroSection, Portfolio, Service, AboutMe, Profile

def index(request):
    # Fetch data from all models
    hero_data = HeroSection.objects.first()
    about_data = AboutMe.objects.first()
    portfolio_items = Portfolio.objects.all()
    services_items = Service.objects.all()
  
    about_me_data = AboutMe.objects.first()
    profile_data = Profile.objects.first()  # Fetch Profile data
    clients = Client.objects.all()  # Fetch all clients
   
    # Combine all the data into a single context
    context = {
        'hero': hero_data,
        'about': about_data,
        'portfolio': portfolio_items,
        'services': services_items,
       
        'about_me': about_me_data,
        'profile': profile_data , # Add Profile data to context
        'clients': clients  # Add clients to context
    }

    # Render the index template with the combined context
    return render(request, 'index.html', context)

def download_cv(request):
    # Assuming you have a single resume or fetch the specific one you want
    resume = Resume.objects.first()  # Adjust if you have multiple resumes

    # Check if the resume exists and has a file
    if resume and resume.cv_file:
        # Provide the path to the file in your media directory
        resume_path = resume.cv_file.path

        # Return the file as a response to trigger the download
        response = FileResponse(open(resume_path, 'rb'), as_attachment=True, filename='CV-Download.pdf')
        return response
    else:
        return render(request, 'error.html', {'message': 'Resume not found.'})
    

def contact_view(request):
    if request.method == 'POST':
        # Get data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = 'website' in request.POST
        branding = 'branding' in request.POST
        message = request.POST.get('message')

        # Save the data into the database
        contact_message = ContactMessage(
            name=name,
            email=email,
            website=website,
            branding=branding,
            message=message
        )
        contact_message.save()

        # Redirect to a 'Thank you' page or show a success message
        return redirect('thank_you')  # Make sure to create this URL or replace it with your actual success page.

    return render(request, 'contact.html')  # 