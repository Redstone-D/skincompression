import json
import uuid 
# from PIL import Image 

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

def getJson(li): 
    return json.dumps({
        "skins": li 
    })  

def getLang(str, pname): 
    return f"skinpack.{pname}:{pname}={pname}:{pname}\n{str}" 

def skinprop(file): 
    return { 
        "localization_name": "Cinder_64x.png", 
        "geometry": testSex(file),
        "texture": file.name, 
        "type": "free" 
    } 

def testSex(file): 
    ''' 
    try: 
        image = Image.open(file) 
        for x in range(17, 20): 
            for y in range(51, 52): 
                temp = image.getpixel((x, y)) 
                print(temp) 
                if not (temp == (0, 0, 0, 0) or temp == (0, 0, 0, 1)): 
                    return 'geometry.humanoid.custom' 
        return 'geometry.humanoid.customSlim' 
    except: 
    ''' 
    return 'geometry.humanoid.customSlim'  

def getText(name, proname): 
    return f"skin.{proname}.{name[:-4]}={name[:-4]} \n" 
