from django.urls import path
from . import views
# URL PATTERNS

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile-update/', views.profile_update, name="profile-update"),

    path('loan/', views.loan_book, name="loan-book"),
    path('loan-return/', views.loan_return, name="loan-return"),

    path('members/', views.MemberListView.as_view(), name="member-list"),
    path('members/<int:pk>', views.MemberDetailView.as_view(), name="member-detail"),

    path('outstanding/', views.OutstandingListView.as_view(),
         name="outstanding-list"),
    # path('loans/<int:pk>', views.MemberDetailView.as_view(), name="member-detail"),

]
