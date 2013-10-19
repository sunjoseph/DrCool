
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from mezzanine.core.views import direct_to_template
import views

admin.autodiscover()

urlpatterns = patterns("",
    url('^admin/', include(admin.site.urls)),
    url(r'^$', views.homepage, name='home'),
    url(r'^', include("mezzanine.urls")),    
    # url("^$", "mezzanine.blog.views.blog_post_list", name="home"),    
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
