from collections import defaultdict
from flask import Blueprint, render_template, jsonify, redirect, url_for

mod = Blueprint('game', __name__, url_prefix='/game')
menu_list = defaultdict(lambda: {})
