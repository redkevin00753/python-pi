# -*- coding: utf-8 -*- # 
# by oldj http://oldj.net/ #  
import pythoncom 
import pyHook    
 
def onKeyboardEvent(event):
  # 监听键盘事件     
   print "MessageName:", event.MessageName     
   print "Message:", event.Message     
   print "Time:", event.Time     
   print "Window:", event.Window     
   print "WindowName:", event.WindowName     
   print "Ascii:", event.Ascii, chr(event.Ascii)     
   print "Key:", event.Key     
   print "KeyID:", event.KeyID     
   print "ScanCode:", event.ScanCode     
   print "Extended:", event.Extended     
   print "Injected:", event.Injected     
   print "Alt", event.Alt     
   print "Transition", event.Transition     
   print "---"           
   return True 

def main():       
   hm = pyHook.HookManager()         
   hm.KeyDown = onKeyboardEvent       
   hm.HookKeyboard()         
   hm.MouseAll = onMouseEvent       
   pythoncom.PumpMessages() 

if __name__ == "__main__":     
   main()
