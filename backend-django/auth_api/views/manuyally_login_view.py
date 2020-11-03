import json

from django.http.response import JsonResponse
from rest_framework.views import APIView

from ..models import CustomUser


class LoginView(APIView):
    permission_classes = ()

    @staticmethod
    def post(request):
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
        except:
            return JsonResponse({'message': 'Invalid POST Request'}, status=400)

        if not CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Incorrect Username or Password'}, status=403)

        user = CustomUser.objects.get(username=username)
        if not user.check_password(password):
            return JsonResponse({'message': 'Incorrect Username or Password'}, status=403)

        return JsonResponse({'message': 'login succeeded'})
