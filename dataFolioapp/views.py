from django.shortcuts import render
from .models import Projects, Contact

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()

        print('Message received:')

    print('Fetching projects.......')
    projects = Projects.objects.all()

    
    return render(request, 'index.html', {'projects': projects})