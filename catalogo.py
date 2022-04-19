from flask import Flask, render_template #llamamos a la libreria Flask y al archivo templeates

app = Flask(__name__) #creamos una variable 
#Main route
@app.route("/")
def home():
    return render_template('PWindex.html')

@app.route("/aboutme")
def about():
    return render_template('about.html')
    
@app.route("/tgraficas")
def graficas():
    return render_template('graficas.html')
   
if __name__ == "__main__":
    app.run(debug=True) #ponemos nuestra web en modo prueba

