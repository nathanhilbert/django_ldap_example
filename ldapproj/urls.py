from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ldapproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^logindah$', 'tester.views.logindah', name='login'),
    url(r'^nologin$', 'tester.views.nologin', name='nologin'),
    url(r'^mylogin$', 'tester.views.login_user'),

    url(r'^admin/', include(admin.site.urls)),

)
