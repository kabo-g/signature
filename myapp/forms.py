from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import ServerRoom

class ServerRoomForm(forms.ModelForm, forms.Form):


    signature = JSignatureField(widget = JSignatureWidget(jsignature_attrs = {"color" : "#000"}))

    class Meta:
        model = ServerRoom
        fields = ["first_name", "last_name", "phone_no", "company", "date", "time_in", "time_out", "signature"]
