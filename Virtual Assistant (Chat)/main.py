# Required Module 
import pyautogui
import pyttsx3
import webbrowser as web
import time

# Pyttsx3 initilization..
engine = pyttsx3.init()
engine.say('Hello Sir I am Virtual Assistant KeyBo which can perform any task of your Keyboard')
engine.runAndWait()

while True:
    # Command which can perform
    text = input("Enter Your Command: ")
    
    # Desktop Command means shortcut key of windows
    def Desktop_Shortcut():    
        if 'open desktop' in text.lower().strip():
            pyautogui.hotkey('win', 'd')
            
        elif 'take screenshot' in text.lower().strip():
            pyautogui.hotkey('win', 'shift', 's')      
        
        elif 'select all text' in text.lower().strip():
            time.sleep(6)
            pyautogui.hotkey('ctrl', 'a')
            
        elif 'open emoji' in text.lower().strip():
            pyautogui.hotkey('win', '.')
            
        elif 'restart driver' in text.lower().strip():
            pyautogui.hotkey('win', 'ctrl', 'shift', 'b')
            
        elif 'shutdown' in text.lower().strip():
            pyautogui.hotkey('win', 'x', 'u', 'u', 'u')
    
    # Open Web apps like Youtube....
    def Web_Apps():
        if 'open sagar channel' in text.lower().strip():
            web.open('https://www.youtube.com/@codingwithsagarcw')
            
        elif 'open harry channel' in text.lower().strip():
            web.open('https://www.youtube.com/@CodeWithHarry')
        
        elif 'open google' in text.lower().strip():
            web.open('https://google.com/')
                
        elif 'open youtube' in text.lower().strip():
            web.open('https://youtube.com/')
                
        elif 'open chatgpt' in text.lower().strip():
            web.open('https://chatgpt.com/')
        
    if __name__ == '__main__':
        Desktop_Shortcut()
        Web_Apps()
    
    # Loop End 
    if 'exit' in text.lower().strip():
        break