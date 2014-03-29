# -*- coding: utf-8 -*-

"""
Tests for the blobstorage module
Usage:  python -m unittest -v test_blobstorage
"""

import unittest
import sys
import dev_appserver
sys.path = dev_appserver.EXTRA_PATHS + sys.path
from google.appengine.ext import testbed
from google.appengine.api.blobstore import blobstore_stub, file_blob_storage
from google.appengine.api.files import file_service_stub

from gae_blobstorage import BlobStorage

class TestbedWithFiles(testbed.Testbed):

    def init_blobstore_stub(self):
        blob_storage = file_blob_storage.FileBlobStorage(
          '/tmp/testbed.blobstore',
          testbed.DEFAULT_APP_ID
        )
        blob_stub = blobstore_stub.BlobstoreServiceStub(blob_storage)
        file_stub = file_service_stub.FileServiceStub(blob_storage)
        self._register_stub('blobstore', blob_stub)
        self._register_stub('file', file_stub)

class TestBlobStorage(unittest.TestCase):

    def setUp(self):
        self.storage = BlobStorage()

        self.testbed = TestbedWithFiles()
        self.testbed.activate()
        self.testbed.init_blobstore_stub()
        self.testbed.init_datastore_v3_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_save(self):
        file_name = 'test_name'
        file_content = b'test_content'

        f_name = self.storage.save(file_name, file_content)

        self.assertEqual(f_name, file_name)

    def test_open(self):
        file_name = 'test_name'
        file_content = b'test_content'

        self.storage.save(file_name, file_content)

        f = self.storage.open(file_name)

        self.assertEqual(f.read(), file_content)

    def test_exists(self):
        file_name = 'test_name'
        file_content = b'test_content'

        self.assertFalse(self.storage.exists(file_name))

        self.storage.save(file_name, file_content)

        self.assertTrue(self.storage.exists(file_name))

    def test_available_name(self):
        file_name = 'test_name'
        file_content = b'test_content'

        self.storage.save(file_name, file_content)

        f_name_1 = self.storage.save(file_name, file_content)
        f_name_2 = self.storage.save(file_name, file_content)

        self.assertEqual(f_name_1, "%s" % file_name)
        self.assertEqual(f_name_2, "%s" % file_name)

    def test_unicode_file_names(self):
        file_name = u'¿Cómo?'
        file_content = b'test_content'

        f_name = self.storage.save(file_name, file_content)

        self.assertEqual(f_name, file_name)

if __name__ == '__main__':
    unittest.main()
