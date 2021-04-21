import random
from textblob import  TextBlob

print('Hello, Welcome to our friendly Chatbot :)')
print('What is your name?')
name = input()
print('Do you have nickname?')
ans = input()
if 'y' in ans.lower():
    nickname = input('What is your nickname ')
    print('Good to meet you ' + nickname)
else:
    nickname = name + name[-1]
    print('I will call you ' + nickname)

greetings = [
    'How are you today ' + name + '?',
    'Howdy ' + name + ' how are you feeling?',
    "What's up " + nickname + '?',
    'Greetings ' + name + ', are you well?',
    'How are things going ' + nickname + '?'
]

print(random.choice(greetings))
ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
    print('Glad you are doing well')
else:
    print('Sorry to hear that')

topics = [
    'fashion',
    'football',
    'make-up',
    'Python',
    'Computer',
    'Computer games',
    'Software'
]

questions = [
    'What is your take on ',
    'What do you think about ',
    'How do you fell about ',
    'I would like your opinion on '
]
for i in range(0, random.randint(3,4)):
    question = random.choice(questions)
    questions.remove(question)
    topic = random.choice(topics)
    topics.remove(topic)
    print(question + topic + '?')
    ans = input()
    blob = TextBlob(ans)

    if blob.polarity > 0.5:
        print('Omg ' + name + ' love ' + topic)
    elif blob.polarity > 0.1:
        print('Well, you cleary like ' + topic)
    elif blob.polarity < -0.5:
        print('My ' + nickname + ' you totally hate ' + topic)
    elif  blob.polarity < -0.1:
        print("So, you don't like " + topic)
    else:
        print('That is a very neutral view on ' + topic)

    if blob.subjectivity > 0.6:
        print('and you are so biased')
    elif blob.subjectivity > 0.3:
        print('and you are a bit biased')
    else:
        print('and quite objective')
