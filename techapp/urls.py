"""
URL configuration for lapify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from techapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.home),
    path('product',views.privacyp),
    path('login',views.Userlogin),
    path('register',views.register),
    path('logout',views.userlogout),
    path('details/<pid>',views.laptopdetails),
    path('addtocart/<laptopid>',views.addtocart),
    path('mycart',views.showmycart),
    path('delete/<cartid>',views.delete),
    path('checkout',views.checkout),
    path('makepayment',views.makepayment),
    path('billing',views.billing),
    path('order',views.order),
    path('shopnow',views.shopnow),
    path('contactus',views.contactus),
    path('thankyou',views.thankyou),
]
urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)