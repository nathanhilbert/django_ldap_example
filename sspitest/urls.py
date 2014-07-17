from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^login$', 'tester.views.login', name='login'),
    url(r'^nologin$', 'tester.views.nologin', name='nologin'),
    url(r'^mylogin$', 'tester.views.login_user'),
    
    

    # url(r'^blog/', include('blog.urls')),
)


