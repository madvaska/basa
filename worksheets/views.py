from django.shortcuts import render,redirect
from .models import WorksheetFile
from .forms import WFForm
#from . import views

# Create your views here.
def sheet_file(request):
    wsfiles = WorksheetFile.objects.all()
    return render(request, 'worksheets/wf.html', {'wsf':wsfiles})

def sheet_file_form(request):
    if request.method == "POST":
        formdata = WFForm(request.POST,request.FILES)
        print(formdata.is_valid())
        if formdata.is_valid():
            form1 = formdata.save(commit=False)
            #form1.original = request.original
            #form1.fileName = request.fileName
            form1.save()
            #return redirect('sheet_file', pk=form1.pk)
            return redirect('sheet_file')
    #    else:
    #        form = WFForm()
    #        return render(request, 'worksheets/wfform.html', {'form':form})
    else:
        form = WFForm()
    return render(request, 'worksheets/wfform.html', {'form':form})
