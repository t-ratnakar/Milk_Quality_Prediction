import os
from django.conf import settings
from django.shortcuts import render
import joblib
from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import os



def Training(request):
    # Load the dataset
    df = pd.read_csv('media/milknew.csv')  # Update path to your dataset

    # Encode the target variable
    lb = LabelEncoder()
    df['Grade'] = lb.fit_transform(df['Grade'])

    # Split the data into features and target
    X = df.drop('Grade', axis=1)
    Y = df['Grade']

    # Split into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Train the Random Forest Classifier
    rf = RandomForestClassifier()
    rf.fit(x_train, y_train)

    # Evaluate the model
    y_pred = rf.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Format the accuracy score to display all decimals
    accuracy_exact = f"{accuracy:.10f}"  # Adjust precision as needed (10 decimal places here)

    # Print or use the exact accuracy
    print(f"Exact Accuracy: {accuracy_exact}")

    # Generate the confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    joblib.dump(rf, 'milk_quality_model.pkl')
    cm_image_path = "media/confusion_matrix.png"

    # Plot the confusion matrix
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(os.path.join(settings.MEDIA_ROOT, 'confusion_matrix.png'))

    context={
       'accuracy': accuracy_exact,
        'cm_image_path': cm_image_path
    }

    return render(request, 'result.html', context)




# Load the model
model = joblib.load('milk_quality_model.pkl')

# Mapping of prediction results to labels
RESULT_MAPPING = {
    0: "High",
    1: "Low",
    2: "Moderate"
}

def Prediction(request):
    prediction_label = None
    if request.method == "POST":
        # Collect form data
        pH = float(request.POST['pH'])
        temperature = float(request.POST['temperature'])
        taste = int(request.POST['taste'])
        odor = int(request.POST['odor'])
        fat = int(request.POST['fat'])
        turbidity=int(request.POST['turbidity'])
        colour = int(request.POST['colour'])

        
        

        # Create input array for prediction
        new_data = [[pH,temperature,taste,odor,fat,turbidity,colour]]
        prediction = model.predict(new_data)[0]  # Predict the class

        # Map the prediction to the corresponding label
        prediction_label = RESULT_MAPPING.get(prediction, "Unknown")

    return render(request, 'predict.html', {'prediction': prediction_label})


def ViewDataset(request):
    dataset = os.path.join(settings.MEDIA_ROOT, 'milknew.csv')
    import pandas as pd
    df = pd.read_csv(dataset,nrows=100)
    df = df.to_html(index=None)
    return render(request, 'users/viewData.html', {'data': df})


from django.shortcuts import render, redirect
from .models import UserRegistrationModel
from django.contrib import messages

def UserRegisterActions(request):
    if request.method == 'POST':
        user = UserRegistrationModel(
            name=request.POST['name'],
            loginid=request.POST['loginid'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
            email=request.POST['email'],
            locality=request.POST['locality'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            status='waiting'
        )
        user.save()
        messages.success(request,"Registration successful!")
    return render(request, 'UserRegistrations.html') 


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                data = {'loginid': loginid}
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})



def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})


def index(request):
    return render(request,"index.html")