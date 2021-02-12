from django.urls import path
from home.views import HomeView, UploadCategory, ExportCategoryToXlsx, \
    LogView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('category-upload/', UploadCategory.as_view(), name='upload_category'),
    path('download-category/', ExportCategoryToXlsx.as_view(), name='download_categories'),
    path('logs/', LogView.as_view(), name='logs')
]
