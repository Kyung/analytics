from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FittleAnalytics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ganalytics/$', 'Analytics.views.ganalytics'),
    url(r'^challenge/detail/$', 'Analytics.views.challenge_detail'),
    url(r'^challenge/$', 'Analytics.views.challenge_list'),
    url(r'^member/post/$', 'Analytics.views.member_post'),
    url(r'^admin/', include(admin.site.urls)),
)
