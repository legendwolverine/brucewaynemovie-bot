from Flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
  return 'Greymatters'
  

if__name__=="__main__":
  app.run()
