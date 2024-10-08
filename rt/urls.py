from django.conf.urls import include, url
from . import views


app_name = "RT"

urlpatterns = [
    url(r'^tickets/', include([
        url(r'^new/$', views.new_ticket, name="new-ticket"),
    ])),
    url(r'^connect/rt/$', views.link_account, name="link-account")
]
