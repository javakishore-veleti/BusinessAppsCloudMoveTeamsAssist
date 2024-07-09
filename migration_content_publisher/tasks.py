from celery import shared_task
from django.conf import settings
from .models import Content
import fitz  # PyMuPDF to process PDF
from transformers import pipeline


@shared_task
def process_pdf_task(file_path, content_id):
    try:
        # Extract text from PDF
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()

        # Initialize Hugging Face pipeline for Q&A (Example)
        qa_pipeline = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

        # Process the text as needed for your application
        # This part depends on your use case, just storing the text for now

        # You can now use the text for further processing or storing
        # Example: you can store the text back to the content model
        content = Content.objects.get(id=content_id)
        content.processed_content = text  # Example: if you want to store the text
        content.save()

    except Exception as e:
        # Handle exceptions
        print(f"Error processing PDF: {e}")
