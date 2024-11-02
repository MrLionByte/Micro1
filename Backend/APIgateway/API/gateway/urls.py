from django.urls import path
from .views import Gateway, xassert

urlpatterns = [
    # path('admin_action/<path:path>', xassert, name='xassert'),
    path('user_action/<path:path>', Gateway.as_view(), name='gateway'),
    path('admin_action/<path:path>', Gateway.as_view(), name='gateway')
]
