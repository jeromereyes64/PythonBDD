class ResponseCode:
    OK = 200  # Successful request
    CREATED = 201  # Resource successfully created
    ACCEPTED = 202  # Request accepted but processing not complete
    NO_CONTENT = 204  # Request successful, but no content returned

    BAD_REQUEST = 400  # Client-side error (invalid request)
    UNAUTHORIZED = 401  # Authentication required
    FORBIDDEN = 403  # Access denied
    NOT_FOUND = 404  # Resource not found
    METHOD_NOT_ALLOWED = 405  # HTTP method not supported
    CONFLICT = 409  # Request conflicts with server state
    UNSUPPORTED_MEDIA_TYPE = 415  # Invalid request format

    INTERNAL_SERVER_ERROR = 500  # Generic server error
    NOT_IMPLEMENTED = 501  # Endpoint not implemented
    BAD_GATEWAY = 502  # Invalid response from upstream server
    SERVICE_UNAVAILABLE = 503  # Server temporarily overloaded or under maintenance
    GATEWAY_TIMEOUT = 504  # Upstream server timeout