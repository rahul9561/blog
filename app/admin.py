from django.contrib import admin
from .models import BlogPost
from ckeditor.widgets import CKEditorWidget
from django import forms


class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # Use CKEditor widget for 'content'

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm


admin.site.register(BlogPost, BlogPostAdmin)
