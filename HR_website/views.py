from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Attendence
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        attend = request.form.get('attendence')
        new_record = Attendence(data=attend, user_id=current_user.id)
        db.session.add(new_record)
        db.session.commit()
        flash('Check-In Added!', category='success')
    # if request.method == 'PUT':
    #     id = request.form.get('id')
    #     rec = Attendence.query.filter_by(id==id).first()
    #     checkout = request.form.get('checkout')
    #     recnew= Attendence(id= id, checkout=checkout, user_id=current_user.id)
    # if request.method == 'POST':
    #     if request.form.get('action1') == 'VALUE1':
    #         attend = request.form.get('attendence')
    #         new_record = Attendence(data=attend, user_id=current_user.id)
    #         db.session.add(new_record)
    #         db.session.commit()
    #         flash('Check-In Added!', category='success')
     

        # else:
            # pass # unknown
    # elif request.method == 'GET':
        # return render_template('index.html', form=form)

    return render_template("home.html", user=current_user)

# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def employee():
    
#     return render_template("admin.html")
