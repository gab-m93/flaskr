import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('/test', methods=('GET', 'POST'))

def test():
    if request.method == 'POST':
        username = request.form['username']
    
    return render_template('test/test.html')