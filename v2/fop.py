import zipfile 

def file_to_list(file): 
    skin_list = [] 
    ext = file.name[-4:] 
    if (ext == ".zip"): 
        zip = zipfile.ZipFile(file) 
        names = zip.namelist() 
        
    return [] 