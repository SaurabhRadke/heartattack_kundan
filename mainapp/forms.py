from django import forms

class HeartPredictionForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=[(1, 'Male'), (0, 'Female')])
    cp = forms.ChoiceField(choices=[(0, 'Typical Angina'), (1, 'Atypical Angina'), (2, 'Non-anginal Pain'), (3, 'Asymptomatic')])
    trestbps = forms.IntegerField(label='Resting Blood Pressure')
    chol = forms.IntegerField(label='Cholesterol')
    fbs = forms.ChoiceField(choices=[(1, 'Yes'), (0, 'No')], label='Fasting Blood Sugar > 120 mg/dl')
    restecg = forms.ChoiceField(choices=[(0, 'Normal'), (1, 'ST-T Wave Abnormality')], label='Resting ECG')
    thalach = forms.IntegerField(label='Max Heart Rate')
    exang = forms.ChoiceField(choices=[(1, 'Yes'), (0, 'No')], label='Exercise Induced Angina')
    oldpeak = forms.FloatField(label='ST Depression')
    slope = forms.ChoiceField(choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')])
    ca = forms.ChoiceField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')], label='Number of Major Vessels')
    thal = forms.ChoiceField(choices=[(1, 'Normal'), (2, 'Fixed Defect'), (3, 'Reversible Defect')])