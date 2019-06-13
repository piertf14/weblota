import uuid
import os
from time import gmtime, strftime


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4()).replace('-', ''), ext)
    path = strftime("gallery/%Y/%m/%d", gmtime())
    return os.path.join(path, filename)