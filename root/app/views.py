from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Insurance
from .serializers import InsuranceSerializer
from . import forms

class InsuranceView(viewsets.ModelViewSet):
    serializer_class=InsuranceSerializer
    queryset=Insurance.objects.all()  
    def homeview(request):
        return render(request,'app/main.html')

class InsuranceAutomobilesView(viewsets.ModelViewSet):
    queryset=Insurance.objects.filter(riskType="Automobile")
    serializer_class=InsuranceSerializer

class InsuranceTradingCardsView(viewsets.ModelViewSet):
    queryset=Insurance.objects.filter(riskType="Trading Cards")
    serializer_class=InsuranceSerializer
    
def InsuranceFormView(request):
    if request.method=='POST':
        form=forms.InsuranceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/main/')           
    else:
        form=forms.InsuranceForm()
    return render(request,'app/form.html',{'form':form})
