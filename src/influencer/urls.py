from django.urls import path
from .views import test_view, campaign_list, profile_create, influencers_assignment,campaign_detail, memer_assignment

app_name = 'influencer'

urlpatterns = [
    path('test/', test_view, name='create-campaign'),
    path('list/', campaign_list, name='campaign-list'),
    path('profile/', profile_create, name='create-profile'),
    path('task_list/', influencers_assignment, name='assignments-list'), 
    path('detail/', campaign_detail, name='campaign-detail'),
    path('memer/', memer_assignment, name='memer-list'),
]