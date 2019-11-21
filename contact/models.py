from django.db import models

# Create your models here.
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core import blocks

from wagtail.snippets.models import register_snippet


class SocialMediaLink(Orderable):
    PLATFORM_CHOICES = (
        ('at', 'Email'),
        ('github', 'Github'),
        ('stack-overflow', 'Stack Overflow'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter')
    )
    platform_name = models.CharField(max_length=100, choices=PLATFORM_CHOICES)
    link = models.CharField(max_length=280)
    handle = models.CharField(max_length=100, null=True)
    page = ParentalKey('ContactPage', related_name='social_links', on_delete=models.CASCADE)

    panels = [
        FieldPanel("platform_name"),
        FieldPanel("link"),
        FieldPanel("handle")
    ]

    @property
    def icon_class(self):
        return f'fa-{self.platform_name.lower()}'



class ContactPage(Page):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('email'),
        InlinePanel('social_links', label='Links')
    ]
