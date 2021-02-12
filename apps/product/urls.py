from django.urls import path
from product.views import UploadProducts, ExportProductsToXlsx, \
    UploadProductAspects, ExportProductAspectToXlsx, UploadAggregationModelSet, \
    ExportAggregationModelSet

app_name = 'product'
urlpatterns = [
    path('upload/', UploadProducts.as_view(), name="upload_product"),
    path('download-products/', ExportProductsToXlsx.as_view(), name="download_products"),
    path('aspect-upload/', UploadProductAspects.as_view(), name="upload_product_aspects"),
    path('download-aspects/', ExportProductAspectToXlsx.as_view(), name="download_product_aspects"),
    path('aggregation-model-set/', UploadAggregationModelSet.as_view(), name="upload_aggregation_model_set"),
    path('download-aggregation-model-set/', ExportAggregationModelSet.as_view(), name="download_aggregation_model_set"),
]
