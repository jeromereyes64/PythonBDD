import requests
from BDD.utils.schema_validator import validate_response_schema

class APIClient:
    def __init__(self, base_url, auth_token=None):
        self.base_url = base_url
        self.auth_token = auth_token

    def _get_headers(self, headers):
        """Merge custom headers with authentication headers"""
        default_headers = {"Content-Type": "application/json"}
        if self.auth_token:
            default_headers["Authorization"] = f"Bearer {self.auth_token}"
        if headers:
            default_headers.update(headers)
        return default_headers

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            print(f"Sending GET request to: {url}")
            if params:
                print(f"🔹 Query Params: {params}")

            response = requests.get(url, params=params, headers=self._get_headers(headers))

            print(f"Response Status: {response.status_code}")
            print(f"Response Body: {response.text}")

            return response
        except requests.RequestException as e:
            print(f"GET request failed: {str(e)}")
            return {"error": str(e)}

    def post(self, endpoint, data, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            print(f"Sending POST request to: {url}")
            print(f"Request Body: {data}")

            response = requests.post(url, json=data, headers=self._get_headers(headers))

            print(f"Response Status: {response.status_code}")
            print(f"Response Body: {response.text}")

            return response
        except requests.RequestException as e:
            print(f"POST request failed: {str(e)}")
            return {"error": str(e)}

    def put(self, endpoint, data, headers=None):
        """Send a PUT request"""
        url = f"{self.base_url}{endpoint}"
        try:
            print(f"Sending PUT request to: {url}")
            print(f"Request Body: {data}")

            response = requests.put(url, json=data, headers=self._get_headers(headers))

            print(f"Response Status: {response.status_code}")
            print(f"Response Body: {response.text}")

            return response
        except requests.RequestException as e:
            print(f"PUT request failed: {str(e)}")
            return {"error": str(e)}

    def patch(self, endpoint, data, headers=None):
        """Send a PATCH request"""
        url = f"{self.base_url}{endpoint}"
        try:
            print(f"Sending PATCH request to: {url}")
            print(f"Request Body: {data}")

            response = requests.patch(url, json=data, headers=self._get_headers(headers))

            print(f"Response Status: {response.status_code}")
            print(f"Response Body: {response.text}")

            return response
        except requests.RequestException as e:
            print(f"PATCH request failed: {str(e)}")
            return {"error": str(e)}

    def delete(self, endpoint, headers=None):
        """Send a DELETE request"""
        url = f"{self.base_url}{endpoint}"
        try:
            print(f"Sending DELETE request to: {url}")

            response = requests.delete(url, headers=self._get_headers(headers))

            print(f"Response Status: {response.status_code}")
            print(f"Response Body: {response.text}")

            return response
        except requests.RequestException as e:
            print(f"DELETE request failed: {str(e)}")
            return {"error": str(e)}


    #Assertion Methods
    @staticmethod
    def assert_schema(response, expected_schema, message="Schema validation failed"):
        """Validates API response against an expected schema"""
        response_data = response.json()
        validation_result = validate_response_schema(response_data, expected_schema)
        assert validation_result is True, f"{message}: {validation_result}"
        print("Schema validation passed!")

    @staticmethod
    def assert_response_time(response, max_time=2.0):
        """Validates that the API response time is within an acceptable limit (default 2 seconds)"""
        response_time = response.elapsed.total_seconds()
        assert response_time < max_time, f"Response time exceeded! Expected < {max_time}s, but got {response_time}s"
        print(f"Response time is within limit: {response_time}s")


    @staticmethod
    def assert_stat_code(response, expected_status, message="Unexpected status code"):
        assert response.status_code == expected_status, f"{message} Expected: {expected_status}, Got: {response.status_code}"