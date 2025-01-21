from django.urls import path
from .views import GetEmailLayout, UploadImage, UploadEmailConfig, RenderAndDownloadTemplate

urlpatterns = [
    path('getEmailLayout/', GetEmailLayout.as_view()),
    path('uploadImage/', UploadImage.as_view()),
    path('uploadEmailConfig/', UploadEmailConfig.as_view()),
    path('renderAndDownloadTemplate/', RenderAndDownloadTemplate.as_view()),
]
