from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .views import (
    AuthorViewSet,
    BlogViewSets,
    CategoryViewSet,
    TagViewSets,
    RegisterView,
    CommentView,
)


router = DefaultRouter()
router.register("post", BlogViewSets, basename="posts")
router.register("category", CategoryViewSet, basename="category")
router.register("tag", TagViewSets, basename="tag")
router.register("comments", CommentView, basename="comment")
router.register("authors", AuthorViewSet, basename="authors")

posts_router = routers.NestedDefaultRouter(router, "post", lookup="post")
posts_router.register("comments", CommentView, basename="post-comments")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
