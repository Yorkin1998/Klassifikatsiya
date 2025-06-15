from django.shortcuts import render
from .forms import TextInputForm
from .utils import classify_text
from .models import TextInput

def classify_view(request):
    categories = [
        "O'zbekiston", "Jamiyat", "Dunyo", "Iqtisodiyot", "Siyosat", 
        "Texnologiya", "Madaniyat", "Avto", "Sport", "Foto", 
        "Salomatlik", "Qonunchilik", "Jinoyat", "Ayollar", "Pazandachilik"
    ]
    
    form = TextInputForm()
    result = None

    if request.method == "POST":
        form = TextInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            classification = classify_text(text)
            
            # Transform the nested classification results
            result = [
                {
                    'label': item['label'], 
                    'score': item['score'] * 100
                } 
                for item in classification[0]  # Access the first (and only) list in the outer list
            ]
            
            # Sort results by score in descending order
            result.sort(key=lambda x: x['score'], reverse=True)
            
            # Ma'lumotlarni saqlash (ixtiyoriy)
            TextInput.objects.create(text=text, classification_result=result)

    return render(request, 'classification/classify.html', {
        'form': form, 
        'result': result,
        'categories': categories
    })