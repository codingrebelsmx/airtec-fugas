"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

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

def dashboard(request):
    """Renders the home page."""
    cliente = request.session.get("id_cliente",None)
    planta = request.session.get("id_planta",None)

    if cliente != None and planta != None:
        return render(request, 'MainApp/Dashboard/dashboard.html',
            {
                'title':'Dashboard',
                'year':datetime.now().year,
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

def mapafugas(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainApp/Fuga/mapa-fugas.html',
        {
            'title':'Mapa fugas',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )