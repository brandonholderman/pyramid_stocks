def includeme(config):
    """
    Sets the route for each corresponding jinja2 file
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/auth')
    config.add_route('portfolio', '/portfolio')
    config.add_route('add', '/add')
    config.add_route('detail', '/detail/{symbol}')
    config.add_route('logout', '/logout')
