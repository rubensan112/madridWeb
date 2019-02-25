"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from backend.api import urls as api_urls
#from backend.authentication import urls as authentication_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView, TemplateView
from backend.authentication import urls as authentication_urls

urlpatterns = [
    url(r'^api/', include(api_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), #Creo que basta con esto para que la api tenga el boton del login. Lo cual es muy extraño
    url(r'^admin/', admin.site.urls),
    url(r'^login', RedirectView.as_view(pattern_name='login', permanent=False)),
    url(r'^logout', RedirectView.as_view(pattern_name='logout', permanent=False)),
    url(r'^account/', include(authentication_urls)),

]
#url(r'^account/', include(authentication_urls)),


urlpatterns += [

    #url(r'^$', login_required(TemplateView.as_view(template_name='index.html')),
        #name='home'),
    url(r'^schema', schema_view),
    url(r'^.*', TemplateView.as_view(template_name='index.html'), name='email-detail'),

]





