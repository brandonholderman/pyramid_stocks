def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('auth', '/auth')
    config.add_route('portfilio', '/portfolio')
    config.add_route('stock-add', '/portfolio/{symbol}')
    config.add_route('stock-detail', '/portfolio{symbol}')
