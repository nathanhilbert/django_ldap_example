
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext



# Create your views here.


def logindah(request):
    #authetnicate this
    output = ""
    output += "hello " + str(request.user) + "<br>"
    output +=  "you are authenticated maybe: " + str(request.user.is_authenticated())
    return HttpResponse("<html>" + output + "</html>", mimetype="text/html")

def nologin(request):
    return HttpResponse("<html>here is not authenticated</html>", mimetype="text/html")

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
    user = authenticate(username=username, password=password)
    print "and finally here is my user", user
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/logindah')
    #return render(request, 'thelogin.html', RequestContext(request))
    return render_to_response('thelogin.html', RequestContext(request))
    #return render_to_response('login.html', context_instance=RequestContext(request))
