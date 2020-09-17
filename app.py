#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
import config
from flask_migrate import Migrate
from forms import PromotionForm
from datetime import datetime
import sys
from sqlalchemy import func
import os
import random
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Users(db.Model):
  __tablename__ = 'Users'
  id = db.Column(db.Integer, primary_key=True)
  first = db.Column(db.String)
  last = db.Column(db.String)
  email = db.Column(db.String)
  promo_code = db.Column(db.String(8))
  won = db.Column(db.Boolean)
  date = db.Column(db.DateTime)

class Promos(db.Model):
  __tablename__ = 'Promos'
  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(8))
  date = db.Column(db.DateTime)

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')

#  Promotion
#  ----------------------------------------------------------------
@app.route('/promos')
def promos():
  data = Users.query.filter(Users.won == True).all()
  return render_template('pages/promos.html', promos=data)

@app.route('/promos/new', methods=['GET'])
def new_promo_code():
  form = PromotionForm()
  return render_template('forms/new_promo.html', form=form)

@app.route('/promos/new', methods=['POST'])
def new_promo_submission():
  promo_entry = request.form.to_dict()  # first, last, email, code
  codes = list(Promos.query.all()) #TODO cache this better

  # win_check = random.choice(codes) == promo_entry['code']
  curr_date = datetime.today().date()
  duplicate = Users.query.filter_by(email=promo_entry['email'], date=curr_date).first()

  try:
    new_entry = Users(first=promo_entry['firstname'], last=promo_entry['lastname'], 
              email=promo_entry['email'], promo_code=promo_entry['code'], won=win_check,
              date=curr_date)
    db.session.add(new_entry)
    db.session.commit()

    if duplicate: # duplicate email within 24h
      flash('You have already submitted a code today, please wait 24 hours!')
    elif win_check: # won
      flash('Congratulation, you have won a $10 voucher. Please use this code WIN2020 to claim your prize.')
    elif not win_check: # lost
      flash('Sorry, you are not a winner. Click here to enter another code.')

  except Exception as e:
    db.session.rollback()
    flash('Sorry, there was an issue. Please try again!')
  finally:
    db.session.close()

  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run(debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
