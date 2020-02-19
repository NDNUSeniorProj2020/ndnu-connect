from .accounts.serializers import UserSerializer


def my_jwt_response_handler(token, user=None, request=None):
    context = {
        'request': request
    }

    return {
        'token': token,
        'user': UserSerializer(user, context).data
    }
