
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel



from wagtail.core import blocks


class HomePage(Page):
    info = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('info', classname='full')
    ]
