from django.urls import path
# from .views import contact
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('courses/',views.courses),
    path('home/',views.home),
]