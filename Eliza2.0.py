import random 
import re
import sys
import speech_recognition as sr
import pyttsx
##########################################################################################################################################################################################################################################################
engine_one = pyttsx.init()
engine = pyttsx.init()
record = sr.Recognizer()
##########################################################################################################################################################################################################################################################
class Eliza(object):
    def __init__(self):
        self.reflections = {
            "am": "are",
            "was": "were",
            "i": "you",
            "i'd": "you would",
            "i've": "you have",
            "i'll": "you will",
            "my": "your",
            "are": "am",
            "you've": "I have",
            "you'll": "I will",
            "your": "my",
            "yours": "mine",
            "you": "me",
            "me": "you"
        }

        self.psychobabble = [
            [r'I need (.*)',
            ["Why do you need {0}?",
            "Would it really help you to get {0}?",
            "Are you sure you need {0}?"]],

            [r'Why don\'?t you ([^\?]*)\??',
            ["Do you really think I don't {0}?",
            "Perhaps eventually I will {0}.",
            "Do you really want me to {0}?"]],

            [r'Why can\'?t I ([^\?]*)\??',
            ["Do you think you should be able to {0}?",
            "If you could {0}, what would you do?",
            "I don't know -- why can't you {0}?",
            "Have you really tried?"]],

            [r'I can\'?t (.*)',
            ["How do you know you can't {0}?",
            "Perhaps you could {0} if you tried.",
            "What would it take for you to {0}?"]],

            [r'I am (.*)',
            ["Did you come to me because you are {0}?",
            "How long have you been {0}?",
            "How do you feel about being {0}?"]],

            [r'I\'?m (.*)',
            ["How does being {0} make you feel?",
            "Do you enjoy being {0}?",
            "Why do you tell me you're {0}?",
            "Why do you think you're {0}?"]],

            [r'Are you ([^\?]*)\??',
            ["Why does it matter whether I am {0}?",
            "Would you prefer it if I were not {0}?",
            "Perhaps you believe I am {0}.",
            "I may be {0} -- what do you think?"]],

            [r'What (.*)',
            ["Why do you ask?",
            "How would an answer to that help you?",
            "What do you think?"]],

            [r'How (.*)',
            ["How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?"]],

            [r'Because (.*)',
            ["Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "If {0}, what else must be true?"]],

            [r'(.*) sorry (.*)',
            ["There are many times when no apology is needed.",
            "What feelings do you have when you apologize?"]],

            [r'Hello(.*)',
            ["Hello... I'm glad you could drop by today.",
            "Hi there... how are you today?",
            "Hello, how are you feeling today?"]],

            [r'I think (.*)',
            ["Do you doubt {0}?",
            "Do you really think so?",
            "But you're not sure {0}?"]],

            [r'(.*) friend (.*)',
            ["Tell me more about your friends.",
            "When you think of a friend, what comes to mind?",
            "Why don't you tell me about a childhood friend?"]],

            [r'Yes',
            ["You seem quite sure.",
            "OK, but can you elaborate a bit?"]],

            [r'(.*) computer(.*)',
            ["Are you really talking about me?",
            "Does it seem strange to talk to a computer?",
            "How do computers make you feel?",
            "Do you feel threatened by computers?"]],

            [r'Is it (.*)',
            ["Do you think it is {0}?",
            "Perhaps it's {0} -- what do you think?",
            "If it were {0}, what would you do?",
            "It could well be that {0}."]],

            [r'It is (.*)',
            ["You seem very certain.",
            "If I told you that it probably isn't {0}, what would you feel?"]],

            [r'Can you ([^\?]*)\??',
            ["What makes you think I can't {0}?",
            "If I could {0}, then what?",
            "Why do you ask if I can {0}?"]],

            [r'Can I ([^\?]*)\??',
            ["Perhaps you don't want to {0}.",
            "Do you want to be able to {0}?",
            "If you could {0}, would you?"]],

            [r'You are (.*)',
            ["Why do you think I am {0}?",
            "Does it please you to think that I'm {0}?",
            "Perhaps you would like me to be {0}.",
            "Perhaps you're really talking about yourself?"]],

            [r'You\'?re (.*)',
            ["Why do you say I am {0}?",
            "Why do you think I am {0}?",
            "Are we talking about you, or me?"]],

           [r'I don\'?t (.*)',
           ["Don't you really {0}?",
           "Why don't you {0}?",
           "Do you want to {0}?"]],

           [r'I feel (.*)',
           ["Good, tell me more about these feelings.",
           "Do you often feel {0}?",
           "When do you usually feel {0}?",
           "When you feel {0}, what do you do?"]],

           [r'I have (.*)',
           ["Why do you tell me that you've {0}?",
           "Have you really {0}?",
           "Now that you have {0}, what will you do next?"]],

           [r'I would (.*)',
           ["Could you explain why you would {0}?",
           "Why would you {0}?",
           "Who else knows that you would {0}?"]],

           [r'Is there (.*)',
           ["Do you think there is {0}?",
           "It's likely that there is {0}.",
           "Would you like there to be {0}?"]],

           [r'My (.*)',
           ["I see, your {0}.",
           "Why do you say that your {0}?",
           "When your {0}, how do you feel?"]],

           [r'You (.*)',
           ["We should be discussing you, not me.",
           "Why do you say that about me?",
           "Why do you care whether I {0}?"]],

           [r'Why (.*)',
           ["Why don't you tell me the reason why {0}?",
           "Why do you think {0}?"]],

           [r'I want (.*)',
           ["What would it mean to you if you got {0}?",
           "Why do you want {0}?",
           "What would you do if you got {0}?",
           "If you got {0}, then what would you do?"]],

           [r'(.*) mother(.*)',
           ["Tell me more about your mother.",
           "What was your relationship with your mother like?",
           "How do you feel about your mother?",
           "How does this relate to your feelings today?",
           "Good family relations are important."]],

           [r'(.*) father(.*)',
           ["Tell me more about your father.",
           "How did your father make you feel?",
           "How do you feel about your father?",
           "Does your relationship with your father relate to your feelings today?",
           "Do you have trouble showing affection with your family?"]],

           [r'(.*) child(.*)',
           ["Did you have close friends as a child?",
           "What is your favorite childhood memory?",
           "Do you remember any dreams or nightmares from childhood?",
           "Did the other children sometimes tease you?",
           "How do you think your childhood experiences relate to your feelings today?"]],

           [r'(.*)\?',
           ["Why do you ask that?",
           "Please consider whether you can answer your own question.",
           "Perhaps the answer lies within yourself?",
           "Why don't you tell me?"]],

           [r'quit',
           ["Thank you for talking with me.",
           "Good-bye.",
           "Thank you, that will be $150.  Have a good day!"]],

           [r'(.*)',
           ["Please tell me more.",
           "Let's change focus a bit... Tell me about your family.",
           "Can you elaborate on that?",
           "Why do you say that {0}?",
           "I see.",
           "Very interesting.",
           "{0}.",
           "I see.  And what does that tell you?",
           "How does that make you feel?",
           "How do you feel when you say that?"]]
           ]

        self.__gender = 'female'
        self.__age = 21
        
        self.select_gender(self.__gender)
        self.set_gender(self.get_gender())
        self.set_speech_rate()


    def reflect(self, fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if token in self.reflections:
                tokens[i] = self.reflections[token]
        return ' '.join(tokens)

    def analyze(self, statement):
        for pattern, responses in self.psychobabble:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
        return engine_one.say(response.format(*[self.reflect(g) for g in match.groups()]))

    def select_gender(self, sex):
        self.__gender = sex
    
    def set_gender(self, sex):
        if sex == 'female' and sys.platform == 'linux2':
            voices = engine.getProperty('voices')
            engine.setProperty('voice', 'english+f2')
    
    def get_gender(self):
        return self.__gender

    def set_speech_rate(self):
        rate = engine.getProperty('rate')
        rate_two = engine_one.getProperty('rate')
        engine.setProperty('rate', rate-40)
        engine_one.setProperty('rate', rate-40)
        

    
    def test_voices():
        engine = pyttsx.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            engine.setProperty('voice', voice.id)
            engine.say('The quick brown fox jumped over the fence')

    class ElizaSpeak(object):
        def __init__(self):
            pass

        def init_mini(self):
            engine.connect('finished-utterance', self.onEnd)
            engine.say('Hello, how are you today?')
            engine.startLoop()

        def onEnd(self, name, completed):
            engine.endLoop()
    
    class UserSpeak(object):
        def __init(self):
            pass
        
        def accept_speech_input(self):
            with sr.Microphone() as source:
                audio = record.listen(source)
            try:
                pass
            except sr.UnknownValueError:
                print('Eliza has failed to recognize your speech. Please try again')
                self.accept_speech_input()
            except sr.RequestError as e:
                print("Eliza error; {0}".format(e))
            return record.recognize_sphinx(audio)
    
    

##########################################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################################
e = Eliza()
es = Eliza.ElizaSpeak()
us = Eliza.UserSpeak()

def main():
    while True:
        statement = raw_input("> ")
        e.analyze(statement)
        if statement == "quit":
            break
        elif statement == 'pause':
            print(us.accept_speech_input())
            
            
def main_speak():
    while True:
        statement = us.accept_speech_input()
        e.analyze(statement)
        if statement == 'quit':
            break
       
es.init_mini()

##########################################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################################
print('Type voice for voice mode or text for text mode: ')
var = raw_input('> ')
if var == 'voice':
    main_speak()
elif var == 'text':
    main()
    
    
'''
Requirements and instructions:

In order to use this, you need the following packages ( marked with an * )

Please follow these install procedures IN ORDER, if not bundled into an .exe (an install script can be made)

*Python 2.7 (comes by dfault with all linux distros. Arch linux uses python 3+ but should still come with a 2.7 version, check your system before installing this)
*python -m pip install pyttsx
*python -m pip install SpeechRecognition
*sudo apt-get install libasound-dev
*PortAudio (Download it here: http://www.portaudio.com/download.html , then follow these instructions: http://portaudio.com/docs/v19-doxydocs/compile_linux.html )
*python -m pip install PyAudio
*sudo apt-get install build-essential libpcre3-dev
*python -m pip install pep8 (can be forced with sudo -H python -m pip install pep8) Run python -m pip list to check if pep8 exists already
*sudo apt-get install automake byacc flex
*swig
    on some systems running sudo apt-get install gcc automake autoconf libtool bison swig python-dev libpulse-dev 
    can get everything that you need. Which means the following steps upto (*PocketSphinx) can be skipped.

    Steps to install swig: git clone https://github.com/swig/swig.git 
                           cd swig 
                           ./autogen.sh && ./configure && make
                      
*python -m pip install PocketSphinx

For windows or mac based systems you'll need a FLAC encoder. You're own your own there.
'''

'''
Notes on Voice input:

The latency between the users voice commands and the program responding is noticeable. It can be fixed in a variety of ways and I'll work on that now...

Sphinx is NOT the best for this. If you speak in a normal speaking voice and try to make it clear it does accuratley interpret what you say.

The key thing in this stage is that the logner you speak the longer it takes her to respond!

'''
