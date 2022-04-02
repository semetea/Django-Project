from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def index(request) :
    context = {}
    if request.method == 'POST' :
        tfrom = request.POST.get("tfrom")
        sfrom = request.POST.get("sfrom")
        sto = request.POST.get("sto")
        translator = Translator()
        trans1 = translator.translate(tfrom, src=sfrom, dest=sto)
        context.update({
            'trans' : trans1.text,
            'tfrom' : tfrom,
            'sfrom' : sfrom,
            'sto' : sto
        })
    return render(request, 'trans/index.html', context)    
