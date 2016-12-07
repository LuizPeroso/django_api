"""Default authentication classes.
"""
import logging
import requests

from tastypie.authentication import ApiKeyAuthentication
from tastypie.http import HttpAccepted

from main.settings import AUTHENTICATION_API

logger = logging.getLogger(__name__)


class UserAuthentication(ApiKeyAuthentication):
    """Class that extends the ApiKeyAuthentication the tastypie to also
    validate the date of User key expiration
    """

    def is_authenticated(self, request, **kwargs):
        """
        Finds the user and checks their API key.
        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.

        Args:
            request (tastypie.requests): Http request.
            **kwargs (TYPE): kwargs.
        """

        logger.info(
            "status=authenticating_api "
            "step=start message=authentication_initializing")
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            logger.error(
                "status=authenticating_api "
                "step=end message=invalid_api_key")
            return self._unauthorized()

        if not username or not api_key:
            return self._unauthorized()

        data = {
            'username': username,
            'api_key': api_key
        }

        try:
            key_auth_check = requests.post(AUTHENTICATION_API, json=data)
        except Exception:
            logger.error(
                "status=authenticating_api "
                "step=end message=invalid_authentication_api")
            return self._unauthorized()

        if key_auth_check.status_code == HttpAccepted.status_code:
            logger.info(
                "status=authenticating_api "
                "step=end message=api_key_accepted")
            return True
        else:
            logger.info(
                "status=authenticating_api "
                "step=end message=invalid_api_key")
            return False
