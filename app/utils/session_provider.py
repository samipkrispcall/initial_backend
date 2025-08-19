from starlette.requests import Request

def get_session(request: Request):
        return request.state.session
        # return None
