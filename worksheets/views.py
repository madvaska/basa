from django.shortcuts import render,redirect
from .models import WorksheetFile
from .models import TypeOfWork
from .forms import WFForm
import django.core.exceptions
import xlrd
import re
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

def readSheetFile(filename,sheetname=0):
    print('Открываем файл')
    try:
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(sheetname)
    except Exception:
        return None
    else:
        return sheet

def parseCellToStr(data):
    if(isinstance(data,(str))):
        return data.strip()
    return None

def searchTypeOfWork(cellData):
    try:
        typeOfWork = TypeOfWork.objects.get(name__contains=cellData)
    except DoesNotExist as e:
        return None
    else:
        return typeOfWork.pk


def parseRow(rowValues=[],columnNum=2):
    print('Разбираем строку '+str(rowValues)]
    rowData = []
    for cell in rowValues:
        data = parseCellToStr(cell)
        if(data is None):
            return None
        rowData.append(data)
    if(len(rowData) > columnNum):
        id = searchTypeOfWork(rowData[columnNum])
        if id==0:
            return None
        rowData[columnNum]=id
        return rowData
    else:
        return None
    return None

def isYesRow(rowData=[],yesColumn=3):
    print('Проверяем, что это - YES')
    if(len(rowData) < yesColumn):
        return False
    if(rowData[yesColumn].strip().lower()=u"да"):
        return True
    return False

def parseSheet(sheet,startRow):
    print('Разбираем лист')
    returnData = []
    for rownum in range(startRow, sheet.nrows):
        row = sheet.row_values(rownum)
        rowData = []
        rowData = parseRow(row)
        if(rowData is None):
            return None
        if(len(rowData)==0):
            return None
        if(isYesRow(rowData)):
            returnData.append(rowData)
    return returnData
