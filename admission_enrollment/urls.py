from django.conf.urls import url
from django.contrib import admin

from admission import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home_url"),
    url(r'^submit/$', views.save_application, name="submit_application"),
    url(r'^search/$', views.search_admission, name="search_admission"),

]
