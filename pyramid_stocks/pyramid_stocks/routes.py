def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('auth', '/auth')
    config.add_route('portfolio', '/portfolio')
    config.add_route('add', '/add')
    config.add_route('detail', '/detail')
