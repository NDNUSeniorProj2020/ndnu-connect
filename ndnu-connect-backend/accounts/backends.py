import jwt

from django.conf import settings
from rest_framework import authentication, exceptions

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    # Authenticate method will always be called regardless of whether the endpoint requires authentication
    # This method returns None if authentication fails, or (user, token) if authentication is successful
    def authenticate(self, req):
        req.user = None

        # auth_header should be an array with header 'Token' and the JWT used to authenticate against
        auth_header = authentication.get_authorization_header(req).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        # Check for invalid token header. If no credentials are provided, do not authenticate
        if len(auth_header) == 1:
            print('len(auth_header) == 1')
            return None

        # Token string should not contain spaces
        elif len(auth_header) > 2:
            print('len(auth_header) > 2')
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        # If the prefix does not match the auth_header_prefix, do not authenticate
        if prefix.lower() != auth_header_prefix:
            print('prefix.lower() != auth_header_prefix')
            return None

        return self._authenticate_credentials(req, token)

    # _authenticate_credentials attempts to authenticate with the given credentials
    def _authenticate_credentials(self, req, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            raise exceptions.AuthenticationFailed('Invalid authentication. Could not decode token.')

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No user matching this token was found.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('This user has been deactivated.')

        return (user, token)
