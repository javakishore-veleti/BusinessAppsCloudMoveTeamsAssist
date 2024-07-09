import os

from django.http import JsonResponse
from django.shortcuts import render

from .models import Content
from .tasks import process_pdf_task


def upload_pdf(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_name = file.name
        file_path = os.path.join(os.path.expanduser('~/BusinessAppsCloudMoveTeamsAssist/UploadedFiles/'), file_name)

        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        content = Content.objects.create(
            content_type='pdf',
            content_author='AWS',  # Example, adjust as necessary
            content_author_sub_type='service',  # Example, adjust as necessary
            content_feature='feature',  # Example, adjust as necessary
            content_sub_feature='sub_feature',  # Example, adjust as necessary
            content_sub_feature_level_1='sub_feature_level_1',  # Example, adjust as necessary
            content_sub_feature_level_2='sub_feature_level_2',  # Example, adjust as necessary
            content_sub_feature_level_3='sub_feature_level_3',  # Example, adjust as necessary
            content_sub_feature_level_4='sub_feature_level_4',  # Example, adjust as necessary
            content_sub_feature_level_5='sub_feature_level_5',  # Example, adjust as necessary
            content_keywords={},  # Example, adjust as necessary
            content_file_path=file_path,
            content_file_path_type='local_file_system'  # Example, adjust as necessary
        )

        # Start the asynchronous task to process the PDF
        process_pdf_task.delay(file_path, content.id)

        return JsonResponse({'message': 'File uploaded and processing started', 'file_path': file_path})

    return render(request, 'upload_pdf.html')
