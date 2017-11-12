def includeme(config):
    config.add_route('home','/')
    config.add_route('list','/list')
    config.add_route('exports','/exports')
    config.add_route('fexports', '/fexports')
    config.add_route('download', '/download')