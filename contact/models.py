from django.db import models

# Create your models here.
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core import blocks

from wagtail.snippets.models import register_snippet


class SocialMediaLink(Orderable):
    platform_name = models.CharField(max_length=100)
    link = models.URLField()
    page = ParentalKey('ContactPage', related_name='social_links', on_delete=models.CASCADE)

    panels = [
        FieldPanel("platform_name"),
        FieldPanel("link")
    ]



class ContactPage(Page):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('email'),
        InlinePanel('social_links', label='Links')
    ]
