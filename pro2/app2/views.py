from django.shortcuts import render

from django.http import HttpResponse
def wish(request):
    html_code="<html> <body> <h1>this programing of tesing</h1></body> </html>"

    return HttpResponse(html_code)
