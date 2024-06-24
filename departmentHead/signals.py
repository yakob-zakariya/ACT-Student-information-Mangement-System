from school.models import Section,Section_teacher,Batch_course
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Batch_course)
def create_section_teacher(sender, instance, created, **kwargs):
    if created:
        # Get all sections for the batch
        sections = Section.objects.filter(batch=instance.batch)
        for section in sections:
            Section_teacher.objects.create(
                course=instance.course,
                semester=instance.semester,
                section=section,
                teacher=None  # Set to None initially
            )