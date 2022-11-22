from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import ServerRoom

class ServerRoomForm(forms.ModelForm, forms.Form):

    """
        Jsig attrs for styling


        JSIGNATURE_COLOR = "#000"
        JSIGNATURE_BACKGROUND_COLOR = "#fff"
        JSIGNATURE_DECOR_COLOR (decor-color)
        JSIGNATURE_LINE_WIDTH (lineWidth)
        JSIGNATURE_UNDO_BUTTON (UndoButton)
        JSIGNATURE_RESET_BUTTON (ResetButton)
    """
    signature = JSignatureField(widget = JSignatureWidget(jsignature_attrs = {"color" : "#000"}))

    class Meta:
        model = ServerRoom
        fields = ["first_name", "last_name", "phone_no", "company", "date", "time_in", "time_out", "signature"]
