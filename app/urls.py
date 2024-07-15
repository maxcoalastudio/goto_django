from app.views import TodoviewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'',TodoviewSet)

urlpatterns = router.urls



