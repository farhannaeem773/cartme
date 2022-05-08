from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "Admin — Cartme.pk"
admin.site.site_title = " — Cartme.pk"
admin.site.index_title = "Welcome to Cartme.pk"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'))
]


