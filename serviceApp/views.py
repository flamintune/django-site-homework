from django.shortcuts import render
from django.shortcuts import HttpResponse


def download(request):
    html = '<html><body>资料下载</body><ml>'
    return HttpResponse(html)
 
def  platform(request):
    html = '<html><body>人工智能开放平台</body><ml>'
    return HttpResponse(html)
# Create your views here.
