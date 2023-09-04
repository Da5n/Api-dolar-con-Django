from django.shortcuts import render
import requests

#Funcion que dara el valor del dolar actual
def valor_del_dolar():
    Api_url = "https://mindicador.cl/api/dolar"
    respuesta = requests.get(Api_url)
    data = respuesta.json()

    #Retornamos el primer valor encontrado del dolar que correspondera al valor mas actual
    return data['serie'][0]['valor']

def mostrar_valor_dolar(request):
    valordolar = valor_del_dolar()
    return render(request, 'mostrardolar.html', {'valor_del_dolar': valordolar})
# Create your views here.
