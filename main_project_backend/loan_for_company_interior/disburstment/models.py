from django.db import models
from admin_app.models import User
from loan_sanctioning.models import Loan


class Defaulter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Defaulters')
    default_amount = models.FloatField(default=0, blank=True)
    pending_since_date = models.DateField(default="2000-12-12", blank=True)


INSTALLMENT_CHOICES = [('pending','pending'),('unpaid','unpaid')]


class Installment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='Installments')
    remaining_amount = models.FloatField(default=0, blank=True)
    installment_no = models.IntegerField(default=0, blank=True)
    monthly_installment_amount = models.FloatField(default=0, blank=True)
    installment_expected_date = models.DateField(default="2000-12-12", blank=True)
    installment_paid_date = models.DateField(default="2000-12-12", blank=True)
    penalty_amount = models.FloatField(default=0, blank=True)
    status = models.CharField(max_length=100, blank=True, choices=INSTALLMENT_CHOICES, default='pending')

PAYMENT_CHOICES = [('online','online'),('cash on','cash on')]


DISBURSEMENT_CHOICES = [('vender a/c', 'vendor a/c'),('personal a/c','personal a/c')]


class Disbursement(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE, related_name='Disbursements')
    insurance_doc = models.FileField(upload_to='media/customer/disbursement', default=0, blank=True)
    payment_mode = models.CharField(max_length=250, default=0, blank=True, choices=PAYMENT_CHOICES)
    net_disbursed_amount = models.FloatField(default=0, blank=True)
    disbursed_to_account_no = models.CharField(max_length=25, default=0, blank=True)
    receipt_doc = models.FileField(upload_to='customer/disbursement', default=0, blank=True)
    status = models.CharField(max_length=250, default=0, blank=True, choices=DISBURSEMENT_CHOICES)
    response_timestamp = models.DateTimeField(auto_now=True, blank=True)