# -*- coding: UTF-8 -*-
from django.urls import path
from PdfRead import views

urlpatterns = [
path('pdfread/',views.pdfread),
path('pdflist/',views.pdflist),
path('login/',views.login),
path('reg/',views.reg),
path('sendemil/',views.ssendemil)
]
