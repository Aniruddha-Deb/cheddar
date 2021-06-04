from flask import Blueprint, request, session, g
import chess
from chess import Board

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/move')
def move():
    if 'game' not in g:
        g.game = chess.STARTING_FEN
    from_sq = request.args.get("from")
    to_sq = request.args.get("to")
    print(f"{from_sq} -> {to_sq}")
    board = Board(fen=g.game)
    try:
        legal_move = board.find_move(chess.parse_square(from_sq), chess.parse_square(to_sq))
        board.push(legal_move)
        g.game = board.fen()
        print("Found legal move")
        print(board)
        return "LEGAL"
    except:
        print("Found illegal move")
        print(board)
        return "ILLEGAL"

@bp.route('/join_game')
def join_game():
    return 'joining game'


@bp.route('/board')
def board():
    return 'get board'

@bp.route('/exit_game')
def exit_game():
    return 'exiting game'