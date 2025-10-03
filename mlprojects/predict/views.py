import pickle
from django.shortcuts import render, redirect
from django.contrib import messages

# Load model and vectorizer
model = pickle.load(open('predict/model.pkl', 'rb'))
vectorizer = pickle.load(open('predict/vectorizer.pkl', 'rb'))

def predict_spam(request):
    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        
        if not message:
            messages.error(request, 'Please enter some email text.')
            return redirect('predict_spam')  # Or use render if you prefer

        try:
            vectorized = vectorizer.transform([message])
            prediction = model.predict(vectorized)[0]
            if prediction == 1:
                messages.success(request, 'The message is Spam.')
            else:
                messages.success(request, 'The message is Not Spam.')
        except Exception as e:
            messages.error(request, f'Error during prediction: {str(e)}')

    return render(request, 'predict/form.html')
