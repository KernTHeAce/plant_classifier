from django.http import JsonResponse
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from rest_framework_nested.routers import DefaultRouter


from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from users.views import CustomAuthToken, UserViewSet


def index_page(request):
    return JsonResponse({"ok": 200})


v1_router = DefaultRouter()
# v1_router.register("auth/by-password/login", CustomAuthToken, basename="auth")
v1_router.register("users", UserViewSet, basename="user")

api_v1_urlpatterns = [
    path("", include(v1_router.urls)),
    path("auth/by-password/login/", CustomAuthToken.as_view(), name="password-login")
]


api_url_patterns = [
    path("", index_page),
    path("v1/", include(api_v1_urlpatterns)),
]

# schema_view = get_schema_view(
#     openapi.Info(title="Plants Classifier API", default_version="v1"),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
#     patterns=api_url_patterns,
# )

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + api_url_patterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

schema_view = get_schema_view(
    openapi.Info(title="Samurai API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=api_url_patterns,
)

urlpatterns += [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]
