from django.http import HttpResponseNotFound, HttpResponseServerError
from django.template import RequestContext
from django.template.loader import render_to_string


def custom_500(request):
  return HttpResponseServerError(render_to_string("500.html", RequestContext(request)))

def custom_404(request):
    return HttpResponseNotFound(render_to_string("404.html", RequestContext(request)))