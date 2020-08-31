from django.contrib.flatpages import views as flatpages_views
from django.urls import path

from . import views

app_name = 'trading'

urlpatterns = [
    path('', views.IndexView.as_view(), name='list'),
    path('condiciones/', flatpages_views.flatpage, {'url': '/condiciones-permutas/'}, name='conditions'),

    path('crear/', views.TradeOfferAddView.as_view(), name='offer_create'),
    path('ofertas/<int:pk>/editar/', views.TradeOfferEditView.as_view(), name='offer_edit'),
    path('ofertas/<int:pk>/eliminar/', views.TradeOfferDeleteView.as_view(), name='offer_delete'),
    path('ofertas/<int:pk>/responder/', views.TradeOfferAnswerCreateView.as_view(), name='answer_create'),
    path('ofertas/<int:pk>/', views.TradeOfferDetailView.as_view(), name='offer_detail'),

    path('respuestas/<int:pk>/', views.TradeOfferAnswerDetailView.as_view(), name='answer_detail'),
    path('respuestas/<int:pk>/aceptar/', views.TradeOfferAnswerAcceptView.as_view(), name='answer_accept'),
    path('respuestas/<int:pk>/editar/', views.TradeOfferAnswerEditView.as_view(), name='answer_edit'),
    path('respuestas/<int:pk>/eliminar/', views.TradeOfferAnswerDeleteView.as_view(), name='answer_delete'),

    path('intercambio/<int:pk>/completado/', views.ChangeCompletedView.as_view(), name='change_completed'),
    path('intercambio/<int:pk>/', views.ChangeProcessView.as_view(), name='change_process'),

    path('gestion/', views.ManagementListView.as_view(), name='management_list'),
]
