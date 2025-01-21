from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from .models import EmailTemplate
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

# Endpoint to get email layout
class GetEmailLayout(APIView):
    def get(self, request):
        try:
            data = {
                "title": "Sample Title",
                "content": "This is sample content for the email builder.",
                "footer": "Sample Footer Text",
                "image_url": "https://via.placeholder.com/600x200",
            }
            rendered_html = render_to_string('layout.html', data)
            return JsonResponse({"layout": rendered_html})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# Endpoint to upload images
class UploadImage(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_obj = request.data['file']
        file_path = default_storage.save(file_obj.name, file_obj)
        file_url = default_storage.url(file_path)
        return Response({"url": file_url})

# Endpoint to save email configuration
class UploadEmailConfig(APIView):
    def post(self, request):
        data = request.data
        template = EmailTemplate.objects.create(
            title=data['title'],
            content=data['content'],
            footer=data['footer'],
            image_url=data.get('image_url', '')
        )
        return Response({"id": template.id})

# Endpoint to render and download template
class RenderAndDownloadTemplate(APIView):
    def post(self, request):
        data = request.data
        rendered_html = render_to_string('layout.html', data)
        return Response({"rendered_html": rendered_html})
