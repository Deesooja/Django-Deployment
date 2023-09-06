from rest_framework.views import APIView
from django.http.response import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

class CrudApiView(APIView):
    def get(self, request, format=None):
        user_list = []
        for user in User.objects.all():
            user_dict = {
                "id":user.id,
                "username":user.username,
                "email":user.email
            }
            user_list.append(user_dict)
        return JsonResponse({"data": user_list})
    def post(self, request):
        data = request.data
        print(data)
        # username=data.get('username')
        # email=data.get('email')
        # password=data.get('password')
        # user_object = User.objects.create(
        #     username=username,
        #     email=email,
        #     password=password
        # )
        # data["id"]=user_object.id
        return JsonResponse({"data": data})
    
    def put(self, request, pk):
        data = request.data
        username=data.get('username')
        email=data.get('email')

        user_object = User.objects.filter(id=pk).update(
            username=username,
            email=email,
        )
        respons_dict = {
            "id":pk,
            "username":username,
            "email":email
        }

        return JsonResponse({"data": respons_dict})

    
    def delete(self, request, pk):
        user_object = User.objects.get(id=pk)
        user_object.delete()
        return JsonResponse({"data": pk})