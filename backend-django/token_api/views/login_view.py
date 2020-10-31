from django.contrib.auth.models import User
from django.http.response import JsonResponse
from rest_framework.views import APIView
from ..models import TokenRDB

import json


class Login(APIView):

    @staticmethod
    def post(request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
        except:
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        if not User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Login failure.'}, status=403)

        user = User.objects.get(email=email)
        if not user.check_password(password):
            return JsonResponse({'message': 'Login failure.'}, status=403)

        token = TokenRDB.create(user)
        return JsonResponse({'token': token.token})
