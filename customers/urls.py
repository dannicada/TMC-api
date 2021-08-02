from django.urls import path, include
from . import views

urlpatterns = [
    path('customer/create/', views.CustomerView.as_view({'post':'create'}), name='create-customer'),
    path('customer/update/<int:pk>/', views.CustomerView.as_view({'put': 'partial_update'}), name='update-customer'),
    path('customer/list/', views.CustomerView.as_view({'get': 'list'}), name='list-customers'),



    # path('team/<int:pk>/',views.RetrieveTeamView.as_view(), name='get-team'),
    # path('team/all/<int:workspace>',views.ListTeamsView.as_view(), name='get-all-teams-in-workspace'),
    # # path('team/delete/<int:pk>/',views.TeamView.as_view(get= 'destroy'), name='delete-team'),
    # path('team/update/<int:pk>/',views.UpdateTeamView.as_view(), name='update-team'),
    # path('team/add-member/<int:pk>/',views.AddMemberToTeamView.as_view(), name='update-team')
]