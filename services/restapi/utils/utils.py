from flask import request, jsonify

def RESPONSE(answer={'success':True}, status=200):
    return jsonify(answer), status, {'ContentType':'application/json'} 

RESPONSE_200 = RESPONSE
RESPONSE_201 = lambda: RESPONSE(status = 201)
RESPONSE_204 = lambda: RESPONSE(status = 204)
RESPONSE_400 = lambda reason=None: RESPONSE({'success': False, 'reason': reason}, 400)
RESPONSE_404 = lambda reason=None: RESPONSE({'success': False, 'reason': reason}, 404)
RESPONSE_500 = lambda reason=None: RESPONSE({'success': False, 'reason': reason}, 500)


def register_api(bp, view, endpoint, url, pk='id', pk_type='string'):
    view_func = view.as_view(endpoint)
    bp.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    bp.add_url_rule(url, view_func=view_func, methods=['POST',])
    bp.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])
