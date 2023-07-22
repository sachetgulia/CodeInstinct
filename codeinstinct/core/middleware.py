# middlewares.py
import time
import json
from internal.models.instinct_log import InstinctLog


class InstinctLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # Capture request data before processing
        request_data = None
        if request.body:
            try:
                request_data = json.loads(request.body)
            except json.JSONDecodeError:
                request_data = request.body

        response = self.get_response(request)

        end_time = time.time()

        view_method = request.method
        path = request.path
        status_code = response.status_code
        response_time = end_time - start_time

        # Capture response data after processing
        response_data = None
        if response.streaming:
            response_data = "[Streaming response]"
        elif response.content:
            try:
                response_data = json.loads(response.content)
            except json.JSONDecodeError:
                response_data = response.content

        # Save the request-response log to the database
        intinct_log_entry = InstinctLog(
            view_method=view_method,
            path=path,
            request=request_data,
            response=response_data,
            status_code=status_code,
            response_time=response_time,
        )
        intinct_log_entry.save()

        return response
