from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns =[
    path('', views.home),
    path('losujzadanie', views.losujzadanie),
    path('testparametry', views.testparametry),
    path('wyborarkusza', views.wyborarkusza),
    path('formula2023', views.formula2023),
    path('formula2015', views.formula2015),
    path('malamatura', views.malamatura),
    path('baza', views.baza),
    path('kontakt', views.kontakt),
    path('instrukcje', views.instrukcje),
    

    path('ajax/load-tematy/', views.load_tematy, name = 'ajax_load_tematy'),
    path('ajax/load-tematy-test/', views.load_tematy_test, name = 'ajax_load_tematy_test')
    
]