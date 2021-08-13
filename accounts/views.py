from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth

from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string


from .models import Account
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone_no = request.POST['phone']
            # password and confirm password is same(checked in forms.py)
            password = request.POST['password']

            # create account with provided from form
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name,
                email=email, phone=phone_no, password=password
            )

            # Send email
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            mail_message = render_to_string('account_verification_email.html', {
                'domain': current_site, 'uid': uid,
                'token': token, 'user': user,
            })
            mail = EmailMessage(
                subject='AmazinZone : Activate your account',
                body=mail_message, to=[email])
            mail.send()
            messages.success(request, 'Email with verification link has been sent to ' + email +
                             '\nPlease activate your account if not done yet.')
            return redirect('/accounts/login/?command=verification&email='+email)
        else:
            # form not valid
            messages.error(request, 'Signup failed')
    else:
        # Form has not been submited(first visit)
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        print(request.GET)
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
    return render(request, 'login.html')


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('homepage')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()  # pk
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account Activated.')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Something went wrong. Please try again.')
        return redirect('accounts:register')


