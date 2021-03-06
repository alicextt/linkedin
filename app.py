from flask import Flask, render_template, request
from query_tools import *
from query_api import *
import logging,logging.config, yaml
logging.config.dictConfig(yaml.load(open('logging.conf')))

app = Flask(__name__,  template_folder='client', static_folder='client/static')
import json

fakepeers={
  "links": [
    {"link": {
    "Title": "Software Engineer",
    "img_url":"https://media.licdn.com/mpr/mpr/shrinknp_400_400/p/4/005/042/1a1/08b48ac.jpg",
    "profile_url": "https://www.linkedin.com/profile/view?id=ADEAAAauYmQBGwCTxbICPCV-k53MsxyYuaGiOyw"
  }},{"link": {
    "Title": "Software Developer",
     "img_url":"https://media.licdn.com/mpr/mpr/shrinknp_400_400/AAEAAQAAAAAAAAMPAAAAJDQwMmRiMGJlLWNkNTgtNDAxNC1hN2UwLTNmNjY3OGEwYmRiNA.jpg",
    "profile_url": "https://www.linkedin.com/profile/view?id=ADEAAAS-uHMBmmfUr8-urMQ0GGDu9odW3VYjK1w"

  }},
    {"link": {
    "Title": "Software Developer",
     "img_url":"http://www.utexas.edu/cola/history/_files/images/people/graduation_speakers/ryan_maidie.jpg",
    "profile_url": "https://www.linkedin.com/profile/view?id=ADEAAA93W-MBpZgbhfh6gD2mcvbXZmVNZ9DurXs"
  }}
  ]
}
# mysql = MySQL()

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'glass'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    data = request.data
    data = json.loads(data)
    url = data.get('url')
    logconsole.debug(url)
    if url:
        r = search_query(url)
        logconsole.debug(r)
        return json.dumps(r)
    else:
        return "error"
    

if __name__ == '__main__':
    logfile    = logging.getLogger('file')
    logconsole = logging.getLogger('console')
    logfile.debug("Debug FILE")
    logconsole.debug("Debug CONSOLE")
    app.run()
    # app.run(host='0.0.0.0')
