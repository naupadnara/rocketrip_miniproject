from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^activity/$', 'myapp1.views.activities'),
                       url(r'^activity_add/$', 'myapp1.views.activity_add'),
    # Examples:
    url(r'^$', 'myapp1.views.activities', name='activity')
    # url(r'^$', 'miniproject.views.home', name='home'),
    # url(r'^miniproject/', include('miniproject.miniproject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)