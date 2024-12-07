from django import forms
from .models import blog

class blogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields= '__all__'


from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # CKEditor Widget

    class Meta:
        model = BlogPost
        fields = ['title', 'content']
