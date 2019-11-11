from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    info = models.CharField(max_length=140)
    
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='home_pages'
    )

    content_panels = Page.content_panels + [
        FieldPanel('info'),
        ImageChooserPanel('banner_image')
    ]
