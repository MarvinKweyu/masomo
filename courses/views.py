from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from courses.models import Course


class OwnerMixin(object):
    def get_queryset(self):
        """Return a list of courses created only by current user"""
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    fields = ["subject", "title", "slug", "overview"]
    success_url = reverse_lazy("manage_course_list")


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = "courses/manage/course/form.html"


class ManageCourseListView(OwnerCourseMixin, ListView):
    permission_required = 'courses.view_course'
    template_name = "courses/manage/course/list.html"


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'
    pass


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'
    pass


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    permission_required = 'courses.delete_course'
    template_name = "courses/manage/course/delete.html"


class ManageCourse(ListView):
    """View courses"""

    model = Course
    template_name = "courses/manage/course/list.html"

    def get_queryset(self):
        """Return a list of courses created only by current user"""
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
