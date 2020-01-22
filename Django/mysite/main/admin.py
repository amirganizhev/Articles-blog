from django.contrib import admin
from .models import Tutorial
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		("Заголок/Дата", {"fields": ["tutorial_title", "tutorial_published"]}),
		("Содержание", {"fields":["tutorial_content"]})
	]

admin.site.register(Tutorial, TutorialAdmin)

