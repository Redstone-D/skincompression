from django.http import FileResponse
from django.shortcuts import render 
from . import fop 

# Create your views here.

def index(request): 
    if (request.method == "POST"): 
        file_list = request.FILES.getlist("Upload") 
        sl = fop.start(file_list)   
        file = fop.topkg(sl) 
        return FileResponse(file, content_type='application/zip') 
    return render(request, "v2/index.html") 
