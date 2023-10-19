from django.urls import path
from .views import *

urlpatterns = [
    path('', PostViev.as_view(), name='home'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('review/<int:pk>/', AddComment.as_view(), name='add_comment'),
    path('new/', PostCreate.as_view(), name='post_new'),
    path('<int:pk>/edit', BlogUpdte.as_view(), name='post_edit'),
    path('<int:pk>/delete', BlogDelete.as_view(), name='post_delete'),
]