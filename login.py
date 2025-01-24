from flask_restful import Resource, Api

class Login(Resource):
    def post(self):
        user = User.query.filter(username == request.get_json()['username']).first()
        
        session['user_id'] = user.id
        return user.to_dict()

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(username == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {
                {'message': '401: Not Authorized'}, 401
            }      
api.add_resource(CheckSession, '/check_session')

class Logout(self):
    def delete(self):
        session['user_id'] = None
        return {'message': '204: No Content'}, 204
api.add_resource(Logout, '/logout')
        