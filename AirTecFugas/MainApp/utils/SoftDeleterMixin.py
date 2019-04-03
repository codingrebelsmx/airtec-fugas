from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

class SoftDeleterMixin(object):
    def delete(self, request, *args, **kwargs):
        modelo = get_object_or_404(self.model, pk=self.kwargs['pk'])
        modelo.is_enabled=False
        modelo.save()
        return redirect(self.success_url)



