from . import api

@api.route('/users')
def users():
    return "inside users"


@api.route('/users2')
def users2():
    return "inside users 2"