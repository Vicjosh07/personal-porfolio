from django.contrib import admin
from .models import Intro, Expertise, \
    Experience, Education, Project, Certificates
# Register your models here.

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Disable add button if instance exists
        return not Intro.objects.exists()

    def changelist_view(self, request, extra_context=None):
        # Redirect to the edit page if instance exists
        obj = Intro.objects.first()
        if obj:
            from django.shortcuts import redirect
            return redirect(f'/admin/home/intro/{obj.id}/change/')
        return super().changelist_view(request, extra_context)

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Disable add button if instance exists
        return not Expertise.objects.exists()

    def changelist_view(self, request, extra_context=None):
        # Redirect to the edit page if instance exists
        obj = Expertise.objects.first()
        if obj:
            from django.shortcuts import redirect
            return redirect(f'/admin/home/expertise/{obj.id}/change/')
        return super().changelist_view(request, extra_context)
   

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Certificates)
