from django.contrib import admin
from .models import Validation
from .models import Suggestion
from .models import EventType
from .models import EventTag
from .models import SuggestionOption
from .models import ImageTag
from .models import SuggestionImages
from django.utils.safestring import mark_safe


admin.site.register(Validation)
admin.site.register(Suggestion)
admin.site.register(EventType)
admin.site.register(EventTag)
admin.site.register(ImageTag)

@admin.register(SuggestionOption)
class SuggestionImagesAdmin(admin.ModelAdmin):
    list_display = "id", "event_type", "thumbnail",
    list_filter = "event_type",

    def thumbnail(self, si):
        x = "<img height=\"100\" src=%s />"%si.answer_image.url
        return mark_safe(x)
