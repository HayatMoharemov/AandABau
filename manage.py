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


from django.utils import timezone
from feedback.models import CreateFeedback
from career.models import JobPositions
from ourteam.models import TeamMembersModel

'''Here we have some data that can be seeded directly to the database by simply running the script under. Make sure to uncomment the code.'''

#'''Job positions'''
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

#'''Data ready to seed for feedback app'''


# CreateFeedback.objects.bulk_create([
#     CreateFeedback(
#         name="Michael Thompson",
#         rating=CreateFeedback.Rating.EXCELLENT,
#         comment="Built our dream home exactly on time and budget. The attention to detail was outstanding!",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Sarah Patel",
#         rating=CreateFeedback.Rating.GOOD,
#         comment="Very professional team. Kitchen renovation looks great, just a few small paint touch-ups needed after handover.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="David & Laura Wilson",
#         rating=CreateFeedback.Rating.AVERAGE,
#         comment="Solid work overall, but communication could be better — we had to chase updates several times.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="James Rodriguez",
#         rating=CreateFeedback.Rating.BAD,
#         comment="Significant delays on the extension project. Promised 8 weeks, took almost 5 months. Disappointing.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Emily Chen",
#         rating=CreateFeedback.Rating.EXCELLENT,
#         comment="New roof installed perfectly in bad weather — crew was very efficient and cleaned up thoroughly.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Robert Kline",
#         rating=CreateFeedback.Rating.VERY_BAD,
#         comment="Poor quality materials used for bathroom tiling. Already cracking after 4 months. No real response from office.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Anna Kowalski",
#         rating=CreateFeedback.Rating.GOOD,
#         comment="Office fit-out completed to high standard. Minor electrical issues fixed quickly after we reported them.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Carlos Mendoza",
#         rating=CreateFeedback.Rating.AVERAGE,
#         comment="Decent price and the structure is sound, but finishing work (trim, paint) feels rushed.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Sophie Laurent",
#         rating=CreateFeedback.Rating.EXCELLENT,
#         comment="Renovated our 1970s house — modern, energy-efficient, and beautiful. Project manager was excellent.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Mark Evans",
#         rating=CreateFeedback.Rating.BAD,
#         comment="Driveway and landscaping done, but levels are off — water pools in one corner every rain.",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Lisa & Tom Harper",
#         rating=CreateFeedback.Rating.GOOD,
#         comment="Full home build. Mostly happy — only issue was a 3-week delay due to permit problems (not entirely their fault).",
#         created_at=timezone.now(),
#     ),
#     CreateFeedback(
#         name="Ahmed Al-Sayed",
#         rating=CreateFeedback.Rating.EXCELLENT,
#         comment="Commercial warehouse conversion completed ahead of schedule. Great value and very professional.",
#         created_at=timezone.now(),
#     ),
# ])

#'''Team members'''
# # ====== SITE SUPERVISOR (2) ======
# site_supervisor1 = TeamMembersModel.objects.create(
#     name="Bobi Bobinson",
#     description="Bobi is a dedicated Site Supervisor with extensive experience managing construction projects efficiently.",
#     position=JobPositions.TitleChoices.SITE_SUPERVISOR
# )
# site_supervisor2 = TeamMembersModel.objects.create(
#     name="Lukas Schmidt",
#     description="Lukas ensures all construction sites operate safely, on time, and to high quality standards.",
#     position=JobPositions.TitleChoices.SITE_SUPERVISOR
# )
# ====== TECHNICAL MANAGERS (2) ======
# technical_manager1 = TeamMembersModel.objects.create(
#     name="Sofia Müller",
#     description="Sofia oversees the technical aspects of construction projects, ensuring smooth execution and compliance.",
#     position=JobPositions.TitleChoices.TECHNICAL_MANAGER,
# )
# technical_manager2 = TeamMembersModel.objects.create(
#     name="David Weber",
#     description="David coordinates technical teams and manages project specifications efficiently.",
#     position=JobPositions.TitleChoices.TECHNICAL_MANAGER,
# )
#
# # ====== OFFICE ADMINISTRATORS (2) ======
# office_admin1 = TeamMembersModel.objects.create(
#     name="Anna Fischer",
#     description="Anna handles administrative duties and ensures smooth office operations.",
#     position=JobPositions.TitleChoices.OFFICE_ADMINISTRATOR,
# )
#
# office_admin2 = TeamMembersModel.objects.create(
#     name="Markus Becker",
#     description="Markus supports office workflows with precision and efficiency.",
#     position=JobPositions.TitleChoices.OFFICE_ADMINISTRATOR,
# )
#
# # ====== CONSTRUCTION WORKERS (10) ======
# construction_worker1 = TeamMembersModel.objects.create(
#     name="Jonas Keller",
#     description="Jonas is a skilled Construction Worker performing a variety of on-site tasks.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker2 = TeamMembersModel.objects.create(
#     name="Lena Braun",
#     description="Lena specializes in construction tasks and ensures quality workmanship.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker3 = TeamMembersModel.objects.create(
#     name="Maximilian Hofmann",
#     description="Maximilian performs general construction duties efficiently and safely.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker4 = TeamMembersModel.objects.create(
#     name="Sophia Klein",
#     description="Sophia works on-site executing construction tasks with precision.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker5 = TeamMembersModel.objects.create(
#     name="Felix Wagner",
#     description="Felix is responsible for a variety of construction-related duties on site.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker6 = TeamMembersModel.objects.create(
#     name="Emilia Neumann",
#     description="Emilia ensures high-quality construction work and team collaboration.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker7 = TeamMembersModel.objects.create(
#     name="Leon Schmidt",
#     description="Leon is a versatile Construction Worker skilled in multiple trades.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker8 = TeamMembersModel.objects.create(
#     name="Mia Fischer",
#     description="Mia contributes to construction projects with precision and dedication.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker9 = TeamMembersModel.objects.create(
#     name="Niklas Berger",
#     description="Niklas performs site tasks efficiently, following safety protocols.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )
#
# construction_worker10 = TeamMembersModel.objects.create(
#     name="Lea Hoffmann",
#     description="Lea works as a Construction Worker, ensuring timely and quality results.",
#     position=JobPositions.TitleChoices.CONSTRUCTION_WORKER,
# )