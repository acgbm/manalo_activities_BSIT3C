from django.urls import path
from .views import index, admin, include

app_name = "app"
urlpatterns = [
path('admin/', admin.site.urls),
path('/', include('index.urls', namespace="index")),
]
