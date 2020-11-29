from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

from rest_framework.routers import DefaultRouter

from app1 import views as app1_views
from app2.views import BookViewSet

router = DefaultRouter()
router.register("alts", app1_views.AViewset, basename="alts")
# router.register("books", BookViewSet, basename="books")


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^api-auth/', include('rest_framework.urls')),

    path('', include(router.urls)),
    path("api/a/", app1_views.AListView.as_view()),
    path("api/a/<int:pk>/", app1_views.ARetrieveView.as_view()),
    path("api/b/<int:pk>", app1_views.BListView.as_view()),
    # path("api/b/", app1_views.BListView.as_view()),
    # path("api/b/<int:pk>/", app1_views.BRetrieveView.as_view()),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns