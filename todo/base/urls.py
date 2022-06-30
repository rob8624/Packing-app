from django.urls import path
from .views import ItemList, BoxList, ItemCreateView, BoxCreateView, BoxDetail
from . import views


urlpatterns = [

    path('', ItemList.as_view(), name='items'),
    path('boxes/', BoxList.as_view(), name='boxes'),
    path('item/add/', ItemCreateView.as_view(), name='item-add'),
    path('boxes/add/', BoxCreateView.as_view(), name='box-add'),
    path('boxes/<int:pk>/', BoxDetail.as_view(), name='box-detail'),
    path('add-item/', views.add_item, name='add-item'),
    path('delete_item/<int:pk>/', views.delete_item, name='item-delete'),
    path('search-items/', views.search_items, name='search-items'),
    path('pack-item/<int:pk>', views.pack_item, name='pack-item'),
    path('unpack-item/<int:pk>', views.unpack_item, name='unpack-item'),


]