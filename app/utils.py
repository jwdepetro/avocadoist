"""
Defines all utility functions that can be used across the app.
"""

def get_client_ip(request):
    """
    Get the client IP address
    :param request:
    :return:
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    return ip_address


def get_anonymous_id(request):
    """
    Get the anonymous ID for users
    :param request:
    :return:
    """
    if not request.session.session_key:
        request.session.create()

    return request.session.session_key
