'''
Design a creative UI using Python's tkinter module to calculate the total cost of a pizza. 
The UI should have (at least) each widget that was covered in class:

Frames
Labels
input box
buttons
radio buttons
check boxes
You can use check boxes for for selecting toppings (each with a different cost), radio buttons for the type of crust selected 
(each with a different cost), buttons for calculation and quit. The input box can be used to record the name of the person placing the order. 
Use a message box to display the total cost of the pizza along with the name of the person placing the order.

Make sure your design is well laid out and intuitive to the user. 
Take account of spacing and packing so that everything is properly aligned and professional looking. 
Be creative with font, color, size, etc.
'''
import tkinter
import tkinter.messagebox
from turtle import right

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x300')
        self.main_window.configure(bg='green')
        
        self.main_window.title("Blake's Pizza")
        self.top_frame = tkinter.Frame(self.main_window)
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.test4_frame = tkinter.Frame(self.main_window)
        self.output_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #check boxes
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text="Sausage",
                                        variable=self.cb_var1)
        
        self.cb2 = tkinter.Checkbutton(self.top_frame, text="Pepperoni",
                                        variable=self.cb_var2)

        self.cb3 = tkinter.Checkbutton(self.top_frame, text="Chicken",
                                        variable=self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        #RadioButtons
        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.test4_frame,
                                        text='8 inch crust',
                                         variable=self.radio_var,
                                         value=10)
        
        
        self.rb2 = tkinter.Radiobutton(self.test4_frame,
                                        text='10 inch crust',
                                         variable=self.radio_var,
                                         value=20)
        
        
        self.rb3 = tkinter.Radiobutton(self.test4_frame,
                                        text='16 inch crust',
                                         variable=self.radio_var,
                                         value=30)
        



        self.label1 = tkinter.Label(self.test1_frame, 
                                    text=" Welcome to Blake's Pizza! Enter name for order:")
        self.label2 = tkinter.Label(self.test2_frame, 
                                    text="Select toppings")
        self.label3 = tkinter.Label(self.test3_frame, 
                                    text="Select type of crust:")    

        #self.descr_label = tkinter.Label(self.output_frame,
                                            #text="Average:") 
        self.name = tkinter.Entry(self.test1_frame,width=15) 
        #self.test2 = tkinter.Entry(self.test2_frame,width=10)
        #self.test3 = tkinter.Entry(self.test3_frame,width=10)

        self.avg_var = tkinter.StringVar()

        self.avg_label = tkinter.Label(self.output_frame,
                                            textvariable=self.avg_var)

        #self.mybutton = tkinter.Button(self.main_window,
                                       # text='Average',
                                        #command= self.convert)
        self.mybutton1 = tkinter.Button(self.main_window,
                                        text='Checkout',
                                        command= self.do_something)

        self.quit_button = tkinter.Button(self.main_window,
                                            text='Quit',
                                            command=self.main_window.destroy)
        
        
        self.test1_frame.pack(side='top')
        self.test2_frame.pack(side='top')
        self.top_frame.pack(side='left')
        
        self.test3_frame.pack(side='left')

        self.output_frame.pack(side='top')
        self.test4_frame.pack(side='top')
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.bottom_frame.pack(side='bottom')

        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')
        #self.descr_label.pack(side='top')
        self.avg_label.pack(side='right')
        self.quit_button.pack(side='right')
        #self.mybutton.pack(side='left')

        self.mybutton1.pack(side='bottom')
        self.name.pack(side='top')
        #self.test2.pack(side='right')
        #self.test3.pack(side='right')
        

        tkinter.mainloop()

    #messagebox   
    def do_something(self):
        
        self.message = 'Thanks ' + self.name.get() +'\n' + 'Your Total Cost is:\n'
         
        price = 0
        if self.cb_var1.get() == 1:
            #self.message += 'Sausage\n'
            price += 2
        if self.cb_var2.get() == 1:
            #self.message += 'Pepperoni\n'
            price +=3
        if self.cb_var3.get() == 1:
            #self.message += 'Chicken\n'
            price +=4
        if self.radio_var.get() == 10:
            price+=10
        if self.radio_var.get() == 20:
            price+=12
        if self.radio_var.get() == 30:
            price+=14
        
        tkinter.messagebox.showinfo('Response', self.message + '${:,.2f}'.format(price))
my_gui = MyGUI()          