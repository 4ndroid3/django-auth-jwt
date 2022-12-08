from rest_framework.routers import DefaultRouter

class CustomRouter(DefaultRouter):
    """
    Extend DRF's built-in DefaultRouter to:
    1. Support bulk operations
    2. Alphabetically order endpoints under the root view
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update the list view mappings to support bulk operations
        self.routes[0].mapping.update({
            'put': 'bulk_update',
            'patch': 'bulk_partial_update',
            'delete': 'bulk_destroy',
        })