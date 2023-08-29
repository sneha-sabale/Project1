import speech_recognition as sr
import webbrowser
import os


TT=0
while 1:
    

    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source

        r.adjust_for_ambient_noise(source)
        print('JARVIS IS LISTENING...\n')
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    try:
        print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition

        WRODD=r.recognize_google(audio)
        Task=WRODD.split()
        Task1=Task[0]
        Task2=Task[1]
        if Task1=='Wikipedia':#Wikipedi Tendulkar
            Search_Query=Task2
            # finding result for the search
            # sentences = 2 refers to numbers of line
            result = wikipedia.summary(Search_Query, sentences = 2)

            # printing the result
        print(result,'\n')
        elif
        Task1=='Gmail': #Gmail Open:
            print('Opening Gmail')
            url='https://accounts.google.com/'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            #webbrowser.open_new_tab('https://accounts.google.com/')

        elif Task1=='YouTube': #Youtube Open:
            print('Opening Trending Youtube')
            url='https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif Task1=='Notepad': #Notepad Open:
            os.system('notepad')

        elif Task1=='CMD': #cmd Open:
            os.system('cmd')

        elif Task1=='paint': #PAINT Open:
            os.system('mspaint')

    except:
        print('NONE')
