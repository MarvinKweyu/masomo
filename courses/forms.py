from django import forms
from django.forms.models import inlineformset_factory
from courses.models import Course, Module

# build formset, i.e nested form dynamically
ModuleFormSet = inlineformset_factory(
    Course, Module, fields=["title", "description"], extra=2, can_delete=True
)
