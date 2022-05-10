from django.urls import path
from .views import ItemList, BoxList, ItemCreateView, BoxCreateView, BoxDetail

urlpatterns = [

    path('', ItemList.as_view(), name='items'),
    path('boxes/', BoxList.as_view(), name='boxes'),
    path('item/add/', ItemCreateView.as_view(), name='item-add'),
    path('boxes/add/', BoxCreateView.as_view(), name='box-add'),
    path('boxes/<int:pk>/', BoxDetail.as_view(), name='box-detail'),


]