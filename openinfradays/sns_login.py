from django.utils import timezone
import requests
import json
import uuid
import csv


from datetime import datetime, timedelta

from django.contrib.auth import get_user_model, login
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


from .models import Profile, OnetimeToken
from .views import make_menu_context
from . import get_client_ip


UserModel = get_user_model()


def login_with_github(request):
    client_id = settings.GITHUB_CLIENT_ID
    redirect_url = settings.GITHUB_CALLBACK_URL
    url = "https://github.com/login/oauth/authorize?client_id=%s&redirect_uri=%s&scope=read:user"
    return redirect(url % (client_id, redirect_url))


# https://wayhome25.github.io/django/2017/05/18/django-auth/
def github_callback(request):
    code = request.GET.get("code", None)
    client_id = settings.GITHUB_CLIENT_ID
    client_secret = settings.GITHUB_CLIENT_SECRET
    token_request = requests.post(
        f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
        headers={"Accept": "application/json"},
    )
    token_json = token_request.json()
    access_token = token_json.get("access_token")
    profile_request = requests.get(
        "https://api.github.com/user",
        headers={
            "Authorization": f"token {access_token}",
            "Accept": "application/json",
        },
    )
    profile_json = profile_request.json()
    username = profile_json.get('login', None)
    if username is not None:
        name = profile_json.get('name', 'NO NAME')
        email = profile_json.get("email")
        if email is None:
            email = 'no_email'
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = UserModel(username=username)
            user.first_name = name
            user.email = email
            user.save()
            user.profile.login_type = Profile.GITHUB
            user.save()
        login(request, user)
        if not user.profile.agree_with_private:
            return redirect('/join')
    return redirect('/')


@csrf_exempt
def login_with_onetime(request):

    if request.method == "GET":
        email = request.COOKIES.get('email', '')
        if email == '':
            return redirect('/')

        context = {'email': email}
        menu = make_menu_context()
        return render(request, 'onetime_login_info.html', {**menu, **context})

    if request.method != "POST":
        return redirect('/')

    body = json.loads(request.body)
    try:
        user = UserModel.objects.get(email=body.get('email', ''))
    except UserModel.DoesNotExist:
        return HttpResponse('Unauthorized', status=401)

    email_appkey = settings.NHNCLOUD_EMAIL_APPKEY
    email_secret = settings.NHNCLOUD_EMAIL_SECRET
    base_domain = settings.BASE_DOMAIN

    token = uuid.uuid4().hex
    client_ip = get_client_ip(request)
    expire = datetime.now() + timedelta(days=1)
    ott = OnetimeToken(user=user, token=token, request_ip=client_ip, expire_at=expire)
    ott.save()

    response = requests.post(
        url="https://api-mail.cloud.toast.com/email/v2.0/appKeys/%s/sender/mail" % email_appkey,
        headers={
            "X-Secret-Key": email_secret,
            "Content-Type": "application/json; charset=utf-8",
        },
        data=json.dumps({
            "senderName": "OpenInfra Days Korea",
            "templateId": "onetime_login",
            "receiverList": [
                {
                    "receiveMailAddr": body.get('email'),
                    "receiveType": "MRT0"
                }
            ],
            "templateParameter": {
                "onetime_url": "%s/login/onetime/%s" % (base_domain, token)
            }
        })
    )
    resp_body = json.loads(response.content)
    if resp_body['header']['resultMessage'] != 'success':
        return HttpResponse('{"fail": "Fail to send email"}', status=400)
    resp = HttpResponse('{}', content_type='application/json')
    resp.set_cookie('email', body.get('email'))
    return resp


def onetime_login_check(request, token):
    try:
        ott = OnetimeToken.objects.get(token=token)
    except Exception as e:
        print(e)
        return render(request, 'onetime_login_error.html')

    now = timezone.now()
    if ott.expired or now > ott.expire_at:
        return render(request, 'onetime_login_error.html')
    client_ip = get_client_ip(request)

    if client_ip != ott.request_ip:
        return render(request, 'onetime_login_error.html')

    user = ott.user
    ott.expired = True
    ott.access_time = datetime.now()
    ott.save()
    login(request, user)
    return redirect('/')
