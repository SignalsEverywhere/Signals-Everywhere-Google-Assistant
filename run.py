from flask import Flask
from flask_assistant import Assistant, ask, tell, context_manager
import logging
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
from Plugins import hamCall

app = Flask(__name__)
assist = Assistant(app, route='/')


@assist.action('Welcome')
def greet_and_start():
    speech = "Hello, this is Signals everywhere. What can I do for you?"
    return ask(speech)

@assist.action('callsign', mapping={'callsign': 'sys.any'})
def lookup(callsign):
    phonetics = hamCall.convert(callsign.lower()).split()
    call = [word[0] for word in phonetics]
    result = hamCall.callsign_start("".join(call))
    speech = result
    print(str(callsign))
    return ask(speech)

@assist.action('repeater', mapping={'repeat': 'sys.any'})
def repeat_test(repeat):
    speech = 'You said ' + str(repeat)
    return ask(speech)

@assist.action('what')
def what_are_commands(what):
    speech = 'You can ask to lookup a callsign, at the moment it only works for U S calls.'
    return ask(speech)



if __name__ == '__main__':
    app.run(debug=True)
