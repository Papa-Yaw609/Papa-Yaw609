from curses.textpad import Textbox
from msilib.schema import Font
from  tkinter import *
from socket import *




def initialize_server():
    #initialise socket
    s = socket(AF_INET, SOCK_STREAM)
    #config details of server
    host ='localhost' 
    port = 1234
    s.bind((host,port))
    #set the number of clients
    s.listen(1)
    #accept the connection
    conn,addr =s.accept()

    return conn

def update_chat(msg,state,chatlog):
    chatlog.config(state=NORMAL)
    #Update msg
    if state == 0:
        chatlog.insert(END, 'YOU: ' + msg)
    else:
        chatlog.insert(END,'OTHER: ' + msg)
    chatlog.config(state=DISABLED)
    #SHOW LATEST MSG
    chatlog.yview(END)



def send(textbox,update_chat):
    msg = textbox.get("0.0",END)
    update_chat(msg,0)
    #send msg
    conn.send(msg.encode('ascii'))
    textbox.delete("0.0,END")


#fun to receive msg
def receive(update_chat):
    while 1:
        try:
            data = conn.recv(1024)
            msg =data.decode('ascii')
            if msg !="":
                update_chat(msg,1)
        except:
            pass


def GUI():
    gui = Tk()
    gui.title("Client Chat")
    gui.geometry("380x430") #the size of the box
    #TEXT SPACE TO DISPLAY MESSAGE
    chatlog = Text(gui, bg='white')
    chatlog.config(state=DISABLED)

    sendbutton = Button(gui,bg='blue',fg='black',font='bold',text='SEND', command='send')


    #textbox for the messages
    textbox =Text(gui, bg='white', width='30',height='8')
    

    #place the component in the window
    chatlog.place(x=6,y=6,height=386,width=370 )
    textbox.place(x=6,y=401,height=20,width=265)
    sendbutton.place(x=300,y=401,height=20,width=50 )


    gui.mainloop()  










if __name__ == '__main__':
    conn = initialize_server()
    GUI()



