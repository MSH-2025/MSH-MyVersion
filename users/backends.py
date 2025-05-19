from axes.backends import AxesBackend

class SafeAxesBackend(AxesBackend):
    def authenticate(self, request=None, *args, **kwargs):
        if request is None:
            return None  # пропускаем, если request отсутствует
        return super().authenticate(request, *args, **kwargs)