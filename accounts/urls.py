from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name="accounts"),
    path('register/',views.RegistrationView.as_view(), name="register"),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("password-reset-complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name="password_reset_complete")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)