from django.urls import path
from . import views

urlpatterns=[

    path('',views.ProductInfo.as_view(),name='product_info'),
    path('new_product/',views.Newproduct.as_view(),name='new_product'),
    path('new_reviews/',views.NewReview.as_view(),name='review')
]