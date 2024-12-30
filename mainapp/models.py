# mainapp/models.py
from django.db import models

class HeartPrediction(models.Model):
   age = models.IntegerField()
   sex = models.IntegerField(choices=[(1, 'Male'), (0, 'Female')])
   cp = models.IntegerField(choices=[(0, 'Typical Angina'), (1, 'Atypical Angina'), 
                                   (2, 'Non-anginal Pain'), (3, 'Asymptomatic')])
   trestbps = models.IntegerField()
   chol = models.IntegerField() 
   fbs = models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])
   restecg = models.IntegerField(choices=[(0, 'Normal'), (1, 'ST-T Wave Abnormality')])
   thalach = models.IntegerField()
   exang = models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])
   oldpeak = models.FloatField()
   slope = models.IntegerField(choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')])
   ca = models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')])
   thal = models.IntegerField(choices=[(1, 'Normal'), (2, 'Fixed Defect'), (3, 'Reversible Defect')])
   prediction = models.BooleanField()
   probability = models.FloatField(null=True)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f"Prediction for {self.age} year old - {self.get_sex_display()}"