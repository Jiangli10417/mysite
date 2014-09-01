from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts  import render_to_response
def test(request):

    return render_to_response("formgroup.html",locals())

