from typing import Union

from decouple import config
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from utils.constants import GRANT_TYPE, REDIRECT_LOCAL_URL
from utils.wrappers import MeliWrapper
from meli import OAuth20Api, ApiClient


def oauth_login(request):
    with ApiClient() as api_client:
        auth_api = OAuth20Api(api_client)
        meli_wrapper = MeliWrapper(
            auth_api=auth_api,
            grant_type=GRANT_TYPE,
            client_id=config('APP_ID'),
            client_secret=config('APP_SECRET'),
            redirect_uri=REDIRECT_LOCAL_URL,
        )
        response = meli_wrapper.get_auth()
        return response


def oauth_redirect(request):
    with ApiClient() as api_client:
        code = request.GET.get('code')
        print(code)
        auth_api = OAuth20Api(api_client)
        meli_wrapper = MeliWrapper(
            auth_api=auth_api,
            grant_type=GRANT_TYPE,
            client_id=config('APP_ID'),
            client_secret=config('APP_SECRET'),
            redirect_uri=REDIRECT_LOCAL_URL,
        )

        user_data = meli_wrapper.get_token(code)

        return render(request, 'auth/oauth_redirect.html', {
            'response': user_data
        })
