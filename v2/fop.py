import hashlib
import io
import zipfile 

from django.http import HttpResponse 
from . import skins 
from . import models  

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
        object = models.Skin.objects.create(file=sfile, name=file_name) 
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
