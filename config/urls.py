from django.http import JsonResponse
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from users.views import UserViewSet
from classifier.dataset.views import ClassifierView
from classifier.request_history.views import RequestHistoryViewSet


def index_page(request):
    return JsonResponse({"ok": 200})


v1_router = DefaultRouter()

api_v1_urlpatterns = [
    path("users/login/", views.obtain_auth_token),
    path(
        "users/",
        UserViewSet.as_view(
            {
                "get": "read_me",
                "patch": "partial_update_me",
                "put": "update_me",
                "delete": "destroy_me",
                "post": "create",
            }
        )
    ),
    path("classification", ClassifierView.as_view()),
    path("history", RequestHistoryViewSet.as_view({"get": "list"}), name="history")
]

api_url_patterns = [
    path("", index_page),
    path('admin/', admin.site.urls),
    path("v1/", include(api_v1_urlpatterns)),
]


urlpatterns = api_url_patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

schema_view = get_schema_view(
    openapi.Info(title="Plan Classifier API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=api_url_patterns,
)

urlpatterns += [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]
