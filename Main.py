from __future__ import print_function, unicode_literals
import sys
from sty import *
from whaaaaat import *

from Config import Config
from Store import Store

from twitter.training import Main as TwitterTrainer
from imdb.training import Main as IMDBTrainer

fg.red = ('rgb', (255, 157, 0))

style = style_from_dict({
    Token.QuestionMark: '#FF9D00 bold',
    Token.Question: '#FF9D00 bold',
    Token.Instruction: '#263238',
})


def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def watermark():
    clear()
    print("   _____            _   _                      _                          _           _      ")
    print("  / ____|          | | (_)                    | |       /\               | |         (_)     ")
    print(" | (___   ___ _ __ | |_ _ _ __ ___   ___ _ __ | |_     /  \   _ __   __ _| |_   _ ___ _ ___  ")
    print("  \___ \ / _ \ '_ \| __| | '_ ` _ \ / _ \ '_ \| __|   / /\ \ | '_ \ / _` | | | | / __| / __| ")
    print("  ____) |  __/ | | | |_| | | | | | |  __/ | | | |_   / ____ \| | | | (_| | | |_| \__ \ \__ \ ")
    print(" |_____/ \___|_| |_|\__|_|_| |_| |_|\___|_| |_|\__| /_/    \_\_| |_|\__,_|_|\__, |___/_|___/ ")
    print("                                                                             __/ |           ")
    print("                                                                            |___/            ")
    print("                                                                                             ")
    print("                                                                              by EL AMRI Ali ")
    print()

    recap()


def recap():
    if Config.action:
        print(fg.green + "Action:\t\t" + fg.rs + Config.action.title() + "\n")

    if Config.corpus:
        print(fg.green + "Corpus:\t\t" + fg.rs + Config.corpus.title() + "\n")

    if Config.classifiers:
        print(fg.green + "Classifiers:\t" + fg.rs + "\n\t\t".join(
            classifier['name'] for classifier in Config.classifiers) + "\n")


def classifiers_picker(error=False):
    watermark()

    if error:
        print(fg.red + "(!) You must pick at least one classifier.\n" + fg.rs)

    print("Multiple classifiers will be ran into a voting system.\n")

    questions = [
        {
            'type': 'checkbox',
            'message': 'Select classifiers',
            'name': 'classifiers',
            'choices': Store.classifiers,
        }
    ]

    answers = prompt(questions, style=style)

    if answers and len(answers['classifiers']) == 0:
        classifiers_picker(error=True)

    if answers and len(answers['classifiers']):
        get_classifiers(answers['classifiers'])


def get_classifiers(classifiers_names):
    for classifier in Store.classifiers:
        for classifier_name in classifiers_names:
            if classifier['name'] == classifier_name:
                Config.classifiers.append(classifier)


def corpus_picker():
    watermark()

    questions = [
        {
            'type': 'rawlist',
            'message': 'Select a corpus',
            'name': 'corpus',
            'choices': [
                'IMDb: Formal-ish with positive & negative classifications',
                'Twitter: Informal with positive, negative & neutral classifications'
            ],
            'filter': lambda val: val.lower().split(':')[0]
        }
    ]

    answers = prompt(questions, style=style)

    if answers and len(answers['corpus']):
        Config.corpus = answers['corpus']


def action_picker():
    watermark()

    questions = [
        {
            'type': 'rawlist',
            'message': 'Which action do you wish to perform',
            'name': 'action',
            'choices': [
                'Training: Train the classifiers using the corpus.',
                'Testing: Assess the classifiers\' accuracy using the corpus.',
                'Analyzing: Analyze the Sentube data set using the classifiers and the corpus'
            ],
            'filter': lambda val: val.lower().split(':')[0]
        }
    ]

    answers = prompt(questions, style=style)

    if answers and len(answers['action']):
        Config.action = answers['action']


def perform_action():
    watermark()

    action = Config.action

    if action == 'training':
        train()
    if action == 'testing':
        test()
    if action == 'analyzing':
        analyze()


def train():
    if Config.corpus == 'twitter':
        TwitterTrainer.run()
    if Config.corpus == 'imdb':
        IMDBTrainer.run()


def test():
    print("Test")
    print(Config.action)
    print(Config.corpus)
    print(Config.classifiers)


def analyze():
    print("Analyze")
    print(Config.action)
    print(Config.corpus)
    print(Config.classifiers)


classifiers_picker()

if Config.classifiers:
    corpus_picker()

if Config.corpus:
    action_picker()

if Config.action:
    perform_action()
