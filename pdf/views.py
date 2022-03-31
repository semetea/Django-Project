from django.shortcuts import render
import pdfplumber

# Create your views here.
def index(request) :
    if request.method == 'POST' :
        rawPdf = request.FILES.get('pdf')
        pdf = pdfplumber.open(rawPdf)
        pdfPage = pdf.pages
        context = {
            'pdfPage' : pdfPage
        }       
        return render(request, "pdf/index.html", context)

    return render(request, "pdf/index.html")
       
