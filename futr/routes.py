from futr.database.factory import db


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('home_json', '/api/')
    config.add_tween('futr.routes.close_db_tween_factory')


def close_db_tween_factory(handler, registry):
    """
    Factory for creating the tween that wraps around the view.
    """
    def _tween(request):
        """
        This is called in stead of the view with the view as param.
        """
        # do stuff before view code with request and session

        # execute the view, creates the response
        response = handler(request)
        # do stuff after the view code with request and session
        db.close()
        # return the response returned by the view
        return response

    # return the new tween
    return _tween
