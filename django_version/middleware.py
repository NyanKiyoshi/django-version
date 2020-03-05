from django.conf import settings


class VersionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Project-Version"] = settings.PROJECT_VERSION
        return response
