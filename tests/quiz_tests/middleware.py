from icecream import ic
import requests as r
import json as j


class Middleware:
    mockdata_path = "mockdata/"
    api_base_path = "http://api.localhost:1001/api/"
    prefix_auth = "auth/"
    methods = {
            'post': r.post,
            'get': r.get,
        }

    def __init__(self, credentials_role: str):
        self.__load_credentials(credentials_role)
        self.__prepare_authentication_headers()

    def __load_credentials(self, credentials_role):
        credentials_mockdata_path = self.mockdata_path + credentials_role + "_credentials.json"
        try:
            self.credentials_data = j.load(open(credentials_mockdata_path))
            ic(self.credentials_data)
        except Exception as e:
            message = "Credentials file not found or internal error"
            raise Exception(f"{message} {e}")
        
    def get_credentials(self):
        return self.credentials_data
    
    def get_authentication_headers(self):
        return self.authentication_headers
    
    def build_endpoint(self, path):
        ic(path)
        return self.api_base_path + "".join(path)
    
    def make_request(self, endpoint, method, data = None, json = None, headers = None):
        try:
            headers = self.authentication_headers if (self.authentication_headers and not headers) else headers
            if data or json:
                to_send = {'data': data} if (data and not json) else {'json': json}
                ic(endpoint, headers, to_send)
                response = self.methods[method](endpoint, headers=headers, **to_send)
            else:
                ic(endpoint, headers)
                response = self.methods[method](endpoint, headers=headers)
            ic(response)
            data = response.json()
            ic(data)
            status_code = response.status_code
            return data, status_code
        except Exception as e:
            message = "Error during requisition..."
            raise Exception(f"{message} {e}")

    def test_authentication(self):
        endpoint = self.build_endpoint([self.prefix_auth, "login"])
        data, status_code = self.make_request(endpoint, "post", data=self.credentials_data)
        try:
            assert status_code == 200
            assert data["data"]["token"] is not None
            authentication = data["data"]["token"]
            return authentication
        except Exception as e:
            message = "Error on authentication..."
            raise Exception(f"{message} {e}")
    
    def __prepare_authentication_headers(self):
        # [TODO] Make authentication only if expired
        self.authentication_headers = None
        authentication = self.test_authentication()
        self.authentication_headers = { "Authorization": "Bearer " + authentication }