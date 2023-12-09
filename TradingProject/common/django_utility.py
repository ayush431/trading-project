from rest_framework.response import Response
from common.constant import *


def send_response(exception_occured=True, custom_description=None, response_status=None, request=None, time_taken=None, response_data=[]):
    try:
        response_status, response_code, description = make_response(
            exception_occured=exception_occured, response_status=response_status)
        if custom_description:
            description = str(custom_description)
        response = {"response_status": response_status, "response_code": response_code,
                    "description": description, "time_taken": time_taken, "response_data": response_data}
        
        return Response(data=response)
    except Exception as e:
        send_response(exception_occured=True, custom_description=SOMETHING_WENT_WRONG_MSG,
                      response_status=RESPONSE_STATUS_500, request=request, time_taken=time_taken)


def make_response(exception_occured=True, response_status=RESPONSE_STATUS_400):
    response_status = response_status if response_status else RESPONSE_STATUS_400
    if exception_occured:
        return response_status, ERROR_RESPONSE_CODE, SOMETHING_WENT_WRONG_MSG
    else:
        return RESPONSE_STATUS_200, SUCCESS_RESPONSE_CODE, SUCCESS_MSG