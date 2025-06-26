from django.shortcuts import render
from django.http import FileResponse
from django.utils.timezone import now
from .models import DownloadLog

def download_cv(request):
    ip = request.META.get('REMOTE_ADDR')
    agent = request.META.get('HTTP_USER_AGENT', '')
    DownloadLog.objects.create(ip_address=ip, user_agent=agent)

    file_path = 'media/TimothyMaina_CV.pdf'  # Ensure this path exists
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='TimothyMaina_CV.pdf')

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')
