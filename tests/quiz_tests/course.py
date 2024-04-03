import requests as r
import json as j
from middleware import Middleware


class Course:
    prefix_admin = "admin/"
    prefix_course = "courses/"

    def __init__(self, middleware: Middleware):
        self.m = middleware

    def test_list_courses(self):
        endpoint = self.m.build_endpoint([self.prefix_admin, self.prefix_course])
        data, status_code = self.m.make_request(endpoint, "get")
        assert status_code == 200
        assert (len(data['data']) > 0)
        data = data['data']
        print(len(data))
        print(data)