# django
from django.urls import path, include
# third
# own
from apps.user.views import Logout

urlpatterns = [
    path('administrator/', include(('apps.user.urls_administrator', 'administrator'))),
    path('supplier/', include(('apps.user.urls_supplier', 'supplier'))),
    path('technical/', include(('apps.user.urls_technical', 'technical'))),
    # path('client/', include(('apps.user.urls_client', 'client'))),
    path('logout/', Logout.as_view(), name='logout'),
]