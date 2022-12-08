from authentication.views import RegisterView
from auth_jwt.routers import CustomRouter

router = CustomRouter()
router.register(r'generos', RegisterView)

urlpatterns = router.urls
