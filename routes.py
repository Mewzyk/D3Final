# add your project directory to the sys.path
project_home = u'/home/Mewzyk/app'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path
    
from flask import Flask, render_template
 
application = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')
 
@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)