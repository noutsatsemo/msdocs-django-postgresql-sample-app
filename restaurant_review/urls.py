from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
 

urlpatterns = [
    path('sillausers/', views.SillaUserList.as_view()),
    path('sillaprojects/', views.SillaProjectList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('sillausers/<int:pk>/', views.SillaUserDetail.as_view()),
    path('sillaprojects/<int:pk>/', views.SillaProjectDetail.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)


