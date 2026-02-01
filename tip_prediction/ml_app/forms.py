from django import forms


class PredictionForm(forms.Form):
    total_bill = forms.FloatField(label='Total bill', min_value=0, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'e.g. 20.50'}))
    sex = forms.ChoiceField(label='Sex', choices=[(0,'Female'),(1,'Male')], widget=forms.Select(attrs={'class':'form-control'}))
    smoker = forms.ChoiceField(label='Smoker', choices=[(0,'No'),(1,'Yes')], widget=forms.Select(attrs={'class':'form-control'}))
    day = forms.ChoiceField(label='Day', choices=[(0,'Thur'),(1,'Fri'),(2,'Sat'),(3,'Sun')], widget=forms.Select(attrs={'class':'form-control'}))
    time = forms.ChoiceField(label='Time', choices=[(0,'Dinner'),(1,'Lunch')], widget=forms.Select(attrs={'class':'form-control'}))
    size = forms.IntegerField(label='Party size', min_value=1, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'e.g. 2'}))

