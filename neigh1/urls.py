from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('signup/',views.signup,name= 'signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('setup/',views.setup,name="setup"),
    path('setup/bussines_type',views.add_type),
    path('update_profile/',views.update_profile, name="update_profile")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
