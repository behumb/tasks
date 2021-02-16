from django.db.models import Count
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
import accounts.serializers as serializers
from datetime import datetime
import jwt

from accounts_api.settings import SECRET_KEY


class UserList(APIView):
    def get(self, request):
        groups_str = request.query_params.get('groups')
        if groups_str:
            users = User.objects.prefetch_related('groups', 'groups__permissions').filter(
                groups__name__in=groups_str.split(','))
        else:
            users = User.objects.prefetch_related('groups', 'groups__permissions').all()
        serializer = serializers.UserResponseSerializer(users, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        request_serializer = serializers.UserRequestSerializer(data=request.data)
        user = request_serializer.get_user_from_serializer()
        response_serializer = serializers.UserResponseSerializer(user)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    def get(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = serializers.UserResponseSerializer(user)
        return Response(data=serializer.data)

    def patch(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = serializers.UserResponseSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupList(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = serializers.GroupSerializer(groups, many=True)
        return Response(data=serializer.data)


class CurrentUserDetail(APIView):
    def get(self, request):
        current_user = request.user
        serializer = serializers.UserResponseSerializer(current_user)
        return Response(data=serializer.data)


class PasswordReset(APIView):
    def patch(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        request.data.update({'user_id': id})
        serializer = serializers.PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data.get('new_password'))
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCount(APIView):
    def get(self, request):
        if request.query_params.get('only_admin') == 'True':
            users = User.objects.filter(is_superuser=True)
            return Response(data={'admin_count': users.count()})
        elif request.query_params.get('only_active') == 'True':
            users = User.objects.filter(is_active=True)
            return Response(data={'active_count': users.count()})
        else:
            return Response(data={'users_count': User.objects.count()})


class UserRegisteredCount(APIView):
    def get(self, request):
        now = datetime.now()
        if request.query_params.get('time_interval') == 'month':
            users = User.objects.filter(date_joined__month=now.month)
            return Response(data={'in_month': users.count()})
        elif request.query_params.get('time_interval') == 'week':
            users = User.objects.filter(date_joined__week=now.strftime("%V"))
            return Response(data={'in_week': users.count()})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserGroups(APIView):
    def get(self, request):
        groups = Group.objects.filter(user__exact=not None)
        group_ids = [group.id for group in groups]
        return Response(data=group_ids)


class GroupUsersCount(APIView):
    def get(self, request):
        groups = Group.objects.prefetch_related('permissions').all().annotate(user_count=Count('user'))
        serializer = serializers.GroupUserCountSerializer(groups, many=True)
        return Response(data=serializer.data)


class ObtainToken(APIView):
    def post(self, request):
        token_serializer = serializers.ObtainTokenSerializer(data=request.data)
        token_serializer.is_valid(raise_exception=True)
        response_serializer = serializers.TokenResponseSerializer(data=token_serializer.validated_data)
        response_serializer.is_valid(raise_exception=True)
        return Response(data=response_serializer.data)


class VerifyToken(APIView):
    def post(self, request):
        verify_serializer = serializers.VerifyTokenSerializer(data=request.data)
        verify_serializer.is_valid(raise_exception=True)
        response_serializer = serializers.TokenResponseSerializer(data=verify_serializer.validated_data)
        response_serializer.is_valid(raise_exception=True)
        return Response(data=response_serializer.data)