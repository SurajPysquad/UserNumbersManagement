from django.urls import path
from . views import MainPageView, UserAddView, ALlUserView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('', MainPageView.as_view(), name = "index_page"),
    path("login_view", UserAddView.as_view(), name="login_page"),
    path("all_user", ALlUserView.as_view(), name = "alluser"),
    path('delete/<int:id>/', UserDeleteView.as_view(), name ="delete_record"),
    path('update/<int:pk>/', UserUpdateView.as_view(), name = "user_update_record"),

]
