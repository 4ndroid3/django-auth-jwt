from authentication.views import UserView
from auth_jwt.routers import CustomRouter

router = CustomRouter()
router.register(r'usuario', UserView)

urlpatterns = router.urls
