Keywords: 

- ORM Classes
- Django 
- Django REST Framework
- Vue.js
- Axios
- AWS Lambda
- Zappa

--- 

HOW TO DEPLOY THIS PROJECT:

The app is fully scripted! Please just click the following link to see the project!

####https://h1rrlt221e.execute-api.us-west-2.amazonaws.com/dev/main/

---

---

#Hello! Thank you so much for your time.

My name is Michael Gibbons and I am applying for the full stack developer position at BriteCore. In order to get to this project I decoded the ascii array, then simply copy-pasted the Fernet encrption code into a python file (though the code goes off the screen you can still copy-paste) then fixed the typos to get to this application project. 

---

##Insurance Database Managment Project

This project is broken down into 3 distict sections. The Data section, backend, and frontend. Therefore this readme file is broken down into those 3 sections.

###Data

The purpose of this section is to make a generic data structure which insurers can use to keep track of an arbitrarily distict item/contact. The steps taken to complete this were as follows:

- Create a new Djengo project
- Create a new Djengo app 
- In the models.py file, a new model class was created inheriting from a Djengo model template. (**Please see the attached ERD**)
- This child class takes the following user data:
	- "riskType" represents the type of risk the insurer is taking. Automobiles, houses, prizes etc.
	- "fieldName" reprsents the name of data the insurer would like to keep track of.
	- "fieldData" reprsents the actual data the insurer would like to keep track of.
	- "fieldType" represents the data type of the given field. text, number, date, or enum


This completes the actual data structure, using the data structure moves us into the backend.

###Backend

The purpose of this section is to create a REST API that will serialize the data from our insurance contract database into JSON. This allows for easy communication between applications.
The steps taken to complete this were as follows:

- Include the Dejango REST Framework in the settings.py file
- Create a serializer class for the Insurance Model
- Create class based View functions (viewsets.ModelViewSet) to query specific data to attach to the endpoints
- Create the endpoints attached to the View functions 
	- The first endpoint "all_endpoint" runs a view function which returns the entire database.
	- The second endpoint "single\_endpoint" runs a view function which returns database entries of a single riskType. The  single riskType was hard coded in as "RiskTypeExample\_Automobiles". This could easily be changed to a user entered field, but for demonstration purposes, the example should suffice.


This completes the API. Now by going to the endpoints one should be able to query the database and recieve serialized JSON data of the Insurance database. This was tested using chrome tools and a API checking tool called "postman".




###Frontend

The purpose of this section is to gather data from the backend, and present it to the user in a friendly format.

To do this, Vue and a Http query tool "axios" were used to get the data from the premade endpoints. Then query functions were made in order to sort though the database by risk type.
A data template function was made in order to generate a form to display the data.

A model form was then created in order to let the user input custom data, taking note to add the crsf token to prevent malicious interception. Once the user inputs valid information pertinant to the Djengo model, the user can submit the form to the database. At which point it is added to the "all" endpoint.

####css

No css framework was used, instead I wrote custom css for this application. But I could easily adapt to whatever css framework is commonly used.

##Hosting

The app is hosted using AWS using an S3 bucket to serve the static files and zappa to deploy the Django project. In order to host a Django app using AWS the following steps must be completed,

- Create an S3 bucket
- Configure the bucket for public access
- Create an AWS user group, user, and policy

Then once this step is completed one may do the following steps to deploy the Django app onto AWS

- Create a virtual envoirnment
- Install the packages needed for project within the virtual enviornment(listed in the req.txt file)
- Install zappa
- Zappa init, in order to make a new project using the preconfigured S3 bucket
- Zappa deploy, in order to host the project
- Configure settings.py for AWS usage(security credientials, static paths, etc)


There were a **myriad** of technical issues with this section. But once they have been completed, one can simply apply the same settings for different projects and modify them as needed.
