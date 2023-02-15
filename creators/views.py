from django.shortcuts import render, redirect, reverse
from .models import User
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.conf import settings
import threading

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_activation_email(request):
    email = request.POST['email']
    user = User.objects.filter(email= email)
    if len(user) == 0:
        messages.error(request, 'No account exists for this email')
        return redirect('home')
    else:
        current_site = get_current_site(request)
        email_subject = "You're Almost There! Confirm Email"
        email_body = render_to_string('creators/activate.html', {
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
            'token': generate_token.make_token(user[0])
        })

        Email = EmailMessage(subject=email_subject, 
                    body=email_body, 
                    from_email= settings.EMAIL_FROM_USER,
                    to=[email]
                    )
        EmailThread(Email).start()
        messages.success(request, 'Email sent successfully')
        return redirect('home')

@csrf_protect
def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Inavalid Email or Password')
            return redirect("login")
    else:
        return render(request, 'creators/registration.html', {'title':'Welcome LogIn Here!', 'login_status':'active', 'side_status':'right'})

@csrf_protect
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        country = request.POST['country']
        dob = request.POST['dob']

        if User.objects.filter(email= email).exists():
            messages.info(request, 'Already have an account?Please login')
            return redirect('login')
        else:
            user = User.objects.create_user(email=email, password=password, country=country, dob=dob)
            user.save()
            messages.success(request, 'Your account is created. Please log in now')
            return redirect('login')
    else:
        return render(request, 'creators/registration.html', {'title':'Create Your Account | Epic Influencers' ,'signup_status':'active', 'side_status':'left'})

def logout(request):
    auth.logout(request)
    return redirect('/')

def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.success(request, 'Email verified')
        return redirect('home')

    return render(request, 'creators/activate-failed.html')


def RequestPasswordReset(request):
    if request.method=="POST":
        email = request.POST['email']
        if not User.objects.filter(email= email).exists():
            messages.error(request, 'Invalid Email')
            return redirect('reset-password')
        else:
            user = User.objects.filter(email=email)[0]
            if not user.is_email_verified:
                messages.warning(request, 'Please verify your email first to activate your account')
                return redirect('reset-password')
            else:
                current_site = get_current_site(request)
                email_subject = "Epic Influencers -  Reset Password Instructions"
                email_body = render_to_string('creators/request-reset-password.html', {
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': PasswordResetTokenGenerator().make_token(user)
                })
                email = EmailMessage(subject=email_subject, 
                            body=email_body, 
                            from_email= settings.EMAIL_FROM_USER,
                            to=[user.email]
                            )
                EmailThread(email).start()
                messages.success(request, 'We have sent you an email to reset your password. Please also check in spam.')
                return redirect('login')
    else:
        return render(request, 'creators/reset-password.html')


def RenderResetPasswordTemplate(request, uidb64, token):
    if request.method=="POST":
        context={
            'uidb64': uidb64,
            'token': token
        }
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, 'Password not matching')
            return render(request, 'creators/newpassword.html', context)
        else:
            try:
                uid = force_text(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
                user.set_password(password1)
                user.save()
                messages.success(request, 'Password Changed, you can login now')
                return redirect('login')
            except Exception as e:
                messages.error(request, 'Something went wrong')
                return redirect('reset-password')
    else:
        context={
            'uidb64': uidb64,
            'token': token
        }
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.warning(request, 'Link Expired. You can request a new one.')
                return redirect('reset-password')
        except:
            messages.error(request, 'Something went wrong')
            return redirect('reset-password')
    return render(request, 'creators/newpassword.html', context)
    