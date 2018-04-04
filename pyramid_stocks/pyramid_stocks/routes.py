def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('register', '/auth')
    config.add_route('login', '/auth')
    config.add_route('portfilio', '/stock')
    config.add_route('stock-add', '/portfolio/{symbol}')
    config.add_route('stock-detail', '/portfolio{symbol}')
