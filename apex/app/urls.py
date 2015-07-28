from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'sums', views.SumViewSet, base_name='sum')

urlpatterns = router.urls
