from django.http import JsonResponse
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from rest_framework_nested.routers import DefaultRouter


from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

# from users.views import hueta, UserLogoutAPIView, UserLoginAPIView
from users.views import hueta


def index_page(request):
    return JsonResponse({"ok": 200})


v1_router = DefaultRouter()
# v1_router.register("auth/by-password/login", CustomAuthToken, basename="auth")
# v1_router.register("users", UserViewSet, basename="user")
v1_router.register(r"register", hueta, basename="user_register")

api_v1_urlpatterns = [
    path("", include(v1_router.urls)),
    path('api/user/', include('drf_user.urls'))
    # path('accounts/register', CustomAuthToken.as_view(), name='register'),
    # path("login/", UserLoginAPIView.as_view(), name="user_login"),
    # path(r"register/", hueta, name="user_register"),
    # path("logout/", UserLogoutAPIView.as_view(), name="user_logout")
]


api_url_patterns = [
    path("", index_page),
    path("v1/", include(api_v1_urlpatterns)),
]

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + api_url_patterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

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
