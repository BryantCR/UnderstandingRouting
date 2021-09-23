from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route( '/dojo' )
def dojo():
    return 'Dojo!'
#------------------------------PART II
@app.route('/say/flask')
def hiFlask():
    return 'Hi Flask!'

@app.route('/say/michael')
def hiMichael():
    return 'Hi Michael!'

@app.route('/say/jonh')
def hiJonh():
    return 'Hi Jonh!'

#------------------------------PART III
@app.route('/repeat/35/hello')
def sayHello():
    hello = ""
    for i in range (1, 36, 1)
        print("hello")
    return 'Hi Flask!'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

#URL: http://127.0.0.1:5000