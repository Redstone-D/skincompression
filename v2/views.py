from django.utils import timezone 
from datetime import timedelta 
import json 
import uuid 
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
        name = request.POST["name"] 
        file_list = request.FILES.getlist("Upload") 
        skin_list = fop.start(file_list) 
        try: 
            slm = models.SkinList.objects.get(id=num) 
        except: 
            slm = models.SkinList.objects.create(id=num) 
        slm.skin.set(skin_list) 
        slm.name = name 
        slm.save() 
        return JsonResponse({
            "rid": num 
        }) 
    return render(request, "v2/index.html") 

def add(request, rid): 
    if (request.method == "POST"): 
        file_list = request.FILES.getlist("Upload") 
        skin_list = fop.start(file_list) 
        sl = models.SkinList.objects.get(id=rid) 
        slm = list(models.SkinList.objects.get(id=rid).skin.all()) 
        sl.skin.set(slm + skin_list) 
        sl.save() 
        return JsonResponse({ 
            "rid": rid, 
            "pid": sl.id 
        }) 
    return render(request, "v2/add.html") 

def process(request, rid): 
    return JsonResponse({ 
        "rid": rid 
    }) 

def app(request, rid): 
    slm = models.SkinList.objects.get(id=rid) 
    skin_list = slm.skin.all() 
    skins = [] 
    for skin in skin_list: 
        skins.append({ 
            "id": skin.id, 
            "name": skin.name, 
        }) 
    slm.save() 
    return JsonResponse({ 
        "skins": skins, 
        "id": rid 
    })  

def changeName(request, pid): 
    if request.method == "POST": 
        name = request.POST["name"] 
        ins = models.Skin.objects.get(id=pid) 
        ins.name = name 
        ins.save() 
    return JsonResponse({
        "status": 0 
    }) 
    
def changeModel(request, pid): 
    if request.method == "POST": 
        model = request.POST["model"] 
        ins = models.Skin.objects.get(id=pid) 
        ins.model = model 
        ins.save() 
    return JsonResponse({
        "status": 0 
    }) 

def getskinprop(request, pid): 
    skin = models.Skin.objects.get(id=pid) 
    return JsonResponse({ 
        "id": skin.id, 
        "name": skin.name, 
        "model": skin.model 
    }) 

def picture(request, pid): 
    return FileResponse(models.Skin.objects.get(id=pid).file) 

def getcompress(request, rid):  
    return fop.getFile(rid)  


def deleteskin(request, pid): 
    if request.method == "POST": 
        models.Skin.objects.delete(id=pid) 
    return 1 

def regenerate(): 
    try: 
        add = add + 1 
    except: 
        add = 0 
    if True: 
        cleardb() 
    return random.randint(1, 100000) 

def cleardb(): 
    #Clear the database 
    skinlists = models.SkinList.objects.filter (created_at__lt=timezone.now () - timedelta (minutes=100)) 
    print(skinlists) 
    for sl in skinlists: 
        sl.delete() 
    skins = models.Skin.objects.filter(cont__isnull=True) 
    print(skins) 
    for s in skins: 
        s.delete() 
