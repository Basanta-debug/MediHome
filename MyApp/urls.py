from .import views
from django.urls import path
from .views import khaltiRequestView,khaltiVerifyView


urlpatterns = [
      path('home/',views.appointForm, name="home"),
      path('contact/',views.contact, name="contact"),
      path('khaltirequest/',khaltiRequestView.as_view(),name='khaltirequest'),
      path('khaltiverify/',khaltiVerifyView.as_view(),name='khaltiverify'),

     

      

]
