#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AABau.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



from career.models import JobPositions

'''Here we have some data that can be seeded directly to the database by simply running the script under. Make sure to uncomment the code.'''

#SITE SUPERVISOR
# site_supervisor_1 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.SITE_SUPERVISOR,
#     description="Supervises daily construction activities on a commercial building site in Frankfurt am Main. Ensures safety regulations and schedules are followed.",
#     requirements="3+ years experience as Site Supervisor, knowledge of German construction safety standards, English required, German is a plus.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.FULL_TIME
# )
#
# site_supervisor_2 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.SITE_SUPERVISOR,
#     description="Responsible for coordinating subcontractors and monitoring progress on residential projects in the Frankfurt metropolitan area.",
#     requirements="Construction supervision experience, ability to read technical drawings, strong organizational skills.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.CONTRACT
# )
#
# site_supervisor_3 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.SITE_SUPERVISOR,
#     description="Manages on-site operations for infrastructure projects, ensuring quality control and compliance with local regulations.",
#     requirements="Experience in infrastructure or large-scale construction projects, leadership skills, safety-focused mindset.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.FULL_TIME
# )
#
# #TECHNICAL MANAGER
# technical_manager_1 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.TECHNICAL_MANAGER,
#     description="Leads technical teams and oversees engineering solutions for office and commercial projects in the Frankfurt region.",
#     requirements="Engineering degree, 5+ years experience, strong problem-solving skills, experience managing technical teams.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.FULL_TIME
# )
#
# technical_manager_2 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.TECHNICAL_MANAGER,
#     description="Responsible for technical planning, documentation, and coordination with architects and external engineers.",
#     requirements="Background in civil or structural engineering, excellent communication skills, German language preferred.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.CONTRACT
# )
#
# technical_manager_3 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.TECHNICAL_MANAGER,
#     description="Oversees technical quality and compliance for large-scale construction projects across multiple sites in Hessen.",
#     requirements="Strong leadership skills, experience with German building codes, ability to manage multiple projects simultaneously.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.FULL_TIME
# )
#
# #CONSTRUCTION WORKER
# construction_worker_1 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
#     description="Performs general construction work including concrete, masonry, and site preparation on projects around Frankfurt am Main.",
#     requirements="Previous construction experience preferred, physical fitness, basic German language skills.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.FULL_TIME
# )
#
# construction_worker_2 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
#     description="Supports skilled tradesmen and assists with renovation and refurbishment projects in residential buildings.",
#     requirements="Willingness to learn, reliability, ability to work in a team.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.PART_TIME
# )
#
# construction_worker_3 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
#     description="Works on infrastructure and commercial construction sites, handling materials, tools, and basic technical tasks.",
#     requirements="Experience on construction sites is an advantage, safety awareness, ability to follow instructions.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.CONTRACT
# )
#
# #OFFICE ADMINISTRATOR
# office_administrator_1 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.OFFICE_ADMINISTRATOR,
#     description="Manages office documentation, schedules meetings, and supports project managers in a construction company based in Frankfurt.",
#     requirements="Previous administrative experience, good organizational skills, proficiency in MS Office or similar tools.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.FULL_TIME
# )
#
# office_administrator_2 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.OFFICE_ADMINISTRATOR,
#     description="Provides part-time administrative support including data entry, document handling, and communication with suppliers.",
#     requirements="Attention to detail, basic computer skills, ability to multitask.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.PART_TIME
# )
#
# office_administrator_3 = JobPositions.objects.create(
#     title=JobPositions.TitleChoices.OFFICE_ADMINISTRATOR,
#     description="Assists with HR documentation, onboarding paperwork, and internal office coordination.",
#     requirements="Good communication skills, experience with administrative or HR tasks is a plus.",
#     location="Frankfurt am Main, Germany",
#     employment_type=JobPositions.EmploymentChoices.PART_TIME
# )
