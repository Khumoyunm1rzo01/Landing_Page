from tokenize import Name
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
import requests
def Index(request):
    title = Title.objects.last()
    me = Me.objects.last
    team = Team.objects.last()
    about = About.objects.last()
    design = Design.objects.last()
    project = Project.objects.last()
    video = YoutubeVideo.objects.last()
    context = {
        'me': me,
        'about': about,
        'design': design, 
        'title': title,
        'video': video,
        'project': project, 
        'team': team
    }
    return render(request, 'index.html', context)

def AddContact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
        ids = Telegram_ids.objects.all()
        token = "5115038547:AAFxqKcAqH_4LraxoO7KyN8vFLRpjyG2VpU"
        for id in ids:
            text = 'Yangi obuna: \n\nMijoz: ' + name + '\nEmail: ' + email + '\nPhone: ' + phone + '\nSubject: ' + subject + '\nMessage: ' + message
            url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
            requests.get(url + str(id.ids) + '&text=' + text)
    return redirect('index')
