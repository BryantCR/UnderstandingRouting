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
    
@app.route('/say/<name>', methods = ['GET'])
def hiName( name ):
    return 'Hi '+ name

#------------------------------PART III
# @app.route('/repeat/35/hello')
# def sayHello():
#     hello = ""
#     for i in range (1, 36, 1):
#         hello = hello +
#     return hello

# @app.route('/repeat/80/bye')
# def sayBye():
#     hello = ""
#     for i in range (1, 81, 1):
#         print("bye")
#     return 'Hi Flask!'

# @app.route('/repeat/99/dog')
# def sayDog():
#     hello = ""
#     for i in range (1, 100, 1):
#         print("dog")
#     return 'Hi Flask!'

@app.route('/repeat/<num>/<word>')
def repeatNumWord(num, word):
    number = int(num)
    wordDigited = str(word)
    wordRepeated = ""
    for i in range (0, number, 1):
        wordRepeated = wordRepeated + '<h1>' + word + '</h1>'
    return wordRepeated

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

#URL: http://127.0.0.1:5000

# @app.route('/repeat/<number>/<word>')
# def repeat(number,word):
#     number = int(number)
#     repeatWord = '' 
#     for i in range (number):
#         repeatWord +='<h1>'+ word + '</h1>'
#     return repeatWord
