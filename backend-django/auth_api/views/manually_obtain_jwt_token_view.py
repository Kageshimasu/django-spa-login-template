from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response

from ..serializers.user_auth import UserAuth

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class TokenObtainView(APIView):

    @staticmethod
    def post(request):
        serializer = UserAuth(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.data)
        if not user:
            return Response({'message': 'Incorrect Username or Password'}, status=403)
        payload = jwt_payload_handler(user)
        return Response({'access': jwt_encode_handler(payload)})
