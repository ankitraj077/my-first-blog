from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect, HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# Create your views here.
