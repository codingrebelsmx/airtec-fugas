"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required, login_required
from datetime import datetime
from MainApp.logic import PlantaLogicB


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return render(request,
            'MainApp/Home/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            })
    else:
        return redirect('dashboard')

@login_required
def dashboard(request):
    """Renders the home page."""
    cliente = request.session.get("id_cliente",None)
    id_planta = request.session.get("id_planta",None)

    if cliente != None and id_planta != None:
        planta = PlantaLogicB.get_planta(id_planta)
        total_fugas = PlantaLogicB.get_cantidad_fugas(id_planta)
        fugas_resueltas = PlantaLogicB.get_cantidad_fugas_resueltas(id_planta)
        porcentaje_fugas = PlantaLogicB.calcula_porcentaje_fugas(id_planta)
        ahorro_economico = PlantaLogicB.calcula_ahorro_economico(id_planta)
        ahorro_energetico = PlantaLogicB.calcula_ahorro_energetico(id_planta)
        emisiones_co2 = PlantaLogicB.calcula_emisiones_co2(id_planta)

        return render(request, 'MainApp/Dashboard/dashboard.html',
            {
                'title':'Dashboard',
                'year':datetime.now().year,
                'menu':"DASHBOARD",
                'total_fugas': total_fugas,
                'fugas_resueltas':fugas_resueltas,
                'porcentaje_fugas':porcentaje_fugas,
                'ahorro_economico':ahorro_economico,
                'ahorro_energetico': ahorro_energetico,
                'emisiones_co2':emisiones_co2
            })
    else:
        return redirect("selec-planta-trabajo")

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'MainApp/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'MainApp/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })

@login_required
@permission_required('ModelsApp.view_fuga')
def mapafugas(request):
    """Renders the about page."""
    cliente = request.session.get("id_cliente",None)
    planta = request.session.get("id_planta",None)

    if cliente != None and planta != None:
        assert isinstance(request, HttpRequest)
        return render(request,
            'MainApp/Fuga/mapa-fugas.html',
            {
                'title':'Mapa fugas',
                'message':'Your application description page.',
                'year':datetime.now().year,
            })
    else:
        return redirect("selec-planta-trabajo")
