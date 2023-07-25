from django.urls import path
from . import views

app_name='bacapres'

urlpatterns = [
    path('', views.BacapresView.as_view(), name="bacapres_list"),
    path('create', views.BacapresCreateView.as_view(), name="create_bacapres"),
    path('<int:id>/edit', views.BacapresDetailView.as_view(), name="edit_bacapres"),
    path('<int:id>/delete', views.BacapresView.as_view(), name="delete_bacapres"),
]