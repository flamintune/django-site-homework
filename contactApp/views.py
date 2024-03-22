from django.shortcuts import render

def contact(request):
    html = '<html><body>欢迎咨询</body></html>'
    return HttpResponse(html)
 
def recruit(request):
    html = '<html><body>加入恒达</body></html>'
    return HttpResponse(html)
# Create your views here.
