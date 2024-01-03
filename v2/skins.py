import hashlib 

class skin: 
    file = None 
    model = "geometry.humanoid.customSlim" 
    name = "" 

    def __init__(self, file): 
        self.name = file.name 
        file.name = hashlib.md5(self.name[:-4].encode("UTF-8")).hexdigest() + ".png" 
        self.file = file 

    def get_file(self): 
        return self.file 

    def to_dict(self):
        return {
            "name": self.name,
            "file": self.file.name,
        } 
