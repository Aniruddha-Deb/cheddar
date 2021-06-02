from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/move')
def move():
    return 'Making move'

@bp.route('/join_game')
def join_game():
    return 'joining game'

@bp.route('/board')
def board():
    return 'get board'

@bp.route('/exit_game')
def exit_game():
    return 'exiting game'