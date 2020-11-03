from django.http.response import JsonResponse
from rest_framework.views import APIView


class HelloWorldView(APIView):

    @staticmethod
    def post(request):
        return JsonResponse({'message': 'hello world'})
