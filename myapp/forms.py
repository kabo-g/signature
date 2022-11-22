from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import ServerRoom

class ServerRoomForm(forms.ModelForm):

    class Meta:
        model = ServerRoom
        fields = "__all__"
