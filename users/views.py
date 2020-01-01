from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from users.serializers import UserSerializer, SigninSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = [
        'username',
        'email',
        'first_name',
        'last_name'
    ]
    filterset_fields = [
        'username',
        'is_superuser',
        'is_active',
    ]

    authentication_classes = (
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication,

    )
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def signin(self, request=None):
        serializer = SigninSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.validated_data.get('username'))
        token = Token.objects.get(user=user)

        return Response({
            'username': serializer.validated_data.get('username'),
            'email': user.email,
            'token': f'Token {token.key}',
        })