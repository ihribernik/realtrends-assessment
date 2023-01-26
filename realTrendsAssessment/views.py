from django.views.generic import TemplateView
from http import HTTPStatus


class HomeView(TemplateView):
    template_name = "realTrendsAssessment/index.html"


class ForbiddenHandler(TemplateView):
    error_code = HTTPStatus.FORBIDDEN
    template_name = "403.html"

    def dispatch(self, request, *args, **kwargs):
        """For error on any methods return just GET"""
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["error_code"] = self.error_code
        return context

    def render_to_response(self, context, **response_kwargs):
        """Return correct status code"""
        response_kwargs = response_kwargs or {}
        response_kwargs.update(status=self.error_code)
        return super().render_to_response(context, **response_kwargs)


class ErrorHandler(TemplateView):
    error_code = HTTPStatus.NOT_FOUND
    template_name = "404.html"

    def dispatch(self, request, *args, **kwargs):
        """For error on any methods return just GET"""
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["error_code"] = self.error_code
        return context

    def render_to_response(self, context, **response_kwargs):
        """Return correct status code"""
        response_kwargs = response_kwargs or {}
        response_kwargs.update(status=self.error_code)
        return super().render_to_response(context, **response_kwargs)


class InternalErrorView(TemplateView):
    error_code = HTTPStatus.INTERNAL_SERVER_ERROR
    template_name = "500.html"

    def dispatch(self, request, *args, **kwargs):
        """For error on any methods return just GET"""
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["error_code"] = self.error_code
        return context

    def render_to_response(self, context, **response_kwargs):
        """Return correct status code"""
        response_kwargs = response_kwargs or {}
        response_kwargs.update(status=self.error_code)
        return super().render_to_response(context, **response_kwargs)
