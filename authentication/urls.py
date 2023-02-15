from django.urls import path

from authentication.views import InsertUsersAPIView, UsersListAPIView

urlpatterns = [
    path('api/registration/', InsertUsersAPIView.as_view(), name='Register'),
    path('api/user/list/', UsersListAPIView.as_view(), name="Users List"),
]
