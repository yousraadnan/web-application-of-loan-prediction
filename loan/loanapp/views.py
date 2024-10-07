from django.shortcuts import render
import joblib
import pandas as pd
from .models import LoanApplication
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')
def services(request):
    return  render(request,'services.html')

def about(request):
    return render(request,'about.html')

@csrf_exempt
def loan_predict(request):
    if request.method == 'POST':
        # Load the model and encoders
        gbc = joblib.load(r'C:\Users\smz\PycharmProjects\pythonProject4\loan\loanapp\loan_model.pkl')
        label_encoders = joblib.load(r'C:\Users\smz\PycharmProjects\pythonProject4\loan\loanapp\label_encoders.pkl')
        y_le = joblib.load(r'C:\Users\smz\PycharmProjects\pythonProject4\loan\loanapp\target_encoder.pkl')

        # Get data from POST request
        data = {
            'Gender': request.POST.get('Gender'),
            'Married': request.POST.get('Married'),
            'Dependents': request.POST.get('Dependents'),
            'Education': request.POST.get('Education'),
            'Self_Employed': request.POST.get('Self_Employed'),
            'ApplicantIncome': float(request.POST.get('ApplicantIncome')),
            'CoapplicantIncome': float(request.POST.get('CoapplicantIncome') or 0),  # Default to 0 if None
            'LoanAmount': float(request.POST.get('LoanAmount')),
            'Loan_Amount_Term': float(request.POST.get('loan_term')),
            'Credit_History': float(request.POST.get('credit_history')),
            'Property_Area': request.POST.get('property_area'),
        }

        # Save the data to the LoanApplication model
        loan_application = LoanApplication(
            gender=data['Gender'],
            married=data['Married'],
            dependents=data['Dependents'],
            education=data['Education'],
            self_employed=data['Self_Employed'],
            applicant_income=data['ApplicantIncome'],
            coapplicant_income=data['CoapplicantIncome'],
            loan_amount=data['LoanAmount'],
            loan_amount_term=data['Loan_Amount_Term'],
            credit_history=data['Credit_History'],
            property_area=data['Property_Area'],
        )
        loan_application.save()  # Save the application to the database

        # Create DataFrame with explicit column order
        feature_order = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                         'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                         'Loan_Amount_Term', 'Credit_History', 'Property_Area']

        new_data = pd.DataFrame([[data[col] for col in feature_order]], columns=feature_order)

        # Encode categorical features
        for col in feature_order:
            if col in label_encoders:
                le = label_encoders[col]
                new_data[col] = le.transform(new_data[col])

        # Make predictions
        predictions = gbc.predict(new_data)

        # Decode predictions
        predicted_status = y_le.inverse_transform(predictions)[0]
        return JsonResponse({'status': predicted_status})

    return render(request, 'apply for loan.html')

