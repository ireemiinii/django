from django.shortcuts import render,redirect
from library.models import *
from django.core.files.storage import FileSystemStorage

from .forms import LNotesForm,SNotesForm
from .models import LectureNotes
from .models import StudentNotes

# Create your views here.
def home(request, *args, **kwargs):
    academician = Academician.objects.all()
    cname = Course.objects.all()
    context = {
        'academician': academician,
        'course': cname,

    }
    return render(request, 'library/home.html', context)

# def courses(request, *args, **kwargs ):

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'library/upload.html', context)

def lnotes_list(request):
    lnote = LectureNotes.objects.all()
    return render(request, 'library/lnotes_list.html', {
        'lnote': lnote
    })

def snotes_list(request):
    snote = StudentNotes.objects.all()
    return render(request, 'library/snotes_list.html', {
        'snote': snote
    })


def upload_lnotes(request):
    if request.method == 'POST':
        form = LNotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return redirect('library/lnotes_list.html')
    else:
        form = LNotesForm()
    return render(request, 'library/upload_lnotes.html', {
        'form': form
    })

def upload_snotes(request):
    if request.method == 'POST':
        form = SNotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return redirect('library/snotes_list.html')
    else:
        form = SNotesForm()
    return render(request, 'library/upload_snotes.html', {
        'form': form
    })
