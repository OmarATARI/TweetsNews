from flask import (Flask, Response, request, jsonify, render_template)

# from forms import ExportForm

from flask import Flask, render_template

from models import Tweet

app = Flask(__name__)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pwd@localhost/tweets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def accueil():
    return render_template('accueil.html')


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


# @app.route('/visualization/moment')
# def visualization():
#   try:
#     img = io.BytesIO()
#     tweets = session.query(Tweet).all()
#     data = [t.serialize() for t in tweets]

#     used_data = {'tweet_id': [], 'moment_broadcast': []}
#     for d in data:
#       used_data['tweet_id'].append(d['id'])
#       used_data['moment_broadcast'].append(d['type'])

#     df = pd.DataFrame(used_data, columns=['tweet_id', 'moment_broadcast'])
#     df["moment_broadcast"].value_counts().plot(kind='pie')

#     plt.savefig(img, format='png')
#     img.seek(0)
#     plot_url = base64.b64encode(img.getvalue()).decode()

#     return '<img src="data:image/png;base64,{}">'.format(plot_url)

#   except Exception as e:
#     return(str(e))

# def parse_datetime(str_date) -> datetime:
#   """
#     Parse a datetime string with the format %Y-%m-%d %H:%M:%S

#     Parameters
#     ----------
#     str_date : str
#       the datetime

#     Returns
#     -------
#     datetime
#   """
#   return datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')

# @app.route('/search')
# def search():
#   output = StringIO()
#   cw = csv.DictWriter(output,
#     fieldnames=['id', 'utc_date', 'local_datetime', 'tweet', 'tweet_id', 'language', 'timezone', 'type'])
#   cw.writeheader()

#   start_datetime = parse_datetime(request.args.get('day_start')+ ' ' + request.args.get('hour_start'))
#   end_datetime = parse_datetime(request.args.get('day_end')+ ' ' + request.args.get('hour_end'))
#   tweets = session.query(Tweet).filter(Tweet.utc_date <= end_datetime, Tweet.utc_date >= start_datetime)
#   data = [t.serialize() for t in tweets]

#   for d in data:
#     cw.writerow(d)

#   return Response(output.getvalue(), mimetype="text/csv")

# @app.route('/export')
# def export():
#   form = ExportForm()
#   return render_template('export.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
