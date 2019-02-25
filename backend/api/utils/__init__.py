"""
Basic utils used in api application
"""


def paginated_view(wrapped_function):
    """
    Decorator. Allows view functions to receive
    page and items_per_page as keywords parameters
    """
    def wrapper(*args, **kwargs):
        request = args[1]
        page = request.GET.get('page') or 1
        items_per_page = request.GET.get('items_per_page') or 20
        kwargs.update(dict(page=int(page), items_per_page=int(items_per_page)))
        return wrapped_function(*args, **kwargs)

    return wrapper


def list_view(wrapped_function):
    """
    Decorator. Allows view functions receive query params as arguments.
    """

    def wrapper(*args, **kwargs):
        request = args[1]
        page = request.GET.get('page') or 1
        items_per_page = request.GET.get('items_per_page') or 25
        sort_by = request.GET.get('sort_by') or 'started'
        sort_order = request.GET.get('sort_order') or 'desc'

        kwargs.update(dict(
                page=int(page),
                items_per_page=int(items_per_page),
                sort_by=sort_by,
                sort_order=sort_order,
        ))

        return wrapped_function(*args, **kwargs)

    return wrapper
