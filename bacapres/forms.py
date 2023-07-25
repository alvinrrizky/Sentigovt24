from django import forms
from django.forms import inlineformset_factory
from .models import Bacapres

class BacapresForm(forms.ModelForm):

    class Meta:
        model = Bacapres
        fields = ('name', 'desc', 'keyword', 'avatar')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].required = False

# class BacapresKeywordForm(forms.ModelForm):

#     class Meta:
#         model = BacapresKeyword
#         fields = '__all__'

# KeywordFormSet = inlineformset_factory(
#     Bacapres, BacapresKeyword, form=BacapresKeywordForm, extra = 3,
#     can_delete=True
# )
