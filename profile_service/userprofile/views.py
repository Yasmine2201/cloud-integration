from rest_framework.response import Response
from rest_framework.views import APIView

from core_models.models import User
from userprofile.serializers import UserSerializer


class UserProfileView(APIView):

    @staticmethod
    def get(request):
        user = request.user
        print("user",user)
        try:
            response = UserSerializer(User.objects.get(id=user.id))
            return Response(response.data, status=200)
        except Exception as e:
            return Response({"message": str(e)}, status=400)

    @staticmethod
    def put(request):
        user = request.user
        user_input = UserSerializer(data=request.data)
        if not user_input.is_valid():
            return Response({"message": "Invalid input. Expected 'username'"}, status=400)

        try:
            user.username = user_input.validated_data['username']
            user.save()
            return Response(UserSerializer(user).data, status=200)

        except Exception as e:
            return Response({"message": str(e)}, status=400)


