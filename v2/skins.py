import hashlib 

class skin: 
    file = None 
    model = "geometry.humanoid.customSlim" 
    name = "" 

    def __init__(self, file): 
        self.name = file.name 
        file.name = hashlib.md5(file.name) 
        self.file = file 

