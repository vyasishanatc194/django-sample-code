from django.urls import path
from model_catalog.views import ManageModelCatalog, ExportModelCatalog, \
    FetchModelCatalogProducts, ReprocessModelCatalog

app_name = 'model_catalog'

urlpatterns = [
    path('', ManageModelCatalog.as_view(), name="model_catalog_home"),
    path('download/', ExportModelCatalog.as_view(), name="download_model_catalog"),
    path('<int:id>/products/', FetchModelCatalogProducts.as_view(), name="model_catalog_products"),
    path('reprocess-model-catalog/<int:category_id>/', ReprocessModelCatalog.as_view(), name="reprocess_model_catalog"),
]