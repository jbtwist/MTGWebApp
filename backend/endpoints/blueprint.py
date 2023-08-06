from controllers.index import RHIndexHTML


def register_blueprints(bp):
    bp.add_url_rule('/', 'index', RHIndexHTML)
