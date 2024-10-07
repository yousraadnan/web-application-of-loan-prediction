from django.db import models

class LoanApplication(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    MARRIED_CHOICES = [
        ('Yes', 'Married'),
        ('No', 'Unmarried'),
    ]

    EDUCATION_CHOICES = [
        ('Graduate', 'Graduate'),
        ('Not Graduate', 'Not Graduate'),
    ]

    SELF_EMPLOYED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    PROPERTY_AREA_CHOICES = [
        ('Urban', 'Urban'),
        ('Semiurban', 'Semiurban'),
        ('Rural', 'Rural'),
    ]

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    married = models.CharField(max_length=10, choices=MARRIED_CHOICES)
    dependents = models.FloatField()
    education = models.CharField(max_length=12, choices=EDUCATION_CHOICES)
    self_employed = models.CharField(max_length=3, choices=SELF_EMPLOYED_CHOICES)
    applicant_income = models.FloatField()
    coapplicant_income = models.FloatField(default=0)
    loan_amount = models.FloatField()
    loan_amount_term = models.FloatField()
    credit_history = models.FloatField()
    property_area = models.CharField(max_length=12, choices=PROPERTY_AREA_CHOICES)

    def __str__(self):
        return f"{self.gender}, {self.married}, {self.dependents}, {self.education}, {self.self_employed}, {self.applicant_income}, {self.coapplicant_income}, {self.loan_amount}, {self.loan_amount_term}, {self.credit_history}, {self.property_area}"
