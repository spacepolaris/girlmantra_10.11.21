from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import \
    testApiPostSerializer, testApiGetSerializer, testApiDeleteSerializer, testApiPutSerializer, \
    userMobileSrializer, userPersonalInfoSerializer, userGoalsSerializer, userProblemsSerializer, userPreferredTimeSerializer


from .services.testapi import testPost, testGet, testDelete, testPut
from .services.registration import saveStartOnboarding, savePersonalInfo, saveGoals, saveProblems, savePreferredTimes, \
    getUserFullStatus, getUserRegistrationStatusOnly, getPersonalInfo, getGoals, getProblems, getPreferredTimes


# TEST API
class test_api(APIView):

    def get(self, request):
        serializer = testApiGetSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = testGet(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = testApiPostSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = testPost(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_201_CREATED)
            return Response(return_data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        serializer = testApiDeleteSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = testDelete(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = testApiPutSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = testPut(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class test_update_api(APIView):
    def post(self, request):
        serializer = testApiPutSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = testPut(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# REGISTRATION PROCESS POST

class start_onboard_post_api(APIView):

    def post(self, request):
        serializer = userMobileSrializer(data=request.data)
        if serializer.is_valid():
            ob1 = saveStartOnboarding(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_201_CREATED)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class save_personal_info_post_api(APIView):

    def post(self, request):
        serializer = userPersonalInfoSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = savePersonalInfo(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_201_CREATED)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class save_goals_post_api(APIView):

    def post(self, request):
        serializer = userGoalsSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = saveGoals(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_201_CREATED)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class save_problems_post_api(APIView):

    def post(self, request):
        serializer = userProblemsSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = saveProblems(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_201_CREATED)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class save_preferred_time_post_api(APIView):

    def post(self, request):
        serializer = userPreferredTimeSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = savePreferredTimes(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_201_CREATED)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET USER INFO
class get_user_full_status_api(APIView):
    def get(self, request):
        serializer = userMobileSrializer(data=request.data)
        if serializer.is_valid():
            ob1 = getUserFullStatus(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class get_user_registration_status_api(APIView):
    def get(self, request):
        serializer = userMobileSrializer(data=request.data)
        if serializer.is_valid():
            ob1 = getUserRegistrationStatusOnly(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_personal_info_api(APIView):
    def get(self, request):
        serializer = userMobileSrializer(data=request.data)
        if serializer.is_valid():
            ob1 = getPersonalInfo(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_goals_api(APIView):
    def get(self, request):
        serializer = userMobileSrializer(data=request.data)
        if serializer.is_valid():
            ob1 = getGoals(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_problems_api(APIView):
    def get(self, request):
        serializer = userMobileSrializer(data=request.data)
        if serializer.is_valid():
            ob1 = getProblems(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_preferred_time_api(APIView):
    def get(self, request):
        serializer = userMobileSrializer(data=request.data)
        if serializer.is_valid():
            ob1 = getPreferredTimes(serializer)
            return_data = ob1.start_process()
            if return_data["return_type"] == "success":
                return Response(return_data, status=status.HTTP_302_FOUND)
            else:
                return Response(return_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
