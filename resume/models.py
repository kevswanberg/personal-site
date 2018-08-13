from django.db import models
from django.contrib.postgres.fields import DateRangeField


# Create your models here.
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core import blocks

from wagtail.snippets.models import register_snippet


class ResumeExperience(Orderable):
    title = models.CharField(max_length=100)
    description = RichTextField()
    when = DateRangeField()
    page = ParentalKey('ResumePage', related_name='experience', on_delete=models.CASCADE)


    panels = [
        FieldPanel("title"),
        FieldPanel("when"),
        FieldPanel("description")
    ]



class ResumePage(Page):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    about = RichTextField()
    interests = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('about'),
        FieldPanel('interests'),
        InlinePanel('experience', label='Experience')
    ]


# Create your models here.
