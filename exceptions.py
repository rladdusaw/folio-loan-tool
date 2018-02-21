class RequestError(Exception):
    """Raised when a request goes wrong
    Attributes:
        status_code: HTTP status code from authentication
        message: test message from server
        url: URL of the request
        req_headers (optional): request headers
    """
    def __init__(self, status_code, message, url, req_headers = None):
        self.status_code = status_code
        self.message = message
        self.url = url