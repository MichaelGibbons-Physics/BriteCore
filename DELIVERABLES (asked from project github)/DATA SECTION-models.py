from django.db import models

class Insurance(models.Model):
    
    # "riskType" represents the type of risk the insurer is taking. Automobiles, houses, prizes etc.
    # "fieldName" reprsents the name of data the insurer would like to keep track of.
    # "fieldData" reprsents the actual data the insurer would like to keep track of.
    # "fieldType" represents the data type of the given field. text, number, date, or enum.
    
    #EXAMPLES
    #riskType=automobile, fieldName=model, fieldData=Ford Fiesta, fieldType=text
    #                   , fieldName=monthly payment, fieldData=$400/mo, fieldType=number
    #                   ,...
    #                   ,...
    #                   ,...
    
    #riskType=golf tournament, fieldName=first prize, fieldData=$100,000, fieldType=number
    #                        , fieldName=second prize, fieldData=$50,000, fieldType=number
    #                        ,...
    #                        ,...
    #                        ,...
    fieldTypeChoices=(("False","False"),("text","text"),("number","number"),("date","date"))
    enumChoices=(("False","False"),("Bronze","Bronze"),("Silver","Silver"),("Gold","Gold"))
    #this could be changed to a dependent choice map. IE if user selects enum as data type then and only then allow an enumChoice selection
    #but for the purposes of this project I believe true/false should suffice.
    
    riskType=models.CharField(max_length=100)
    fieldName=models.CharField(max_length=100)
    fieldData=models.CharField(max_length=1000)
    fieldType=models.CharField(max_length=100, choices= fieldTypeChoices,default="False")
    enumType=models.CharField(max_length=100,choices=enumChoices,default="False")
    
    if(fieldType=='date'):
        fieldData=models.Datefield
    if(fieldType=='number'):
        fieldData==models.Decimalfield(max_digits=19, decimal_places=10)
    
    
    def __str__(self):
        return self.riskType 