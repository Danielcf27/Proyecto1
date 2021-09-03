from django.http import HttpResponse
from django.template import loader
def saludo(request):
    t= loader.get_template('Proyecto1/uno.html')
    return 