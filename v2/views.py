from datetime import timedelta, timezone
import json
import random
from django.http import FileResponse, HttpResponseRedirect, JsonResponse 
from django.shortcuts import render
from django.urls import reverse 
from . import fop 
from . import models 

# Create your views here. 

num = 0 
add = 0 

def index(request): 
    num = regenerate() 
    if (request.method == "POST"): 
        file_list = request.FILES.getlist("Upload") 
        skin_list = fop.start(file_list) 
        try: 
            slm = models.SkinList.objects.get(id=num) 
        except: 
            slm = models.SkinList.objects.create(id=num) 
        slm.skin.set(skin_list) 
        slm.save() 
        return HttpResponseRedirect(reverse("process", args=(num,))) 
    return render(request, "v2/index.html") 

def process(request, rid): 
    return render(request, f"v2/process.html", { 
        "rid": rid 
    }) 

def app(request, rid): 
    num = regenerate() 
    slm = models.SkinList.objects.get(id=rid) 
    skin_list = slm.skin.all() 
    skins = [] 
    for skin in skin_list: 
        skins.append({ 
            "id": skin.id, 
            "name": skin.name, 
            "model": skin.model 
        }) 
    slm.id = num 
    slm.save() 
    return JsonResponse({ 
        "skins": skins, 
        "id": num 
    }) 

def picture(request, rid, pid): 
    return FileResponse(models.SkinList.objects.get(id=rid).skin.get(id=pid).file) 

def getcompress(request, rid): 
    file = fop.topkg(models.SkinList.objects.get(id=num).skin.all()) 
    return FileResponse(file, content_type='application/zip') 

def regenerate(): 
    try: 
        add = add + 1 
    except: 
        add = 0 
    if (add > 100): 
        cleardb() 
    return random.randint(1, 100000) 

def cleardb(): 
    #Clear the database 
    skinlists = models.SkinList.objects.filter (created_at__lt=timezone.now () - timedelta (minutes=20))
    for skinlist in skinlists:
        for skin in skinlist.skin.all ():
            if skin.cont.count () == 1: 
                skin.delete () 
    skinlists.delete ()
