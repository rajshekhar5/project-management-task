from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectMemberViewSet, TaskViewSet, CommentViewSet, RegisterUserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'project-members', ProjectMemberViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', include(router.urls)),
]


urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
