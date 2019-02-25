from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django import views


class View(views.View):
    view_factory = None

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(permitted_methods=[])

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(permitted_methods=[])

    @staticmethod
    def render_template(request, template_name, context=None, **kwargs):
        return render(request, template_name=template_name, context=context, **kwargs)

    @staticmethod
    def redirect_to_named_url(to, **kwargs):
        return redirect(to=reverse_lazy(to), **kwargs)

    @staticmethod
    def redirect_to_url(to, **kwargs):
        return redirect(to=to, **kwargs)
