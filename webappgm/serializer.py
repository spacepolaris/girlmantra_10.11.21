from rest_framework import serializers

# TEST API SERIALIZER
class testApiPostSerializer(serializers.Serializer):
    database_type = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    mobile = serializers.CharField(max_length=15)
    value1 = serializers.IntegerField()
    value2 = serializers.FloatField()

class testApiGetSerializer(serializers.Serializer):
    test_id = serializers.CharField(max_length=30)

class testApiDeleteSerializer(serializers.Serializer):
    test_id = serializers.CharField(max_length=30)

class testApiPutSerializer(serializers.Serializer):
    test_id = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    mobile = serializers.CharField(max_length=15)

# REGISTRATION API SEIALIZER
class userMobileSrializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)

class userPersonalInfoSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()

class userGoalsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
    goals = serializers.CharField(max_length=3000)

class userProblemsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
    problems = serializers.CharField(max_length=3000)

class userPreferredTimeSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
    preferred_time = serializers.CharField(max_length=3000)