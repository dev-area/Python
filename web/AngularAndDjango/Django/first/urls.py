from django.conf.urls import url
from first import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^links/$' , views.LinksPageView.as_view()),
    url(r'^getcust/$',views.Customers.getCust),
]
