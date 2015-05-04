from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'groupster.views.LandingView', name='landing'),
    url(r'^jobs$', 'groupster.views.JobsView', name="jobs"),
    url(r'^about$', 'groupster.views.AboutView', name="about"),

    url(r'^admin/', include(admin.site.urls)),
)
