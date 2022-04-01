from django.contrib import admin
from mdeditor.widgets import MDEditorWidget

from .models import *
# Register your models here.


#class PostInline(admin.TabularInline):
    #model = Post

class PostInline(admin.StackedInline):
    model = Post


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    list_filter = ['autor', 'data_cadastro']


class AutorAdmin(admin.ModelAdmin):
    inlines = (PostInline, )


admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AutorAdmin)