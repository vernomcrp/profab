import socket

from profab import _Keys
from profab.tests.mockboto.image import MockInstance, MockImage, MockVolume


class MockConnection(object):
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self._key = aws_access_key_id
        self._secret = aws_secret_access_key
        self._key_pairs = []
        self._key_pairs_created = []

    def associate_address(self, instance_id, ip):
        pass

    def create_key_pair(self, host):
        self._key_pairs_created.append(host)
        key_pair = _Keys(name=host)
        key_pair.save = lambda f: None
        self._key_pairs.append(key_pair)
        return key_pair

    def create_volume(self, size, zone):
        return MockVolume()

    def get_all_key_pairs(self):
        return self._key_pairs

    def get_all_images(self, image):
        return [MockImage()]

    def get_all_volumes(self):
        return [MockVolume()]

    def get_all_instances(self):
        return [_Keys(instances=[MockInstance('running')])]

    #def get_all_zones(self):
        #return [_Keys()]


class Region(object):
    def connect(self, aws_access_key_id, aws_secret_access_key):
        return MockConnection(aws_access_key_id, aws_secret_access_key)


def regions(**kwargs):
    cnx = MockConnection(**kwargs)
    return [Region(), Region()]
