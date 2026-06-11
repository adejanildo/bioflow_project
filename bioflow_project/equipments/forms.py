from django import forms
from .models import Equipment, EquipmentFailure
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ['created_at','updated_at']
        widgets = {
            'acquisition_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'maintenance_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }
    def __init__(self,*a,**k):
        super().__init__(*a,**k)
        for n,f in self.fields.items():
            if 'date' not in n: f.widget.attrs['class']='form-control'
class FailureForm(forms.ModelForm):
    class Meta:
        model = EquipmentFailure
        fields = ['description']
    def __init__(self,*a,**k):
        super().__init__(*a,**k)
        self.fields['description'].widget.attrs['class']='form-control'
