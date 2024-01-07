import hashlib
import io
import json
import os
import uuid
import zipfile 

from django.http import HttpResponse

from skincompress.settings import BASE_DIR 
from . import skins 
from . import models  
from django.core.files.base import ContentFile 

def start(file_list): 
    skin_list = [] 
    for file in file_list: 
        skin_list += file_to_list(file) 
    return skin_list 

def file_to_list(sfile): 
    ext = sfile.name[-4:] 
    if (ext == ".zip"): 
        skin_list = [] 
        with zipfile.ZipFile(sfile, 'r') as zip: 
            file_names = zip.namelist() 
            for file_name in file_names: 
                skin_list += file_to_list(zip.open(file_name).read())  
        return skin_list 
    #elif (ext == ".mcpack") 没有做 
    elif (ext == ".png"): 
        file_name = sfile.name 
        sfile.name = hashname(file_name) 
        object = models.Skin.objects.create(file=sfile, name=file_name[:-4]) 
        return [object] 
    else: 
        return [] 

def topkg(skin_list): 
    zip_buffer = io.BytesIO() 
    name = "" 
    with zipfile.ZipFile(zip_buffer, "w") as zip_file: 
        for skin in skin_list: 
            file = skin.get_file() 
            name += skin.name 
            zip_file.writestr(file.name, file.read()) 
    return io.BytesIO(zip_buffer.getvalue()) 
    # response = HttpResponse(zip_buffer.getvalue(), content_type="application/zip") 
    # response["Content-Disposition"] = f"attachment; filename=test.zip"
    # return response 

def hashname(ori_name): 
    return hashlib.md5(ori_name[:-4].encode("UTF-8")).hexdigest() + ".png"  

def getFile(rid): 
    s = [] 
    tran = "" 
    skins = models.SkinList.objects.get(id=rid).skin.all() 
    skinlist = models.SkinList.objects.get(id=rid) 
    zip_buffer = io.BytesIO() 
    with zipfile.ZipFile(zip_buffer, "w") as zip_file: 
        # Add the uploaded files to the ZIP file
        for skin in skins: 
            file_name = skin.file.name[9:] 
            zip_file.writestr(file_name, skin.file.read()) 
            print(file_name) 
            s.append(skinprop(skin.file, skin.model)) 
            tran += getText(file_name, skin.name, skinlist.name) 
        # Create a ContentFile object from the text input 
        text_file = ContentFile(getManText(skinlist.name)) 
        json_file = ContentFile(str(getJson(s, skinlist.name))) 
        lang_file = ContentFile(getLang(tran, skinlist.name)) 
        # Add the text file to the ZIP file with Json file 
        zip_file.writestr("manifest.json", text_file.read()) 
        zip_file.writestr("skins.json", json_file.read()) 
        zip_file.writestr("texts/en_US.lang", lang_file.read()) 

    # Return the ZIP file as a response
    response = HttpResponse(zip_buffer.getvalue(), content_type="application/zip") 
    response["Content-Disposition"] = f"attachment; filename={skinlist.name}.mcpack" 
    return response 

def genManifest(name): 
    out = {
        "format_version": 1,
        "header": {
            "name": name,
            "uuid": str(uuid.uuid4()), 
            "version": [
                1, 
                0,
                0
            ]
        },
        "modules": [
            {
                "type": "skin_pack",
                "uuid": str(uuid.uuid4()),
                "version": [
                    1,
                    0, 
                    0
                ]
            }
        ]
    } 
    return out 

def getManText(name): 
    return str(json.dumps(genManifest(name)))  

def getJson(li, pname): 
    return json.dumps({
        "skins": li, 
        "serialize_name": pname,
        "localization_name": pname 
    })  

def getLang(str, pname): 
    return f"skinpack.{pname}={pname}{str}" 

def skinprop(file, model): 
    return { 
        "localization_name": file.name, 
        "geometry": model, 
        "texture": file.name, 
        "type": "free" 
    } 

def getText(fname, name, proname): 
    return f"\nskin.{proname}.{fname}={name}" 
