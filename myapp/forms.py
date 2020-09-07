from django.forms import ModelForm, TextInput, EmailInput
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widget = dict(NomPrenom=TextInput(attrs={'class': 'post-form'}), Email=EmailInput(attrs={'class': 'post-form'}),
                      sujet=TextInput(attrs={'class': 'post-form'}), message=TextInput(attrs={'class': 'post-form'}))