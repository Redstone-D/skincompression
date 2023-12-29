import io
import zipfile
from django.shortcuts import render 
from . import forms 
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.base import ContentFile 
from . import text

# Create your views here. 

def index(request): 
    if request.method == "POST": 
        form = forms.UploadAndCompressForm(request.POST, request.FILES) 
        if form.is_valid():
            # Get the uploaded files and the text input from the form
            files = request.FILES.getlist("files")
            name = form.cleaned_data["text"] 
            skin = [] 
            tran = "" 

            # Create a ZIP file in memory
            zip_buffer = io.BytesIO() 
            with zipfile.ZipFile(zip_buffer, "w") as zip_file: 
                # Add the uploaded files to the ZIP file
                for file in files: 
                    zip_file.writestr(file.name, file.read()) 
                    skin.append(text.skinprop(file)) 
                    tran += text.getText(file.name, name) 
                # Create a ContentFile object from the text input
                text_file = ContentFile(text.getManText(name)) 
                json_file = ContentFile(str(text.getJson(skin))) 
                lang_file = ContentFile(text.getLang(tran, name)) 
                # Add the text file to the ZIP file with Json file 
                zip_file.writestr("manifest.json", text_file.read()) 
                zip_file.writestr("skins.json", json_file.read()) 
                zip_file.writestr("texts/en_US.lang", lang_file.read()) 

            # Return the ZIP file as a response
            response = HttpResponse(zip_buffer.getvalue(), content_type="application/zip") 
            response["Content-Disposition"] = f"attachment; filename={name}.mcpack"
            return response 
    return render(request, "compress/index.html", { 
        "form": forms.UploadAndCompressForm 
    })  
