# -*- coding: utf-8 -*-

"""
Module for working with google app engine blob storage
"""

from google.appengine.ext import blobstore
from google.appengine.api import files

class BlobStorage():

    def save(self, name, content):
        file_name = files.blobstore.create(
          mime_type='application/octet-stream',
          _blobinfo_uploaded_filename=name
        )

        with files.open(file_name, 'a') as f:
            f.write(content)

        files.finalize(file_name)
        return name

    def open(self, filename, mode='rb'):
        blobinfo = blobstore.BlobInfo.all().filter('filename =', filename)

        blobstore_key = blobinfo[0].key()._BlobKey__blob_key
        blobstore_info = blobstore.BlobInfo.get(blobstore_key)

        blobstore_file = blobstore.BlobReader(blobstore_key)
        blobstore_file.name = blobstore_info.filename.split('/')[-1]

        return blobstore_file

    def exists(self, name):
        blobinfo = blobstore.BlobInfo.all().filter('filename =', name)

        if blobinfo.count():
            return True
        return False
