"""django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from django.http import HttpResponse



# A function that will behave as a route callback.
def adhoc(request):
    return HttpResponse("Hello (GET from `/adhoc`)")

# A function that will be a route callback with a parameter
def adhoc_regex(request, regex):
    return HttpResponse(f"Hello (GET from `/adhoc-[regex]`)")

# The main entry point to attach to the django routes.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adhoc', adhoc), # An ad-hoc way to include a function directly.
    re_path(r'adhoc-(.*?)', adhoc_regex), # Regex matcher
    path('hello/', include('hello.urls')), # Here we are including another URLconf module, defined at django_example/hello/urls.py

    # Sub paths + lambda
    path('<sub>-<sub_id>/', include([
        path('hello/', lambda request, sub, sub_id: HttpResponse(f'Hello from sub {sub}-{sub_id}')),
    ]))

    # In old django it will be: `url('url_pattern/', view.func, name=name)`
]


# This is also interesting - called when a request is finished.
def my_signal_callback(sender, **kwargs):
    print("Signal recieved - request finished!")
request_finished.connect(my_signal_callback)


# Decorator example (before each request)
@receiver(request_started)
def my_callback(sender, **kwargs):
    print("Request starting!")

