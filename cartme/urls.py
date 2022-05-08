from django.contrib import admin
from django.urls import path,include, re_path
    


from django .views.static import serve
from django.conf import settings


admin.site.site_header = "Admin — Cartme.pk"
admin.site.site_title = " — Cartme.pk"
admin.site.index_title = "Welcome to Cartme.pk"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})

]



