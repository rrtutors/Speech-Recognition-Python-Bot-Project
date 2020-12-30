import speech_recognition as sr
def takeCommand():
   r = sr.Recognizer()
   #Using microphone for listening your voice
   with sr.Microphone() as source:
     print("Please Speak.....")
     #If the user do not speak for 2 seconds it will stop listening
     r.pause_threshold = 2
     audio = r.listen(source)
   try:
   # It will recognise your voice and conver it into the text.
      print("Recognising......")
      query =r.recognize_google(audio, language='en-in')
      print(f"You said: {query}")

   except Exception as e:
    # if some problem occurred than this message will be shown
      print("say that again please")
      return None
   return query

#It will get all the information from the user by listening them &
#will store the value in thr variable
print("Please enter your name")
name= takeCommand()
print("Please enter your class")
Class= "My class is: " + takeCommand() 
print("Please enter your phone number")
phNum= "My phone number is:" + takeCommand()
print("Please tell me your hobby")
hobby= "My hobby is to play:"+ takeCommand()
print("What is your fathers name")
Fname= "My father name is:" + takeCommand()
print("What is your School Name")
SName= "My school name is: "+ takeCommand()

def openFile():
     b= name+".txt"
     #New text file will be created with the name of user.
     f= open(b,"w+")
     # Now this code will write the collected information inside the text file.
     f.write("My name is:"+name + "\r\n"+ Class + "\r\n" +phNum + "\r\n" + hobby + "\r\n" + Fname + "\r\n"+ SName )
     f.close()   
     #To open the text file in the console and read the contents
     print("Here is your text file")
     f=open(b, "r")
     if f.mode == 'r': 
            contents =f.read()
            print (contents)
    
if __name__== "__main__":
  openFile()

