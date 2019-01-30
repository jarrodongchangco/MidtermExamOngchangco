from django.forms import ModelForm
from .models import Position



class PositionForm(ModelForm):
    class Meta :
        model = Position
        fields = ['name', 'description']


#barrier
# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         # exclude = ('id',)
#         fields = ['content']
