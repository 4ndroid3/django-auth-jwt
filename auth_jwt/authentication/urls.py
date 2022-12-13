""" URLs de Usuario """
from authentication.views import UserView, CreateUserView
from auth_jwt.routers import CustomRouter

router = CustomRouter()
router.register(r'user', UserView)
router.register(r'create-user', CreateUserView)

urlpatterns = router.urls
