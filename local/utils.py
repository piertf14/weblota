import uuid
import os
from time import gmtime, strftime
from rest_framework.permissions import BasePermission

from socceruser.utils import get_access_token


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4()).replace('-', ''), ext)
    path = strftime("gallery/%Y/%m/%d", gmtime())
    return os.path.join(path, filename)


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        try:
            get_access_token(request)
            return True
        except:
            if request.method == 'GET':
                return True
        return False