from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^drop$', views.drop, name='drop'),
    url(r'^get_tags$', views.get_tags),
    url(r'^get_cloth_names$', views.get_cloth_names),
    url(r'^update_frequency$', views.update_frequency),
    url(r'^add_order', views.add_order),
]
