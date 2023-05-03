from django.forms import BaseInlineFormSet
from django.forms import ValidationError

class BaseOrderFormSet(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return
        if not self.forms[0].has_changed():
            raise ValidationError("Please add at least one item to proceed.")