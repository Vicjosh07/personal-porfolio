from django.shortcuts import render
from .models import Intro, Expertise, Experience, Education, Project, Certificates
from django.db.models import F, ExpressionWrapper, Case, When, Value, BooleanField


# Create your views here.
def index(request):
    profile_intro = Intro.objects.first()
    expertise = Expertise.objects.all()
    experience = Experience.objects.annotate(
    is_ongoing=Case(
        When(end_date__isnull=True, then=Value(True)),
        default=Value(False),
        output_field=BooleanField()
    )
).order_by('-is_current', '-end_date', '-start_date')
    # education = Education.objects.all().order_by('-end_date', '-start_date')
    education = Education.objects.annotate(
    is_ongoing=Case(
        When(end_date__isnull=True, then=Value(True)),
        default=Value(False),
        output_field=BooleanField()
    )
).order_by('-is_current', '-end_date', '-start_date')
    # Make a flat list of all skills
    all_skills = []
    for item in expertise:
        skills = [skill.strip() for skill in item.expertise.split(',')]
        all_skills.extend(skills)

    projects = Project.objects.all()

    certificates = Certificates.objects.all()

    context = {
        'profile_intro': profile_intro,
        'expertise': all_skills,
        'experience': experience,
        'education': education,
        'projects': projects,
        'certificates': certificates
    }

    return render(request, 'index.html', context=context)
