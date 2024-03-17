from django.contrib import admin
from django.urls import path
from smsapp.views import uhome,ulogin,usignup, usnp , ulogout , create , view , remove
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("uhome" , uhome , name = "uhome"),
    path("" , ulogin , name = "ulogin"),
    path("usignup" , usignup , name = "usignup"),
    path("usnp" , usnp , name = "usnp"),
    path("ulogout" , ulogout , name = "ulogout"),
    path("create" , create , name = "create"),
    path("view" , view , name = "view"),
    path("remove/<int:id>", remove, name="remove")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

