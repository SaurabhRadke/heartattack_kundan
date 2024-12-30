# mainapp/views.py
from django.shortcuts import render
from .forms import HeartPredictionForm
from .models import HeartPrediction
import joblib
import pandas as pd
import numpy as np

# views.py - update preprocess_user_input function
# views.py preprocess_user_input function
# views.py preprocess function
def preprocess_user_input(user_input):
    try:
        features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                   'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        input_df = pd.DataFrame([user_input])[features]
        
        scaler = joblib.load('models/scaler.pkl')
        X_scaled = scaler.transform(input_df)
        return pd.DataFrame(X_scaled, columns=features)
        
    except Exception as e:
        print(f"Preprocessing error: {str(e)}")
        raise e

def predict_heart_disease(request):
   if request.method == 'POST':
       form = HeartPredictionForm(request.POST)
       if form.is_valid():
           try:
               print("Form Data:", form.cleaned_data)
               input_data = form.cleaned_data
               
               prediction_record = HeartPrediction(
                   age=input_data['age'],
                   sex=input_data['sex'],
                   cp=input_data['cp'],
                   trestbps=input_data['trestbps'],
                   chol=input_data['chol'],
                   fbs=input_data['fbs'],
                   restecg=input_data['restecg'],
                   thalach=input_data['thalach'],
                   exang=input_data['exang'],
                   oldpeak=input_data['oldpeak'],
                   slope=input_data['slope'],
                   ca=input_data['ca'],
                   thal=input_data['thal'],
                   prediction=False,
                   probability=0.0
               )
               
               preprocessed_data = preprocess_user_input(input_data)
               model = joblib.load('models/best_randomforest_model.pkl')
               prediction = model.predict(preprocessed_data)[0]
               probability = model.predict_proba(preprocessed_data)[0][1]
               
               prediction_record.prediction = bool(prediction)  
               prediction_record.probability = float(probability)
               prediction_record.save()
               
               print(f"Prediction: {prediction}, Probability: {probability}")
               
               return render(request, 'mainapp/result.html', {
                   'prediction': prediction_record,
                   'form_data': input_data
               })
               
           except Exception as e:
               print(f"Error: {str(e)}")
               form.add_error(None, f"Error: {str(e)}")
   else:
       form = HeartPredictionForm()
   
   return render(request, 'mainapp/predict.html', {'form': form})

def prediction_list(request):
   predictions = HeartPrediction.objects.all().order_by('-created_at')
   return render(request, 'mainapp/prediction_list.html', {'predictions': predictions})