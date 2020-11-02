import json

from django.utils import timezone
from django.http.response import JsonResponse
from rest_framework.views import APIView

from ..models import CustomUser


class CreateAccountView(APIView):

    @staticmethod
    def post(request):
        try:
            data = json.loads(request.body)
            username = data['username']
            email = data['email']
            password = data['password']
        except:
            return JsonResponse({'message': 'Invalid POST Request'}, status=400)

        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'}, status=403)

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Email already exists'}, status=403)
        dt = timezone.now()
        user = CustomUser.objects.create_user(username, email, password, access_datetime=dt)
        return JsonResponse({'message': 'successfully created account', 'token': user.token})
