from transformers import pipeline

# Klassifikatsiya uchun pipeline-ni tayyorlash
pipe = pipeline("text-classification", model="abdumalikov/bert-finetuned-uzbek-text-classification", top_k=None)

def classify_text(text):
    return pipe(text)