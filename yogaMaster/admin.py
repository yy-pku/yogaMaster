from django.contrib import admin

# Register your models here.
from .models import YogaImage
from .models import Result
from .models import StudyRecord
from .models import User
from .models import Favorites


admin.site.register(User)
admin.site.register(YogaImage)
admin.site.register(Result)
admin.site.register(StudyRecord)
admin.site.register(Favorites)