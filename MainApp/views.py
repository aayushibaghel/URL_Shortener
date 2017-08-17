from django.shortcuts import render,get_object_or_404
from .models import URL
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect, JsonResponse
from .forms import URLForm
from django.core.urlresolvers import reverse
from django.views import View


# Create your views here.

def create_URL_shortcode(request):
    if request.method == 'GET':
        return render(request,'home.html',{'form':URLForm})
    if request.method == 'POST':
        form = URLForm(request.POST or None)
        url= request.POST.get('url')
        obj,created = URL.objects.get_or_create(url=url)
        print(obj)
        return render(request,'shortened.html',{'url':obj.url,'shortcode':obj.shortcode})

class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        print("new url is %s"%(qs.url))
        return HttpResponseRedirect(qs.url)

