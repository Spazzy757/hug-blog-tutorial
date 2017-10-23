import directive_example
import hug
import hello_world
import unittest
from falcon import HTTP_200


class TestApp(unittest.TestCase):
    def tests_hello_world(self):
        response = hug.test.get(hello_world, '/world')
        assert response.status == HTTP_200
        assert response.data is not None

    def tests_directive_example(self):
        response = hug.test.get(directive_example, '/data', {'name': 'JohnSnow'})
        assert response.status == HTTP_200
        assert response.data is not None


if __name__ == '__main__':
    unittest.main()
