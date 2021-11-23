from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import LatticeTypes,lattice_2D_data,lattice_3D_data,FilesUpload,FileModel
from django.views.generic import TemplateView
from django.core import serializers
import sys
from subprocess import run,PIPE
from .scripts import test
from .forms import LatticeForm,UploadFileForm
from django.core.files.base import ContentFile
import base64
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from ntpath import join
from os.path import isfile
import os
from os import listdir

def index(request):
    lattices  = LatticeTypes.objects.all()
    return render(request,'index.html',{'lattices':lattices})
    #return HttpResponse("<h1>Welcome to Home Page")


def about(request):
    return HttpResponse("<h1>Welcome to About Page")

def calculate(request):
    # lattices  = lattice_2D_data.objects.all()
    return render(request,'calculate.html')
    # return HttpResponse("<h1>Welcome to calculate Page")

def HomeView(TemplateView):
    template_name = 'modals/manual_entry.html'


def upload(request):
    lattices  = LatticeTypes.objects.all()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mypath = os.path.join(BASE_DIR, 'media') 

    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    return render(request,'upload.html',{'files':files})
    # return HttpResponse("<h1>Welcome to calculate Page")

def cluster(request):


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mypath = os.path.join(BASE_DIR, 'media') 

    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    return render(request,'cluster.html',{'files':files})
    # return HttpResponse("<h1>Welcome to calculate Page")


def compute2d(request):

    if request.method == 'POST':
        
        len_a1 = float(request.POST['len_a1'])
        len_b1 = float(request.POST['len_b1'])
        angle1 = float(request.POST['angle1'])

        len_a2 = float(request.POST['len_a2'])
        len_b2 = float(request.POST['len_b2'])
        angle2 = float(request.POST['angle2'])

        print('values:',len_a1,len_b1,angle2)
        new_lattice = lattice_2D_data(a=len_a1,b=len_b1,gamma=angle1)
        new_lattice.save()

        new_lattice = lattice_2D_data(a=len_a2,b=len_b2,gamma=angle2)
        new_lattice.save()

        lat1 = {'a':len_a1,'b':len_b1,'angle':angle1}
        lat2 = {'a':len_a2,'b':len_b2,'angle':angle2}

        distance = test.lattice2d_compute(lat1,lat2)

        print(distance)

        success = distance
       
        return HttpResponse(success)

def compute3d(request):

    if request.method == 'POST':
        
        len_a1 = float(request.POST['a1'])
        len_b1 = float(request.POST['b1'])
        len_c1 = float(request.POST['c1'])
        alpha1 = float(request.POST['alpha1'])
        beta1 = float(request.POST['beta1'])
        gamma1 = float(request.POST['gamma1'])

        len_a2 = float(request.POST['a2'])
        len_b2 = float(request.POST['b2'])
        len_c2 = float(request.POST['c2'])
        alpha2 = float(request.POST['alpha2'])
        beta2 = float(request.POST['beta2'])
        gamma2 = float(request.POST['gamma2'])

        print('values:',len_a1,len_b1,alpha1)
        # new_lattice = lattice_3D_data(a=len_a1,b=len_b1,gamma=len_c1)
        # new_lattice.save()

        # new_lattice = lattice_3D_data(a=len_a2,b=len_b2,gamma=len_c2)
        # new_lattice.save()

        lat1 = {'a':len_a1,'b':len_b1,'c':len_c1,'alpha':alpha1,'beta':beta1,'gamma':gamma1}
        lat2 = {'a':len_a2,'b':len_b2,'c':len_c2,'alpha':alpha2,'beta':beta2,'gamma':gamma2}

        print(lat1)
        print(lat2)

        distance = test.lattice3d_compute(lat1,lat2)

        print(distance)

        success = distance
       
        return HttpResponse(success)





@csrf_exempt
def upload_file(request):

    file = request.FILES.get("file")

    fss = FileSystemStorage()
    filename = fss.save(file.name, file)
    url = fss.url(filename)

    # print(file.name)
    # data = ContentFile(base64.b64decode(file), name=file.name) 
    FileModel.objects.create(doc=url)
    # print(data)



    media_root = settings.MEDIA_ROOT
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mypath = os.path.join(BASE_DIR, 'media') 

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


    return JsonResponse({"link": url,"files":onlyfiles})

@csrf_exempt
def remove_file(request):

    file_name  = request.POST.get("file")
    print(file_name)
    os.remove(os.path.join(settings.MEDIA_ROOT, file_name))

    return JsonResponse({"status": 'removed',"file":file_name})

@csrf_exempt
def getMediaFiles(request):

    print(request.POST.get("file"))

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mypath = os.path.join(BASE_DIR, 'media') 


    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]


    return JsonResponse({"status":1,"files":files})

@csrf_exempt
def compareCIFs(request):

    
    # file1 = float(request.POST['file1'])
    # file2 = float(request.POST['file2'])

    # print('f1:',file1,file2)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, 'media')

    print(path)

    files = [f for f in listdir(path) if isfile(join(path, f))]

    print('fi:',files)

    pathA  = join(path, str(files[0]))
    pathB  = join(path, str(files[1]))

    print('pA:',pathA)


    lat1,lat2=test.genCIF_to_Lattice(pathA,pathB)

    print('values:',lat1,lat2)
    

    distance = test.lattice3d_compute(lat1,lat2)

    print(distance)

    success = distance
    
    return HttpResponse(success)



@csrf_exempt
def computeDistMatrix(request):

    
    # file1 = float(request.POST['file1'])
    # file2 = float(request.POST['file2'])

    # print('f1:',file1,file2)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, 'media')

    print(path)

    files = [f for f in listdir(path) if isfile(join(path, f))]

    pair_tuple_list=[]

    for i in range(0,len(files)):

        for j in range(0,len(files)):

            temp_tuple = (files[i],files[j])
            pair_tuple_list.append(temp_tuple)


    print('fi:',files)
    print('tuples:',pair_tuple_list)
    
    pair_dist_matrix = []

    for pair in pair_tuple_list:


        pathA  = join(path, str(pair[0]))
        pathB  = join(path, str(pair[1]))

        print('pA:',pathA)


        lat1,lat2=test.genCIF_to_Lattice(pathA,pathB)

        print('values:',lat1,lat2)
        

        distance = test.lattice3d_compute(lat1,lat2)

        print(distance)

        pair_dist_matrix.append(distance)

    print(pair_dist_matrix)

    success = pair_dist_matrix
    
    return HttpResponse(success)




