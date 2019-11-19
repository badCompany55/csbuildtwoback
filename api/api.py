from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from map.models import Map
from users.models import CustomUser, Status
from api.models import Message
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import subprocess

class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ["data"]

    def create(self, validated_data):
        map = Map.objects.create(**validated_data)
        return map

class MapViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MapSerializer
    queryset = Map.objects.all()

class TokenObtainPairPatchedSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):

        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['user'] = self.user.id
        data['backtoken'] = self.user.backtoken

        return data

class TokenObtainPairPatchedView(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairPatchedSerializer

class StatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ["inventory", "current_room"]

    def create(self, validated_data):
        user = CustomUser.objects.get(id=self.context['request'].user.id)
        status = Status.objects.filter(player=user)
        if status:
            status.update(**validated_data)
        else:
            status = Status.objects.create(player=user, **validated_data)
        return status


class UpdateStatsAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatsSerializer
    queryset = Status.objects.all()

class LootSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ["key", "message"]


class RunLootAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/farm.py", "-k", f'{self.request.headers["backKey"]}'])
        return message

class ChangeNameAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "467"])
        return message

class BrightlyLitRoomAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "0"])
        return message

class ShopAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "1"])
        return message

class MistyRoomAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "170"])
        return message

class MtHollowayAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "202"])
        return message

class PeakOfMtHollowayAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "22"])
        return message

class TransmogriphierAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "495"])
        return message

class ADarkCaveApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "450"])
        return message

class LinhsShrineApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "461"])
        return message

class GlassowynsGraveApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "499"])
        return message

class WishingWellApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LootSerializer
    @action(detail=False)

    def get_queryset(self):
        message = Message.objects.filter(key="loot")
        p = subprocess.Popen(["python3", "scriptsapp/travel-to.py", "-k", f'{self.request.headers["backKey"]}',  "-d", "55"])
        return message
