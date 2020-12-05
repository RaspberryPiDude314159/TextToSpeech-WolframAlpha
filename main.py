import pyttsx3
from exchanges.bitfinex import Bitfinex
from datetime import datetime
import wolframalpha 
engine = pyttsx3.init()

engine.say("Welcome. Type a command to get started.")
engine.runAndWait()
def commands():
    print("------------------------------------\nCommands: \n'query' to fetch the answer to a question\n'time' to fetch the time \n'bitcoin' to fetch the current bitcoin price in dollars\n'speak' to make the computer say a message\n-------------------------------")
#Main game loop
command = 1
commands()
while True:
    typed = input()

    #Fetches and speaks bitcoin price

    if typed == "bitcoin" and command == 1:
        variable = Bitfinex().get_current_price()
        print(variable)
        engine.say(str(variable))
        engine.runAndWait()
        commands()

    #Fetches and speaks time

    elif typed == "time" and command == 1:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        hour = now.strftime("%H")
        if int(hour) < 13:
            ampm = " AM"
            ampmsay = " Ay Em."
        else:
            ampm = " PM"
            ampmsay = " Pee Em."
        print("Time is ",str(current_time),ampm)
        timeis = "Time is ",str(current_time), ampmsay
        engine.say(str(timeis))
        engine.runAndWait()
        commands()
    #Speaks message inputted

    elif typed == "speak" and command == 1:
        command = 0
        print("Type message")
        sayvar = input()
        engine.say(str(sayvar))
        engine.runAndWait()
        print("Message spoken.")
        command = 1
        commands()

    #Fetches answer to query

    elif typed == "query" and command ==1:
        command = 0
        engine.say("Input query:")
        engine.runAndWait()
        question = input('Question: ')
        print(question)
        try:
            app_id = "JG3LQW-4QU5YYX8YP"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text 
  
            print(answer)
            engine.say(str(answer))
            engine.runAndWait()
        except:
            print("An error occurred, try making the statement shorter or less complex.")
            engine.say("An error occurred.")
            engine.runAndWait()
        finally:
            command = 1
            commands()

    #Else

    else:
        if command == 1:
            print("Command not recognised. Did you make a typo?")
            engine.say("Command not recognised.")
            engine.runAndWait()
            commands()
