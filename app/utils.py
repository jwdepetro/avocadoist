def get_client_ip(request):
    """
    Get the client IP address
    :param request:
    :return:
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_anonymous_id(request):
    """
    Get the anonymous ID for users
    :param request:
    :return:
    """
    if not request.session.session_key:
        request.session.create()

    return request.session.session_key
