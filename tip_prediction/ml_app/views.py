from django.shortcuts import render
from django.conf import settings
from .forms import PredictionForm
from .ml_model import predict_tip


def home(request):
    prediction = None
    form = PredictionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Order: total_bill, sex, smoker, day, time, size
        data = [
            form.cleaned_data['total_bill'],
            int(form.cleaned_data['sex']),
            int(form.cleaned_data['smoker']),
            int(form.cleaned_data['day']),
            int(form.cleaned_data['time']),
            int(form.cleaned_data['size']),
        ]
        prediction = predict_tip(data)

    return render(request, 'ml_app/home.html', {'form': form, 'prediction': prediction})


def landing(request):
    """Simple landing page with navigation to the predictor."""
    return render(request, 'ml_app/landing.html')
