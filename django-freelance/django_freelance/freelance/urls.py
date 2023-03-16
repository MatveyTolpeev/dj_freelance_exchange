from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    # path('auth/', include('djoser.urls')),
    path('/auth', include('rest_framework_social_oauth2.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtai_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token', obtain_auth_token, name='token'),


    path('tickets/retrieve/<int:pk>', TicketRetrieveView.as_view()),
    path('tickets/update/<int:pk>', TicketUpdateView.as_view()),
    path('tickets/all', TicketListView.as_view()),
    path('tickets/new', TicketCreateView.as_view()),

    path('executors/retrieve/<int:pk>', ExecutorRetrieveView.as_view()),
    path('executors/update/<int:pk>', ExecutorUpdateView.as_view()),
    path('executors/all', ExecutorListView.as_view()),
    path('executors/new', ExecutorCreateView.as_view()),

    path('customers/retrieve/<int:pk>', CustomerRetrieveView.as_view()),
    path('customers/update/<int:pk>', CustomerUpdateView.as_view()),
    path('customers/all', CustomerListView.as_view()),
    path('customers/new', CustomerCreateView.as_view()),

    path('services/retrieve/<int:pk>', ServiceRetrieveView.as_view()),
    path('services/update/<int:pk>', ServiceUpdateView.as_view()),
    path('services/all', ServiceListView.as_view()),
    path('services/new', ServiceCreateView.as_view()),

    path('orders/retrieve/<int:pk>', OrderRetrieveView.as_view()),
    path('orders/update/<int:pk>', OrderUpdateView.as_view()),
    path('orders/all', OrderListView.as_view()),
    path('orders/new', OrderCreateView.as_view()),

    path('tags/retrieve/<int:pk>', TagRetrieveView.as_view()),
    path('tags/update/<int:pk>', TagUpdateView.as_view()),
    path('tags/all', TagListView.as_view()),
    path('tags/new', TagCreateView.as_view()),

    path('orderings/retrieve/<int:pk>', OrderingRetrieveView.as_view()),
    path('orderings/update/<int:pk>', OrderingUpdateView.as_view()),
    path('orderings/all', OrderingListView.as_view()),
    path('orderings/new', OrderingCreateView.as_view()),

    path('messages/retrieve/<int:pk>', MessageRetrieveView.as_view()),
    path('messages/update/<int:pk>', MessageUpdateView.as_view()),
    path('messages/all', MessageListView.as_view()),
    path('messages/new', MessageCreateView.as_view()),

    path('reviews/retrieve/<int:pk>', ReviewRetrieveView.as_view()),
    path('reviews/update/<int:pk>', ReviewUpdateView.as_view()),
    path('reviews/all', ReviewListView.as_view()),
    path('reviews/new', ReviewCreateView.as_view()),

    path('authorings/retrieve/<int:pk>', AuthoringRetrieveView.as_view()),
    path('authorings/update/<int:pk>', AuthoringUpdateView.as_view()),
    path('authorings/all', AuthoringListView.as_view()),
    path('authorings/new', AuthoringCreateView.as_view()),
]
