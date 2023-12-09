from functools import wraps
from common.django_utility import send_response
from common.utility import get_current_time

def validate_params(params):
    def inner_validate_params(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            try:
                start_time = get_current_time()
                if not args[0].data or not isinstance(args[0].data, dict):
                    raise TypeError("Invalid request body")
                for each_param in params:
                    if not each_param in args[0].data.keys():
                        raise KeyError(
                            "Missing parameter ({}) in request body".format(each_param)
                        )
            except Exception as error_msg:
                return send_response(
                    exception_occured=True,
                    custom_description=error_msg,
                    time_taken=get_current_time() - start_time,
                    request=args[0],
                )
            return function(request, *args, **kwargs)

        return wrap

    return inner_validate_params