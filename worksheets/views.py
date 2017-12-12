from django.shortcuts import render

# Create your views here.
def sheet_file(request):
    return render(request, 'worksheets/wf.html', {})
