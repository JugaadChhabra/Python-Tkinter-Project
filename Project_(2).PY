                                                                                ##FLY HIGH##
from tkinter import *   
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import date
from PIL import ImageTk, Image  




global total_pass

user_name=""
departure = ""
arrival= ""
ticket_price=0
total=0
chosen_item_name=[]
chosen_item_qty=[]
chosen_item_price=[]
date = ""
ticket_duration = ""
ticket_departure = ""
ticket_arrival = ""
ticket_airline = ""
final_ticket_price = 0
first_name_1=""
second_name_1 = ""
first_name_2 = ""
second_name_2 = ""
final_first_name_3 = ""
final_second_name_3 = ""
final_first_name_4 = ""
final_second_name_4 = ""
total_seat = 0
seat_total_count = 0

def frame_3_next():
    global total
    global pass1_firstname
    global pass1_lastname
    global gender_1
    if (gender_1.get() == ""):
        messagebox.showerror("","Select a Gender")
    if (pass1_firstname.get() == ""): 
        messagebox.showerror("","Enter Name")
    elif (pass1_lastname.get() == ""):
        messagebox.showerror("","Enter Name")
    elif (pass1_firstname.get() != "") and (pass1_lastname.get() != "") and (gender_1.get() != "") :
        show_frame(frame5)

def frame_4_next():
    frame_3_next()
    global pass2_firstname
    global pass2_lastname
    if (pass2_firstname.get() == ""):
        messagebox.showerror("","Enter Name")
    elif (pass2_lastname.get() == ""):
        messagebox.showerror("","Enter Name")
    elif (pass2_firstname.get() != "") and (pass2_lastname.get() != ""):
        show_frame(frame5)

def second_passenger():
    global total
    global pass1_firstname
    global pass1_lastname
    global gender_1
    if (gender_1.get() == ""):
        messagebox.showerror("","Select a Gender")
    if (pass1_firstname.get() == ""): 
        messagebox.showerror("","Enter Name")
    elif (pass1_lastname.get() == ""):
        messagebox.showerror("","Enter Name")
    elif (total == 1):
        messagebox.showerror("","Only one Passenger Selected")
    elif (pass1_firstname.get() != "") and (pass1_lastname.get() != "") and (total > 1) and (gender_1.get() != ""):
        show_frame(frame4)

def third_passenger():
    global total
    global pass2_firstname
    global pass2_lastname
    global gender_2
    if (gender_2.get() == ""):
        messagebox.showerror("","Select a Gender")
    if (pass2_firstname.get() == ""):
        messagebox.showerror("","Enter Name")
    elif (total == 2):
        messagebox.showerror("","Only two Passengers Selected")
    elif (pass2_lastname.get() == ""):
        messagebox.showerror("","Enter Name")
    elif (pass2_firstname.get() != "") and (pass2_lastname.get() != "") and (total > 2) and (gender_2.get() != ""):
        show_frame(passenger_3_frame)

def fourth_passenger():
    global total
    global pass3_firstname
    global pass3_lastname
    global gender_3
    if (gender_3.get() == ""):
        messagebox.showerror("","Select a Gender")
    if (pass3_firstname.get() == ""):
        messagebox.showerror("","Enter Name")
    elif (total == 3):
        messagebox.showerror("","Only three Passengers Selected")
    elif (pass3_lastname.get() == ""):
        messagebox.showerror("","Enter Name")
    elif (pass3_firstname.get() != "") and (pass3_lastname.get() != "") and (total > 3) and (gender_3.get() != ""):
        show_frame(passenger_4_frame)

def open_window():
    ticket()
    if total == 1 :

        new_window = Toplevel(root,bg="white")
        new_window.geometry("600x300")

        ticket_label = Label(new_window,text="Ticket",bg="white",fg="black")
        ticket_label["font"] = ("Consolas",18,"bold")
        ticket_label.place(x=10,y=5)

        dash_label1 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label1["font"] = ("Consolas",8,"bold")
        dash_label1.place(x=10,y=30)

        dash_label2 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label2["font"] = ("Consolas",8,"bold")
        dash_label2.place(x=10,y=70)

        final_from = Label(new_window,textvariable=var_final_from_to,bg="white",fg="black")
        final_from["font"] = ("Consolas",13,"bold")
        final_from.place(x=10,y=50)

        flight_number = Label(new_window,text="6E-5914",bg="white",fg="grey")
        flight_number["font"] = ("Consolas",8)
        flight_number.place(x=10,y=120)

        ticket_d1 = Label(new_window,textvariable=ticket_date,bg="white",fg="grey")
        ticket_d1["font"] = ("Consolas",8)
        ticket_d1.place(x=180,y=120)

        final_duration = Label(new_window,textvariable=var_final_duratoin,bg="white",fg="grey")
        final_duration["font"] = ("Consolas",8)
        final_duration.place(x=323,y=120)

        economy_label = Label(new_window,text="Economy",bg="white",fg="grey")
        economy_label["font"] = ("Consolas",8)
        economy_label.place(x=320,y=140)

        ticket_d2 = Label(new_window,textvariable=ticket_date,bg="white",fg="grey")
        ticket_d2["font"] = ("Consolas",8)
        ticket_d2.place(x=430,y=120)

        final_arrival = Label(new_window,textvariable=var_final_arrival,bg="white",fg="black")
        final_arrival["font"] = ("Consolas",13,"bold")
        final_arrival.place(x=400,y=100)

        final_departure = Label(new_window,textvariable=var_final_departure,bg="white",fg="black")
        final_departure["font"] = ("Consolas",13,"bold") 
        final_departure.place(x=150,y=100)

        final_airline = Label(new_window,textvariable=var_final_airline,bg="white",fg="black")
        final_airline["font"] = ("Consolas",13,"bold")
        final_airline.place(x=10,y=100)

        baggage_label = Label(new_window,text="Baggage: Check-in: 15 kg, Cabin: 7kg",bg="white",fg="grey")
        baggage_label["font"] = ("Consolas",8)
        baggage_label.place(x=10,y=170)

        travellers_label = Label(new_window,text="TRAVELLERS",bg="white",fg="black")
        travellers_label["font"] = ("Consolas",11,"bold")
        travellers_label.place(x=20,y=210)

        dash_label3 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label3["font"] = ("Consolas",8,"bold")
        dash_label3.place(x=10,y=190)

        dash_label4 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label4["font"] = ("Consolas",8,"bold")
        dash_label4.place(x=10,y=230)

        dash_label5 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label5["font"] = ("Consolas",8,"bold")
        dash_label5.place(x=10,y=270)

        first_name_1 = passenger1_firstname_textbox.get()
        second_name_1 = passenger1_lastname_textbox.get()
        var_name_1.set(f"{first_name_1} {second_name_1}")
        f_name_1 = Label(new_window,textvariable=var_name_1,bg="white",fg="black")
        f_name_1["font"] = ("Consolas",12,"bold")
        f_name_1.place(x=20,y=250)

    elif total == 2:
        new_window = Toplevel(root,bg="white")
        new_window.geometry("600x330")

        ticket_label = Label(new_window,text="Ticket",bg="white",fg="black")
        ticket_label["font"] = ("Consolas",18,"bold")
        ticket_label.place(x=10,y=5)

        dash_label1 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label1["font"] = ("Consolas",8,"bold")
        dash_label1.place(x=10,y=30)

        dash_label2 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label2["font"] = ("Consolas",8,"bold")
        dash_label2.place(x=10,y=70)

        final_from = Label(new_window,textvariable=var_final_from_to,bg="white",fg="black")
        final_from["font"] = ("Consolas",13,"bold")
        final_from.place(x=10,y=50)

        flight_number = Label(new_window,text="6E-5914",bg="white",fg="grey")
        flight_number["font"] = ("Consolas",8)
        flight_number.place(x=10,y=120)

        ticket_d1 = Label(new_window,textvariable=ticket_date,bg="white",fg="grey")
        ticket_d1["font"] = ("Consolas",8)
        ticket_d1.place(x=180,y=120)

        final_duration = Label(new_window,textvariable=var_final_duratoin,bg="white",fg="grey")
        final_duration["font"] = ("Consolas",8)
        final_duration.place(x=323,y=120)

        economy_label = Label(new_window,text="Economy",bg="white",fg="grey")
        economy_label["font"] = ("Consolas",8)
        economy_label.place(x=320,y=140)

        ticket_d2 = Label(new_window,textvariable=ticket_date,bg="white",fg="grey")
        ticket_d2["font"] = ("Consolas",8)
        ticket_d2.place(x=430,y=120)

        final_arrival = Label(new_window,textvariable=var_final_arrival,bg="white",fg="black")
        final_arrival["font"] = ("Consolas",13,"bold")
        final_arrival.place(x=400,y=100)

        final_departure = Label(new_window,textvariable=var_final_departure,bg="white",fg="black")
        final_departure["font"] = ("Consolas",13,"bold") 
        final_departure.place(x=150,y=100)

        final_airline = Label(new_window,textvariable=var_final_airline,bg="white",fg="black")
        final_airline["font"] = ("Consolas",13,"bold")
        final_airline.place(x=10,y=100)

        baggage_label = Label(new_window,text="Baggage: Check-in: 15 kg, Cabin: 7kg",bg="white",fg="grey")
        baggage_label["font"] = ("Consolas",8)
        baggage_label.place(x=10,y=170)

        travellers_label = Label(new_window,text="TRAVELLERS",bg="white",fg="black")
        travellers_label["font"] = ("Consolas",11,"bold")
        travellers_label.place(x=20,y=210)

        dash_label3 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label3["font"] = ("Consolas",8,"bold")
        dash_label3.place(x=10,y=190)

        dash_label4 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label4["font"] = ("Consolas",8,"bold")
        dash_label4.place(x=10,y=230)

        dash_label5 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label5["font"] = ("Consolas",8,"bold")
        dash_label5.place(x=10,y=270)

        first_name_1 = passenger1_firstname_textbox.get()
        second_name_1 = passenger1_lastname_textbox.get()
        var_name_1.set(f"{first_name_1} {second_name_1}")
        f_name_1 = Label(new_window,textvariable=var_name_1,bg="white",fg="black")
        f_name_1["font"] = ("Consolas",12,"bold")
        f_name_1.place(x=20,y=250)

        dash_label6 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label6["font"] = ("Consolas",8,"bold")
        dash_label6.place(x=10,y=310)

        first_name_2 = pass2_firstname.get()
        second_name_2 = pass2_lastname.get()
        var_name_2.set(f"{first_name_2} {second_name_2}")
        f_name_2 = Label(new_window,textvariable=var_name_2,bg="white",fg="black")
        f_name_2["font"] = ("Consolas",12,"bold")
        f_name_2.place(x=20,y=290)

    elif total == 3:
        new_window = Toplevel(root,bg="white")
        new_window.geometry("600x380")

        ticket_label = Label(new_window,text="Ticket",bg="white",fg="black")
        ticket_label["font"] = ("Consolas",18,"bold")
        ticket_label.place(x=10,y=5)

        dash_label1 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label1["font"] = ("Consolas",8,"bold")
        dash_label1.place(x=10,y=30)

        dash_label2 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label2["font"] = ("Consolas",8,"bold")
        dash_label2.place(x=10,y=70)

        dash_label3 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label3["font"] = ("Consolas",8,"bold")
        dash_label3.place(x=10,y=190)

        dash_label4 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label4["font"] = ("Consolas",8,"bold")
        dash_label4.place(x=10,y=230)

        dash_label5 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label5["font"] = ("Consolas",8,"bold")
        dash_label5.place(x=10,y=270)

        dash_label6 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label6["font"] = ("Consolas",8,"bold")
        dash_label6.place(x=10,y=310)

        dash_label7 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label7["font"] = ("Consolas",8,"bold")
        dash_label7.place(x=10,y=350)
        '''
        dash_label8 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label8["font"] = ("Consolas",8,"bold")
        dash_label8.place(x=10,y=390)
        '''
        final_from = Label(new_window,textvariable=var_final_from_to,bg="white",fg="black")
        final_from["font"] = ("Consolas",13,"bold")
        final_from.place(x=10,y=50)

        flight_number = Label(new_window,text="6E-5914",bg="white",fg="grey")
        flight_number["font"] = ("Consolas",8)
        flight_number.place(x=10,y=120)

        ticket_d1 = Label(new_window,textvariable=ticket_date,bg="white",fg="grey")
        ticket_d1["font"] = ("Consolas",8)
        ticket_d1.place(x=180,y=120)

        final_duration = Label(new_window,textvariable=var_final_duratoin,bg="white",fg="grey")
        final_duration["font"] = ("Consolas",8)
        final_duration.place(x=323,y=120)

        economy_label = Label(new_window,text="Economy",bg="white",fg="grey")
        economy_label["font"] = ("Consolas",8)
        economy_label.place(x=320,y=140)

        ticket_d2 = Label(new_window,textvariable=ticket_date,bg="white",fg="grey")
        ticket_d2["font"] = ("Consolas",8)
        ticket_d2.place(x=430,y=120)

        final_arrival = Label(new_window,textvariable=var_final_arrival,bg="white",fg="black")
        final_arrival["font"] = ("Consolas",13,"bold")
        final_arrival.place(x=400,y=100)

        final_departure = Label(new_window,textvariable=var_final_departure,bg="white",fg="black")
        final_departure["font"] = ("Consolas",13,"bold") 
        final_departure.place(x=150,y=100)

        final_airline = Label(new_window,textvariable=var_final_airline,bg="white",fg="black")
        final_airline["font"] = ("Consolas",13,"bold")
        final_airline.place(x=10,y=100)

        baggage_label = Label(new_window,text="Baggage: Check-in: 15 kg, Cabin: 7kg",bg="white",fg="grey")
        baggage_label["font"] = ("Consolas",8)
        baggage_label.place(x=10,y=170)

        travellers_label = Label(new_window,text="TRAVELLERS",bg="white",fg="black")
        travellers_label["font"] = ("Consolas",11,"bold")
        travellers_label.place(x=20,y=210)

        first_name_1 = passenger1_firstname_textbox.get()
        second_name_1 = passenger1_lastname_textbox.get()
        var_name_1.set(f"{first_name_1} {second_name_1}")
        f_name_1 = Label(new_window,textvariable=var_name_1,bg="white",fg="black")
        f_name_1["font"] = ("Consolas",12,"bold")
        f_name_1.place(x=20,y=250)

        first_name_2 = pass2_firstname.get()
        second_name_2 = pass2_lastname.get()
        var_name_2.set(f"{first_name_2} {second_name_2}")
        f_name_2 = Label(new_window,textvariable=var_name_2,bg="white",fg="black")
        f_name_2["font"] = ("Consolas",12,"bold")
        f_name_2.place(x=20,y=290)

        final_first_name_3 = pass3_firstname.get()
        final_second_name_3 = pass3_lastname.get()
        var_name_3.set(f"{final_first_name_3} {final_second_name_3}")
        f_name_3 = Label(new_window,textvariable=var_name_3,bg="white",fg="black")
        f_name_3["font"] = ("Consolas",12,"bold")
        f_name_3.place(x=20,y=330)
    elif total == 4:
        new_window = Toplevel(root,bg="white")
        new_window.geometry("600x420")

        ticket_label = Label(new_window,text="Ticket",bg="white",fg="black")
        ticket_label["font"] = ("Consolas",18,"bold")
        ticket_label.place(x=10,y=5)

        dash_label1 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label1["font"] = ("Consolas",8,"bold")
        dash_label1.place(x=10,y=30)

        dash_label2 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label2["font"] = ("Consolas",8,"bold")
        dash_label2.place(x=10,y=70)

        dash_label3 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label3["font"] = ("Consolas",8,"bold")
        dash_label3.place(x=10,y=190)

        dash_label4 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label4["font"] = ("Consolas",8,"bold")
        dash_label4.place(x=10,y=230)

        dash_label5 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label5["font"] = ("Consolas",8,"bold")
        dash_label5.place(x=10,y=270)

        dash_label6 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label6["font"] = ("Consolas",8,"bold")
        dash_label6.place(x=10,y=310)

        dash_label7 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="grey")
        dash_label7["font"] = ("Consolas",8,"bold")
        dash_label7.place(x=10,y=350)
        
        dash_label8 = Label(new_window,text="______________________________________________________________________________________________",bg="white",fg="black")
        dash_label8["font"] = ("Consolas",8,"bold")
        dash_label8.place(x=10,y=390)
        
        final_from = Label(new_window,textvariable=var_final_from_to,bg="white",fg="black")
        final_from["font"] = ("Consolas",13,"bold")
        final_from.place(x=10,y=50)

        flight_number = Label(new_window,text="6E-5914",bg="white",fg="grey")
        flight_number["font"] = ("Consolas",8)
        flight_number.place(x=10,y=120)

        ticket_d1 = Label(new_window,textvariable=ticket_date,bg="white",fg="grey")
        ticket_d1["font"] = ("Consolas",8)
        ticket_d1.place(x=180,y=120)

        final_duration = Label(new_window,textvariable=var_final_duratoin,bg="white",fg="grey")
        final_duration["font"] = ("Consolas",8)
        final_duration.place(x=323,y=120)

        economy_label = Label(new_window,text="Economy",bg="white",fg="grey")
        economy_label["font"] = ("Consolas",8)
        economy_label.place(x=320,y=140)

        ticket_d2 = Label(new_window,textvariable=ticket_date,bg="white",fg="grey")
        ticket_d2["font"] = ("Consolas",8)
        ticket_d2.place(x=430,y=120)

        final_arrival = Label(new_window,textvariable=var_final_arrival,bg="white",fg="black")
        final_arrival["font"] = ("Consolas",13,"bold")
        final_arrival.place(x=400,y=100)

        final_departure = Label(new_window,textvariable=var_final_departure,bg="white",fg="black")
        final_departure["font"] = ("Consolas",13,"bold") 
        final_departure.place(x=150,y=100)

        final_airline = Label(new_window,textvariable=var_final_airline,bg="white",fg="black")
        final_airline["font"] = ("Consolas",13,"bold")
        final_airline.place(x=10,y=100)

        baggage_label = Label(new_window,text="Baggage: Check-in: 15 kg, Cabin: 7kg",bg="white",fg="grey")
        baggage_label["font"] = ("Consolas",8)
        baggage_label.place(x=10,y=170)

        travellers_label = Label(new_window,text="TRAVELLERS",bg="white",fg="black")
        travellers_label["font"] = ("Consolas",11,"bold")
        travellers_label.place(x=20,y=210)

        first_name_1 = pass1_firstname.get()
        second_name_1 = pass1_lastname.get()
        var_name_1.set(f"{first_name_1} {second_name_1}")
        f_name_1 = Label(new_window,textvariable=var_name_1,bg="white",fg="black")
        f_name_1["font"] = ("Consolas",12,"bold")
        f_name_1.place(x=20,y=250)

        first_name_2 = pass2_firstname.get()
        second_name_2 = pass2_lastname.get()
        var_name_2.set(f"{first_name_2} {second_name_2}")
        f_name_2 = Label(new_window,textvariable=var_name_2,bg="white",fg="black")
        f_name_2["font"] = ("Consolas",12,"bold")
        f_name_2.place(x=20,y=290)

        final_first_name_3 = pass3_firstname.get()
        final_second_name_3 = pass3_lastname.get()
        var_name_3.set(f"{final_first_name_3} {final_second_name_3}")
        f_name_3 = Label(new_window,textvariable=var_name_3,bg="white",fg="black")
        f_name_3["font"] = ("Consolas",12,"bold")
        f_name_3.place(x=20,y=330)

        final_first_name_4 = pass4_firstname.get()
        final_second_name_4 = pass4_lastname.get()
        var_name_4.set(f"{final_first_name_4} {final_second_name_4}")
        f_name_4 = Label(new_window,textvariable=var_name_4,bg="white",fg="black")
        f_name_4["font"] = ("Consolas",12,"bold")
        f_name_4.place(x=20,y=370)

def select_seat(seat):
    global seat_total_count 
    total_seat = count0.get() + count1.get() + count2.get()
    if seat == "1A" and total > 0:    
        s1["state"]=DISABLED
        s1["background"]=("green2")
        s1["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "1B" and total > 0:
        s2["state"]=DISABLED
        s2["background"]=("green2")
        s2["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "2A" and total > 0:
        s3["state"]=DISABLED
        s3["background"]=("green2")
        s3["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "2B" and total > 0:
        s4["state"]=DISABLED
        s4["background"]=("green2")
        s4["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "3A" and total > 0:
        s5["state"]=DISABLED
        s5["background"]=("green2")
        s5["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "3B" and total > 0:
        s6["state"]=DISABLED
        s6["background"]=("green2")
        s6["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "4A":
        s7["state"]=DISABLED
        s7["background"]=("green2")
        s7["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "4B" and total > 0:
        s8["state"]=DISABLED
        s8["background"]=("green2")
        s8["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "5A" and total > 0:
        s9["state"]=DISABLED
        s9["background"]=("green2")
        s9["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "5B" and total > 0:
        s10["state"]=DISABLED
        s10["background"]=("green2")
        s10["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "1C" and total > 0:    
        s11["state"]=DISABLED
        s11["background"]=("green2")
        s11["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "1D" and total > 0:
        s12["state"]=DISABLED
        s12["background"]=("green2")
        s12["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "2C" and total > 0:
        s13["state"]=DISABLED
        s13["background"]=("green2")
        s13["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "2D" and total > 0:
        s14["state"]=DISABLED
        s14["background"]=("green2")
        s14["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "3C" and total > 0:
        s15["state"]=DISABLED
        s15["background"]=("green2")
        s15["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "3D" and total > 0:
        s16["state"]=DISABLED
        s16["background"]=("green2")
        s16["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "4C" and total > 0:
        s17["state"]=DISABLED
        s17["background"]=("green2")
        s17["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "4D" and total > 0:
        s18["state"]=DISABLED
        s18["background"]=("green2")
        s18["disabledforeground"]=("white") 
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "5C" and total > 0:
        s19["state"]=DISABLED
        s19["background"]=("green2")
        s19["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

    elif seat == "5D" and total > 0:
        s20["state"]=DISABLED
        s20["background"]=("green2")
        s20["disabledforeground"]=("white")
        total_seat = total_seat-1
        seat_total_count = seat_total_count + 1

def ticket():
    global date
    date = var_date.get()
    ticket_date.set(f"{date}")

def flight1():
    global ticket_duration
    ticket_duration = "1h 10m"
    var_final_duratoin.set(f"{ticket_duration}")
    global ticket_departure
    ticket_departure = "05:05"
    var_final_departure.set(f"{departure}  {ticket_departure}")
    global ticket_arrival
    ticket_arrival = "06:15" 
    var_final_arrival.set(f"{arrival}  {ticket_arrival}")
    global ticket_airline
    ticket_airline = "Indigo"
    var_final_airline.set(f"{ticket_airline}")
    var_final_from_to.set(f"{departure} to {arrival}")
    global final_price
    final_price = 3943*total_no_pass
    show_frame(frame3)

def flight2():
    global ticket_duration
    ticket_duration = "1h 05m"
    var_final_duratoin.set(f"{ticket_duration}")
    global ticket_departure
    ticket_departure = "16:00"
    var_final_departure.set(f"{departure} {ticket_departure}")
    global ticket_arrival
    ticket_arrival = "17:05" 
    var_final_arrival.set(f"{arrival} {ticket_arrival}")
    global ticket_airline
    ticket_airline = "Vistara"
    var_final_airline.set(f"{ticket_airline}")
    var_final_from_to.set(f"{departure} to {arrival}")
    global final_price
    final_price = 4199*total_no_pass
    show_frame(frame3)

def flight3():
    global ticket_duration
    ticket_duration = "1h 25m"
    var_final_duratoin.set(f"{ticket_duration}")
    global ticket_departure
    ticket_departure = "08:00"
    var_final_departure.set(f"{departure} {ticket_departure}")
    global ticket_arrival
    ticket_arrival = "09:25" 
    var_final_arrival.set(f"{arrival} {ticket_arrival}")
    global ticket_airline
    ticket_airline = "Spicejet"
    var_final_airline.set(f"{ticket_airline}")
    var_final_from_to.set(f"{departure} to {arrival}")
    global final_price
    final_price = 3530*total_no_pass
    show_frame(frame3)

def flight4():
    global ticket_duration
    ticket_duration = "1h 15m"
    var_final_duratoin.set(f"{ticket_duration}")
    global ticket_departure
    ticket_departure = "17:00"
    var_final_departure.set(f"{departure} {ticket_departure}")
    global ticket_arrival
    ticket_arrival = "18:15" 
    var_final_arrival.set(f"{arrival} {ticket_arrival}")
    global ticket_airline
    ticket_airline = "Air Asia"
    var_final_airline.set(f"{ticket_airline}")
    var_final_from_to.set(f"{departure} to {arrival}")
    global final_price
    final_price = 4203*total_no_pass
    show_frame(frame3)

def show_ticket_options():
    global total 
    total = count0.get() + count1.get() + count2.get()
    var_total.set(f"{total} passengers\n\n\n\n\n{total} passengers\n\n\n\n\n{total} passengers\n\n\n\n\n{total} passengers")
    if (var_date.get() == ""):
        messagebox.showerror("","Select Date")
    if (total > 4):
        messagebox.showerror("","Max 4 passengers allowed")      
    if (city.get() == "Select your City" or destination.get() == "Select Your Destination"):
        messagebox.showerror("","Select a City for Departure")   
    if (city.get() == destination.get()):
        messagebox.showerror("","From and To can't be the same")   
    if (city.get() != destination.get() and city.get() != "Select your City" and destination.get() != "Select Your Destination" and total < 5 and var_date.get() != "" ) :
        show_frame(frame2)
        global arrival
        arrival = destination.get()
        var_arrival.set(f"{arrival}\n\n\n\n\n{arrival}\n\n\n\n\n{arrival}\n\n\n\n\n{arrival}")
        global departure
        departure = city.get()
        var_departure.set(f"{departure}\n\n\n\n\n{departure}\n\n\n\n\n{departure}\n\n\n\n\n{departure}")
    book_flight1()
    book_flight2()
    book_flight3()
    book_flight4()

def book_flight1():
    global total
    global ticket_price
    ticket_price = 3943*total
    var_price_1.set(f"₹{ticket_price}")

def book_flight2():
    global total 
    global ticket_price
    ticket_price = 4199*total
    var_price_2.set(f"₹{ticket_price}")

def book_flight3():
    global total 
    global ticket_price
    ticket_price = 3530*total
    var_price_3.set(f"₹{ticket_price}")

def book_flight4():
    global total 
    global ticket_price
    ticket_price = 4203*total
    var_price_4.set(f"₹{ticket_price}")

def show_frame(frame):
    frame.tkraise()

def clear_seat():
    global seat_total_count
    seat_total_count = 0
    s1["state"] = NORMAL
    s1["bg"] = "white"
    s2["state"] = NORMAL
    s2["bg"] = "white"
    s3["state"] = NORMAL
    s3["bg"] = "white"
    s4["state"] = NORMAL
    s4["bg"] = "white"
    s5["state"] = NORMAL
    s5["bg"] = "white"
    s6["state"] = NORMAL
    s6["bg"] = "white"
    s7["state"] = NORMAL
    s7["bg"] = "white"
    s8["state"] = NORMAL
    s8["bg"] = "white"
    s9["state"] = NORMAL
    s9["bg"] = "white"
    s10["state"] = NORMAL
    s10["bg"] = "white"
    s11["state"] = NORMAL
    s11["bg"] = "white"
    s12["state"] = NORMAL
    s12["bg"] = "white"
    s13["state"] = NORMAL
    s13["bg"] = "white"
    s14["state"] = NORMAL
    s14["bg"] = "white"
    s15["state"] = NORMAL
    s15["bg"] = "white"
    s16["state"] = NORMAL
    s16["bg"] = "white"
    s17["state"] = NORMAL
    s17["bg"] = "white"
    s18["state"] = NORMAL
    s18["bg"] = "white"
    s19["state"] = NORMAL
    s19["bg"] = "white"
    s20["state"] = NORMAL
    s20["bg"] = "white"

def food_bill():
    global total_no_pass
    global ticket_price
    global final_price
    food_items=[]                            
    food_items.append(("Base Fare",int((count0.get()+count1.get()+count2.get())),int(final_price)))
    food_items.append(("Chicken Sandwhich",int(chicken_sandwhich_num.get()),250))
    food_items.append(("Veg Sandwhich",int(veg_sandwhich_num.get()),150))
    food_items.append(("Veg Biryani",int(veg_biryani_num.get()),350))
    food_items.append(("Chicken Biryani",int(chicken_biryani_num.get()),390))
    food_items.append(("Cup Noodles",int(cup_noodles_num.get()),250))
    food_items.append(("Cookies",int(cookie_num.get()),70))
    food_items.append(("Fries",int(fries_num.get()),200))
    food_items.append(("Coca Cola",int(coca_cola_num.get()),95))
    food_items.append(("Pepsi",int(pepsi_num.get()),95))
    food_items.append(("Sprite",int(sprite_num.get()),95))
    food_items.append(("Tea",int(tea_num.get()),100))
    food_items.append(("Coffee",int(coffee_num.get()),120))
    food_items.append(("Mango Smoothie",int(mango_num.get()),150))
    food_items.append(("Mineral Water",int(water_num.get()),50))
    

    #Adding the items the user has selected in this list 
    chosen_item_amt=[]
    for (name,qty,price) in food_items:
        if qty>0:
            chosen_item_name.append(name)
            chosen_item_qty.append(qty)
            chosen_item_price.append(price)
            chosen_item_amt.append(qty*price)

    #Storing all the item names in a string
    name_str=""
    for x in chosen_item_name:
        name_str+=f"{x}\n"
    var_item_name.set(name_str)

    qty_str=""
    for x in chosen_item_qty:
        qty_str+=f"{x}\n"
    var_item_quantity.set(qty_str)

    #Storing all the item amounts in a string
    amt_str=""
    for x in chosen_item_amt:
        amt_str+=f"{x}\n"
    var_item_amt.set(amt_str)
    #Finding and storing the total amount without GST
    amt_wo_gst=0
    for x in chosen_item_amt:
        amt_wo_gst+=x
    var_total_amt_wo_gst.set(f"Sub Total :\t{amt_wo_gst}")

    #Calculating GST
    gst=((6/100)*amt_wo_gst)
    var_gst_amt.set(f"GST :\t\t{gst:.2f}\t(6%)")

    #Finding Total Amount
    amt_w_gst=amt_wo_gst+gst
    var_total_amt_w_gst.set(f"Final Amount :\t{amt_w_gst:.2f}")
    show_frame(frame6)

def seat_yes():
    global seat_total_count
    global total
    if seat_total_count > total:
        messagebox.showerror("","Extra Seat Selected")
    elif seat_total_count < total:
        messagebox.showerror("","Less Seats Selected")
    elif seat_total_count == total:
        show_frame(snack)

def seat_no():
    global seat_total_count
    global total
    if seat_total_count > total:
        messagebox.showerror("","Extra Seat Selected")
    elif seat_total_count < total:
        messagebox.showerror("","Less Seats Selected")
    elif seat_total_count == total:
        food_bill()

root = Tk()
root.state('zoomed')                
root.rowconfigure(0, weight=1)          
root.columnconfigure(0, weight=1)

frame1 = Frame(root,bg="#202A44")#no. of people, destination, departure, date     
frame2 = Frame(root,bg="#202A44")#ticket options  
frame3 = Frame(root,bg="#202A44")#traveller details
frame4 = Frame(root,bg="#202A44")#traveller details
frame5 = Frame(root,bg="#202A44")
frame6 = Frame(root,bg="#202A44")
snack = Frame(root,bg="#202A44")
passenger_3_frame = Frame(root,bg="#202A44")
passenger_4_frame = Frame(root,bg="#202A44")
price_sort_ascending = Frame(root,bg="#202A44")
price_sort_descending = Frame(root,bg="#202A44")
duration_sort = Frame(root,bg="#202A44")
duration_sort_descending = Frame(root,bg="#202A44")
departure_sort = Frame(root,bg="#202A44")
departure_sort_descending = Frame(root,bg="#202A44")

for frame in (frame1,frame2,frame3,frame4,frame5,frame6,passenger_3_frame,passenger_4_frame,price_sort_ascending,duration_sort,price_sort_descending,duration_sort_descending,departure_sort,departure_sort_descending,snack):              
    frame.grid(row=0, column=0, sticky='nsew')      

root.geometry("700x500")
root.title("Flight Ticket Booking")
root.maxsize(700,500)

var_final_departure = StringVar()
var_final_arrival = StringVar()
var_final_duratoin = StringVar()
ticket_date = StringVar()
var_final_airline = StringVar()
var_final_from_to = StringVar()
var_item_name = StringVar()
var_item_quantity = StringVar()
var_item_amt = StringVar()
var_total_amt_gst = StringVar()
var_total_amt_wo_gst = StringVar()
var_gst_amt = StringVar()
var_total_amt_w_gst = StringVar()
var_name_1 = StringVar()
var_name_2 = StringVar()
var_name_3 = StringVar()
var_name_4 = StringVar()
gender_1 = StringVar()
gender_2 = StringVar()
gender_3 = StringVar()
gender_4= StringVar()
pass1_firstname = StringVar()
pass1_lastname = StringVar()
pass2_firstname = StringVar()
pass2_lastname = StringVar()
pass3_firstname = StringVar()
pass3_lastname = StringVar()
pass4_firstname = StringVar()
pass4_lastname = StringVar()
chicken_sandwhich_num = IntVar(value=0)
veg_sandwhich_num =IntVar(value=0)
veg_biryani_num = IntVar(value=0)
chicken_biryani_num = IntVar(value=0)
cup_noodles_num = IntVar(value=0)
cookie_num =IntVar(value=0)
fries_num = IntVar(value=0)
coca_cola_num = IntVar(value=0)
pepsi_num = IntVar(value=0)
sprite_num = IntVar(value=0)
tea_num = IntVar(value=0)
coffee_num = IntVar(value=0)
mango_num = IntVar(value=0)
water_num = IntVar(value=0)



#Code heading
title_label = Label(frame1,text="Book Flight Tickets",fg="darkorange",bg="#202A44")        
title_label["font"] = ("Consolas",25,"bold")
title_label.place(x=80,y=20)

var = IntVar()
#From label
from_label = Label(frame1,text="From",fg="darkorange",bg="#202A44")                        
from_label["font"] = ("Consolas",13)
from_label.place(x=80,y=100)

arrow_label = Label(frame1,text="⇌",fg="darkorange",bg="#202A44")
arrow_label.place(x=218,y=125)

to_label = Label(frame1,text="To",font="Consolas",fg="darkorange",bg="#202A44")                            
to_label["font"] = ("Consolas",13)
to_label.place(x=250,y=100)

list_of_cities = ["Ahmedabad","Banglore","Chennai","Delhi","Kolkata","Mumbai"]

#Destination Drop down
destination = StringVar()
destination.set("Select Your Destination")
to_dropdown = OptionMenu(frame1,destination,*list_of_cities)
to_dropdown["fg"]=("darkorange")
to_dropdown["activeforeground"]=("darkorange")
to_dropdown["bg"]=("#202A44")
to_dropdown["activebackground"]=("#202A44")
to_dropdown["bd"] = (0)
to_dropdown.place(x=250,y=125)

#City drop down
city = StringVar()
city.set("Select your City")
from_dropdown = OptionMenu(frame1,city,*list_of_cities) 
from_dropdown["fg"]=("darkorange")
from_dropdown["activeforeground"]=("darkorange")
from_dropdown["bg"]=("#202A44")
from_dropdown["activebackground"]=("#202A44")
from_dropdown["bd"]=(0)
from_dropdown.place(x=80,y=125)

#Calendar to select date
depart_label = Label(frame1,text="Depart On",fg="darkorange",bg="#202A44")                 
depart_label["font"] = ("Consolas",13)
depart_label.place(x=80,y=180)

#min_date=date(2021,10,14)
var_date = StringVar()
cal= Calendar(frame1,selectmode="day",year=2021,month=10,day=20,background="floral white",foreground="#202A44",normalbackground="floral white",normalforeground="purple",showweeknumbers=False,date_pattern="dd/mm/yy")
cal["font"] = ("Consolas",10)
cal["textvariable"] = var_date
cal["othermonthbackground"]="floral white"
cal["othermonthforeground"]="darkorange"
cal["weekendbackground"]="floral white"
cal["weekendforeground"]="red"
cal["othermonthwebackground"]="floral white"
cal["othermonthbackground"] = "floral white"
cal["othermonthforeground"]="gold3"
cal["othermonthweforeground"]="gold3"
cal["headersbackground"]="floral white"
cal["headersforeground"]="#202A44"
cal["bordercolor"] = "floral white"
cal.place(x=200,y=180)

adults_label = Label(frame1,text="Adults",fg="darkorange",bg="#202A44")                    
adults_label["font"] = ("Consolas",13)
adults_label.place(x=80,y=370)

adults_age_label = Label(frame1,text="> 12yrs",fg="darkorange",bg="#202A44")
adults_age_label["font"] = ("Consolas",8)
adults_age_label.place(x=85,y=430)

children_label = Label(frame1,text="Children",fg="darkorange",bg="#202A44")                
children_label["font"] = ("Consolas",13)
children_label.place(x=180,y=370)

children_age_label = Label(frame1,text="2-11 yrs",fg="darkorange",bg="#202A44")
children_age_label["font"] = ("Consolas",8)
children_age_label.place(x=185,y=430)

infant_label = Label(frame1,bg="#202A44")                                             
infant_label["text"] = ("Infants")
infant_label["fg"] = ("darkorange")
infant_label["font"] = ("Consolas",13)
infant_label.place(x=280,y=370)

infant_age_label = Label(frame1,text="< 2yrs",fg="darkorange",bg="#202A44")
infant_age_label["font"] = ("Consolas",8)
infant_age_label.place(x=285,y=430)

count0 = IntVar(value=1)

count1 = IntVar(value=0)

count2 = IntVar(value=0)

adult_age_list = ["1","2","3","4"]

age_list = ["0","1","2","3"]

num_adults = count0.get()
num_child = count1.get()
num_infant = count2.get()

total_no_pass = int(f"{int(num_adults)+int(num_child)+int(num_infant)}")
#no. of adults drop down
adults_dropdown = OptionMenu(frame1,count0,*adult_age_list)  
adults_dropdown["fg"]=("darkorange")
adults_dropdown["activeforeground"]=("darkorange")
adults_dropdown["bg"]=("#202A44")
adults_dropdown["activebackground"]=("#202A44")  
adults_dropdown["bd"] = 0
adults_dropdown.place(x=80,y=400)

#no of children drop down
children_dropdown = OptionMenu(frame1,count1,*age_list) 
children_dropdown["fg"]=("darkorange")
children_dropdown["activeforeground"]=("darkorange")
children_dropdown["bg"]=("#202A44")
children_dropdown["activebackground"]=("#202A44")
children_dropdown["bd"] = 0
children_dropdown.place(x=180,y=400)

#no of infants drop down
infants_dropdown = OptionMenu(frame1,count2,*age_list)  
infants_dropdown["fg"]=("darkorange")
infants_dropdown["activeforeground"]=("darkorange")
infants_dropdown["bg"]=("#202A44")
infants_dropdown["activebackground"]=("#202A44")
infants_dropdown["bd"] = 0
infants_dropdown.place(x=280,y=400)

#Search button to go to next window
search_button = Button(frame1)      
search_button["text"] = ("Search Flights")
search_button["font"] = ("Consolas",13,"bold")
search_button["bg"] = ("darkorange")
search_button["fg"] = ("#202A44")
search_button["activebackground"] = ("darkorange")
search_button["activeforeground"] = ("#202A44")
search_button["bd"] = 0
search_button["command"] = show_ticket_options
search_button.place(x=550,y=450)





                                                                    #FRAME2:
root.geometry("700x500")

bracket = Frame(frame2,bg="darkorange",width=650,height=50)
bracket.place(x=30,y=40)


back_button = Button(frame2)
back_button["text"] = ("Back")
back_button["font"] = ("Consolas",13,"bold")
back_button["fg"] = ("#202A44")
back_button["bg"] = ("darkorange")
back_button["bd"] = 0
back_button["activebackground"] = ("darkorange")
back_button["activeforeground"] = ("#202A44")
back_button["command"] = lambda:show_frame(frame1)
back_button.place(x=50,y=450)

airline_label = Button(frame2)
airline_label["text"] = ("Airline")
airline_label["font"] = ("Consolas",13,"bold")
airline_label["fg"] = ("#202A44")
airline_label["bg"] = ("darkorange")
airline_label["bd"] = (0)
airline_label["activebackground"] = ("darkorange")
airline_label["activeforeground"] = ("#202A44")
airline_label.place(x=50,y=55)


departure_label = Button(frame2)
departure_label["text"] = ("Departure ↑↓")
departure_label["font"] = ("Consolas",13,"bold")
departure_label["fg"] = ("#202A44")
departure_label["bg"] = ("darkorange")
departure_label["bd"] = (0)
departure_label["activebackground"] = ("darkorange")
departure_label["activeforeground"] = ("#202A44")
departure_label["command"] = lambda:show_frame(departure_sort)
departure_label.place(x=150,y=55)

arrival_label = Button(frame2)
arrival_label["text"] = ("Arrival")
arrival_label["font"] = ("Consolas",13,"bold")
arrival_label["fg"] = ("#202A44")
arrival_label["bg"] = ("darkorange")
arrival_label["bd"] = (0)
arrival_label["activebackground"] = ("darkorange")
arrival_label["activeforeground"] = ("#202A44")
arrival_label.place(x=285,y=55)

duration_button = Button(frame2)
duration_button["text"] = ("Duration ↑↓")
duration_button["font"] = ("Consolas",13,"bold")
duration_button["fg"] = ("#202A44")
duration_button["bg"] = ("darkorange")
duration_button["bd"] = (0)
duration_button["activebackground"] = ("darkorange")
duration_button["activeforeground"] = ("#202A44")
duration_button["command"] = lambda:show_frame(duration_sort)
duration_button.place(x=400,y=55)

price_button = Button(frame2)
price_button["text"] = ("Price ↑↓")
price_button["font"] = ("Consolas",13,"bold")
price_button["fg"] = ("#202A44")
price_button["bg"] = ("darkorange")
price_button["bd"] = (0)
price_button["activebackground"] = ("darkorange")
price_button["activeforeground"] = ("#202A44")
price_button["command"] = lambda:show_frame(price_sort_ascending)
price_button.place(x=520,y=55)

var_arrival = StringVar()
arrival_label = Label(frame2)
arrival_label["bg"] = ("#202A44")
arrival_label["fg"] = ("darkorange")
arrival_label["textvariable"] = (var_arrival)
arrival_label.place(x=285,y=130)

var_departure = StringVar()
departure_label = Label(frame2)
departure_label["bg"] = ("#202A44")
departure_label["fg"] = ("darkorange")
departure_label["textvariable"] = (var_departure)
departure_label.place(x=150,y=130)

airline_logo = Label(frame2,font=30,bg="#202A44",fg="darkorange")
airline_logo["text"] = ("Indigo")
indigo_img= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/indigo-logo.jpg")
indigo_resize_image = indigo_img.resize((70,50))
#Convert To photoimage
indigo_tkimage= ImageTk.PhotoImage(indigo_resize_image)
#Display the Image
label=Label(frame2,image=indigo_tkimage)
label.place(x=40,y=100)



departure_time_label = Label(frame2,fg="darkorange",bg="#202A44")
departure_time_label["text"] = ("05:05")
departure_time_label["font"] = (18)
departure_time_label.place(x=155,y=100)

arrival_time_label = Label(frame2,fg="darkorange",bg="#202A44",)
arrival_time_label["text"] = ("06:15")
arrival_time_label["font"] = (18)
arrival_time_label.place(x=290,y=100)

duration_label = Label(frame2,fg="darkorange",bg="#202A44")
duration_label["text"] = ("1h 10m")
duration_label["font"] = (18)
duration_label.place(x=405,y=100)

var_price_1 = IntVar() 
price_show_label = Label(frame2,textvariable=var_price_1,fg="darkorange",font =30,bg="#202A44")
price_show_label.place(x=520,y=100) 

var_total = IntVar()
totalenger = Label(frame2)
totalenger["fg"] = "darkorange"
totalenger["bg"] = "#202A44"
totalenger["textvariable"] = var_total
totalenger.place(x=520,y=130)

book_button= Button(frame2,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=flight1,bd=0)
book_button["font"] = ("Consolas",13,"bold")
book_button.place(x=605,y=100)

airlines_name_label_2 = Label(frame2,text="Vistara",fg="darkorange",font =30,bg="#202A44")
vistara_img= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/vistara-logo.jpg")
vistara_resize_image = vistara_img.resize((70,50))
#Convert To photoimage
vistara_tkimage= ImageTk.PhotoImage(vistara_resize_image)
#Display the Image
label=Label(frame2,image=vistara_tkimage)
label.place(x=40,y=175)

departure_time_label_2 = Label(frame2,text="16:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_2.place(x=155,y=175)

arrival_time_label_2 = Label(frame2,text="17:05",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_2.place(x=290,y=175)

duration_time_label_2 = Label(frame2,text="1h 05m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_2.place(x=405,y=175)

var_price_2 = IntVar()
price_show_label_2 = Label(frame2,textvariable=var_price_2,fg="darkorange",font =30,bg="#202A44")
price_show_label_2.place(x=520,y=175)

book_button_2= Button(frame2,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=flight2,bd=0)
book_button_2["font"] = ("Consolas",13,"bold")
book_button_2.place(x=605,y=175)

airlines_name_label_3 = Label(frame2,text="Spicejet",fg="darkorange",font =30,bg="#202A44")
spicejet_img= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/spicejet-logo.jpg")
spicejet_resize_image = spicejet_img.resize((70,50))
#Convert To photoimage
spicejet_tkimage= ImageTk.PhotoImage(spicejet_resize_image)
#Display the Image
label=Label(frame2,image=spicejet_tkimage)
label.place(x=40,y=250)

departure_time_label_3 = Label(frame2,text="08:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_3.place(x=155,y=250)

arrival_time_label_3 = Label(frame2,text="09:25",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_3.place(x=290,y=250)

duration_time_label_3 = Label(frame2,text="1h 25m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_3.place(x=405,y=250)

var_price_3 = IntVar()
price_show_label_3 = Label(frame2,textvariable=var_price_3,fg="darkorange",font =30,bg="#202A44")
price_show_label_3.place(x=520,y=250)

book_button_3= Button(frame2,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=flight3,bd=0)
book_button_3["font"] = ("Consolas",13,"bold")
book_button_3.place(x=605,y=250)

airlines_name_label_4 = Label(frame2,text="Air Asia",fg="darkorange",font =30,bg="#202A44")
airasia_img= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/airasia-logo.jpg")
airasia_resize_image = airasia_img.resize((70,50))
#Convert To photoimage
airasia_tkimage= ImageTk.PhotoImage(airasia_resize_image)
#Display the Image
label=Label(frame2,image=airasia_tkimage)
label.place(x=40,y=325)

departure_time_label_4 = Label(frame2,text="17:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_4.place(x=155,y=325)

arrival_time_label_4 = Label(frame2,text="18:15",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_4.place(x=290,y=325)

duration_time_label_4 = Label(frame2,text="1h 15m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_4.place(x=405,y=325)

var_price_4 = IntVar()
price_show_label_4 = Label(frame2,textvariable=var_price_4,fg="darkorange",font =30,bg="#202A44")
price_show_label_4.place(x=520,y=325)

book_button_4= Button(frame2,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=flight4,bd=0)
book_button_4["font"] = ("Consolas",13,"bold")
book_button_4.place(x=605,y=325)





                                                                #PRICE SORT ASCENDING:
bracket = Frame(price_sort_ascending,bg="darkorange",width=650,height=50)
bracket.place(x=30,y=40)


back_button = Button(price_sort_ascending)
back_button["text"] = ("Back")
back_button["font"] = ("Consolas",13,"bold")
back_button["fg"] = ("#202A44")
back_button["bg"] = ("darkorange")
back_button["bd"] = 0
back_button["activebackground"] = ("darkorange")
back_button["activeforeground"] = ("#202A44")
back_button["command"] = lambda:show_frame(frame1)
back_button.place(x=50,y=450)

airline_label = Button(price_sort_ascending)
airline_label["text"] = ("Airline")
airline_label["font"] = ("Consolas",13,"bold")
airline_label["fg"] = ("#202A44")
airline_label["bg"] = ("darkorange")
airline_label["bd"] = (0)
airline_label["activebackground"] = ("darkorange")
airline_label["activeforeground"] = ("#202A44")
airline_label.place(x=50,y=55)

departure_label = Button(price_sort_ascending)
departure_label["text"] = ("Departure ↑↓")
departure_label["font"] = ("Consolas",13,"bold")
departure_label["fg"] = ("#202A44")
departure_label["bg"] = ("darkorange")
departure_label["bd"] = (0)
departure_label["activebackground"] = ("darkorange")
departure_label["activeforeground"] = ("#202A44")
departure_label["command"] = lambda:show_frame(departure_sort)
departure_label.place(x=150,y=55)

arrival_label = Button(price_sort_ascending)
arrival_label["text"] = ("Arrival")
arrival_label["font"] = ("Consolas",13,"bold")
arrival_label["fg"] = ("#202A44")
arrival_label["bg"] = ("darkorange")
arrival_label["bd"] = (0)
arrival_label["activebackground"] = ("darkorange")
arrival_label["activeforeground"] = ("#202A44")
arrival_label.place(x=285,y=55)

duration_button = Button(price_sort_ascending)
duration_button["text"] = ("Duration ↑↓")
duration_button["font"] = ("Consolas",13,"bold")
duration_button["fg"] = ("#202A44")
duration_button["bg"] = ("darkorange")
duration_button["bd"] = (0)
duration_button["activebackground"] = ("darkorange")
duration_button["activeforeground"] = ("#202A44")
duration_button["command"] = lambda:show_frame(duration_sort)
duration_button.place(x=400,y=55)

price_button = Button(price_sort_ascending)
price_button["text"] = ("Price ↑")
price_button["font"] = ("Consolas",13,"bold")
price_button["fg"] = ("#202A44")
price_button["bg"] = ("darkorange")
price_button["bd"] = (0)
price_button["activebackground"] = ("darkorange")
price_button["activeforeground"] = ("#202A44")
price_button["command"] = lambda:show_frame(price_sort_descending)
price_button.place(x=520,y=55)

totalenger = Label(price_sort_ascending)
totalenger["fg"] = "darkorange"
totalenger["bg"] = "#202A44"
totalenger["textvariable"] = var_total
totalenger.place(x=520,y=130)

arrival_label = Label(price_sort_ascending)
arrival_label["bg"] = ("#202A44")
arrival_label["fg"] = ("darkorange")
arrival_label["textvariable"] = (var_arrival)
arrival_label.place(x=285,y=130)

departure_label = Label(price_sort_ascending)
departure_label["bg"] = ("#202A44")
departure_label["fg"] = ("darkorange")
departure_label["textvariable"] = (var_departure)
departure_label.place(x=150,y=130)

airline_logo = Label(price_sort_ascending,font=30,bg="#202A44",fg="darkorange")
airline_logo["text"] = ("Indigo")
indigo_img_price_sort_ascending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/indigo-logo.jpg")
indigo_resize_image_price_sort_ascending = indigo_img.resize((70,50))
#Convert To photoimage
indigo_tkimage_price_sort_ascending= ImageTk.PhotoImage(indigo_resize_image_price_sort_ascending)
#Display the Image
label=Label(price_sort_ascending,image=indigo_tkimage_price_sort_ascending)
label.place(x=40,y=175)

departure_time_label = Label(price_sort_ascending,fg="darkorange",bg="#202A44")
departure_time_label["text"] = ("05:05")
departure_time_label["font"] = (18)
departure_time_label.place(x=155,y=175)

arrival_time_label = Label(price_sort_ascending,fg="darkorange",bg="#202A44",)
arrival_time_label["text"] = ("06:15")
arrival_time_label["font"] = (18)
arrival_time_label.place(x=290,y=175)

duration_label = Label(price_sort_ascending,fg="darkorange",bg="#202A44")
duration_label["text"] = ("1h 10m")
duration_label["font"] = (18)
duration_label.place(x=405,y=175)

price_show_label = Label(price_sort_ascending,textvariable=var_price_1,fg="darkorange",font =30,bg="#202A44")
price_show_label.place(x=520,y=175) 

book_button= Button(price_sort_ascending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button["font"] = ("Consolas",13,"bold")
book_button.place(x=605,y=175)

airlines_name_label_2 = Label(price_sort_ascending,text="Vistara",fg="darkorange",font =30,bg="#202A44")
vistara_img_ascending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/vistara-logo.jpg")
vistara_resize_image_ascending = vistara_img_ascending.resize((70,50))
#Convert To photoimage
vistara_tkimage_ascending= ImageTk.PhotoImage(vistara_resize_image_ascending)
#Display the Image
label=Label(price_sort_ascending,image=vistara_tkimage_ascending)
label.place(x=40,y=250)


departure_time_label_2 = Label(price_sort_ascending,text="16:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_2.place(x=155,y=250)

arrival_time_label_2 = Label(price_sort_ascending,text="17:05",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_2.place(x=290,y=250)

duration_time_label_2 = Label(price_sort_ascending,text="1h 05m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_2.place(x=405,y=250)

price_show_label_2 = Label(price_sort_ascending,textvariable=var_price_2,fg="darkorange",font =30,bg="#202A44")
price_show_label_2.place(x=520,y=250)

book_button_2= Button(price_sort_ascending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command= lambda:show_frame(frame3),bd=0)
book_button_2["font"] = ("Consolas",13,"bold")
book_button_2.place(x=605,y=250)


airlines_name_label_3 = Label(price_sort_ascending,text="Spicejet",fg="darkorange",font =30,bg="#202A44")
spicejet_img_price_sort_ascending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/spicejet-logo.jpg")
spicejet_resize_image_price_sort_ascending = spicejet_img.resize((70,50))
#Convert To photoimage
spicejet_tkimage_price_sort_ascending= ImageTk.PhotoImage(spicejet_resize_image_price_sort_ascending)
#Display the Image
label=Label(price_sort_ascending,image=spicejet_tkimage_price_sort_ascending)
label.place(x=40,y=100)

departure_time_label_3 = Label(price_sort_ascending,text="08:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_3.place(x=155,y=100)

arrival_time_label_3 = Label(price_sort_ascending,text="09:25",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_3.place(x=290,y=100)

duration_time_label_3 = Label(price_sort_ascending,text="1h 25m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_3.place(x=405,y=100)

price_show_label_3 = Label(price_sort_ascending,textvariable=var_price_3,fg="darkorange",font =30,bg="#202A44")
price_show_label_3.place(x=520,y=100)

book_button_3= Button(price_sort_ascending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_3["font"] = ("Consolas",13,"bold")
book_button_3.place(x=605,y=100)

airlines_name_label_4 = Label(price_sort_ascending,text="Air Asia",fg="darkorange",font =30,bg="#202A44")
airasia_img_price_sort_ascending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/airasia-logo.jpg")
airasia_resize_image_price_sort_ascending = airasia_img.resize((70,50))
#Convert To photoimage
airasia_tkimage_price_sort_ascending= ImageTk.PhotoImage(airasia_resize_image_price_sort_ascending)
#Display the Image
label=Label(price_sort_ascending,image=airasia_tkimage_price_sort_ascending)
label.place(x=40,y=325)

departure_time_label_4 = Label(price_sort_ascending,text="17:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_4.place(x=155,y=325)

arrival_time_label_4 = Label(price_sort_ascending,text="18:15",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_4.place(x=290,y=325)

duration_time_label_4 = Label(price_sort_ascending,text="1h 15m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_4.place(x=405,y=325)

price_show_label_4 = Label(price_sort_ascending,textvariable=var_price_4,fg="darkorange",font =30,bg="#202A44")
price_show_label_4.place(x=520,y=325)

book_button_4= Button(price_sort_ascending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_4["font"] = ("Consolas",13,"bold")
book_button_4.place(x=605,y=325)





                                                                #PRICE SORT DESCENDING: 
bracket = Frame(price_sort_descending,bg="darkorange",width=650,height=50)
bracket.place(x=30,y=40)


back_button = Button(price_sort_descending)
back_button["text"] = ("Back")
back_button["font"] = ("Consolas",13,"bold")
back_button["fg"] = ("#202A44")
back_button["bg"] = ("darkorange")
back_button["bd"] = 0
back_button["activebackground"] = ("darkorange")
back_button["activeforeground"] = ("#202A44")
back_button["command"] = lambda:show_frame(frame1)
back_button.place(x=50,y=450)

airline_label = Button(price_sort_descending)
airline_label["text"] = ("Airline")
airline_label["font"] = ("Consolas",13,"bold")
airline_label["fg"] = ("#202A44")
airline_label["bg"] = ("darkorange")
airline_label["bd"] = (0)
airline_label["activebackground"] = ("darkorange")
airline_label["activeforeground"] = ("#202A44")
airline_label.place(x=50,y=55)

departure_label = Button(price_sort_descending)
departure_label["text"] = ("Departure ↑↓")
departure_label["font"] = ("Consolas",13,"bold")
departure_label["fg"] = ("#202A44")
departure_label["bg"] = ("darkorange")
departure_label["bd"] = (0)
departure_label["activebackground"] = ("darkorange")
departure_label["activeforeground"] = ("#202A44")
departure_label["command"] = lambda:show_frame(departure_sort)
departure_label.place(x=150,y=55)

arrival_label = Button(price_sort_descending)
arrival_label["text"] = ("Arrival")
arrival_label["font"] = ("Consolas",13,"bold")
arrival_label["fg"] = ("#202A44")
arrival_label["bg"] = ("darkorange")
arrival_label["bd"] = (0)
arrival_label["activebackground"] = ("darkorange")
arrival_label["activeforeground"] = ("#202A44")
arrival_label.place(x=285,y=55)

duration_button = Button(price_sort_descending)
duration_button["text"] = ("Duration ↑↓")
duration_button["font"] = ("Consolas",13,"bold")
duration_button["fg"] = ("#202A44")
duration_button["bg"] = ("darkorange")
duration_button["bd"] = (0)
duration_button["activebackground"] = ("darkorange")
duration_button["activeforeground"] = ("#202A44")
duration_button["command"] = lambda:show_frame(duration_sort)
duration_button.place(x=400,y=55)

price_button = Button(price_sort_descending)
price_button["text"] = ("Price ↓")
price_button["font"] = ("Consolas",13,"bold")
price_button["fg"] = ("#202A44")
price_button["bg"] = ("darkorange")
price_button["bd"] = (0)
price_button["activebackground"] = ("darkorange")
price_button["activeforeground"] = ("#202A44")
price_button["command"] = lambda:show_frame(frame2)
price_button.place(x=520,y=55)

totalenger = Label(price_sort_descending)
totalenger["fg"] = "darkorange"
totalenger["bg"] = "#202A44"
totalenger["textvariable"] = var_total
totalenger.place(x=520,y=130)

arrival_label = Label(price_sort_descending)
arrival_label["bg"] = ("#202A44")
arrival_label["fg"] = ("darkorange")
arrival_label["textvariable"] = (var_arrival)
arrival_label.place(x=285,y=130)

departure_label = Label(price_sort_descending)
departure_label["bg"] = ("#202A44")
departure_label["fg"] = ("darkorange")
departure_label["textvariable"] = (var_departure)
departure_label.place(x=150,y=130)

airline_logo = Label(price_sort_descending,font=30,bg="#202A44",fg="darkorange")
airline_logo["text"] = ("Indigo")
indigo_img_price_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/indigo-logo.jpg")
indigo_resize_image_price_sort_descending = indigo_img.resize((70,50))
#Convert To photoimage
indigo_tkimage_price_sort_descending= ImageTk.PhotoImage(indigo_resize_image_price_sort_descending)
#Display the Image
label=Label(price_sort_descending,image=indigo_tkimage_price_sort_descending)
label.place(x=40,y=250)

departure_time_label = Label(price_sort_descending,fg="darkorange",bg="#202A44")
departure_time_label["text"] = ("05:05")
departure_time_label["font"] = (18)
departure_time_label.place(x=155,y=250)

arrival_time_label = Label(price_sort_descending,fg="darkorange",bg="#202A44",)
arrival_time_label["text"] = ("06:15")
arrival_time_label["font"] = (18)
arrival_time_label.place(x=290,y=250)

duration_label = Label(price_sort_descending,fg="darkorange",bg="#202A44")
duration_label["text"] = ("1h 10m")
duration_label["font"] = (18)
duration_label.place(x=405,y=250)

price_show_label = Label(price_sort_descending,textvariable=var_price_1,fg="darkorange",font =30,bg="#202A44")
price_show_label.place(x=520,y=250) 

book_button= Button(price_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button["font"] = ("Consolas",13,"bold")
book_button.place(x=605,y=250)

airlines_name_label_2 = Label(price_sort_descending,text="Vistara",fg="darkorange",font =30,bg="#202A44")
vistara_img_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/vistara-logo.jpg")
vistara_resize_image_descending = vistara_img_ascending.resize((70,50))
#Convert To photoimage
vistara_tkimage_descending= ImageTk.PhotoImage(vistara_resize_image_descending)
#Display the Image
label=Label(price_sort_descending,image=vistara_tkimage_descending)
label.place(x=40,y=175)

departure_time_label_2 = Label(price_sort_descending,text="16:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_2.place(x=155,y=175)

arrival_time_label_2 = Label(price_sort_descending,text="17:05",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_2.place(x=290,y=175)

duration_time_label_2 = Label(price_sort_descending,text="1h 05m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_2.place(x=405,y=175)

price_show_label_2 = Label(price_sort_descending,textvariable=var_price_2,fg="darkorange",font =30,bg="#202A44")
price_show_label_2.place(x=520,y=175)

book_button_2= Button(price_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command= flight2,bd=0)
book_button_2["font"] = ("Consolas",13,"bold")
book_button_2.place(x=605,y=175)

airlines_name_label_3 = Label(price_sort_descending,text="Spicejet",fg="darkorange",font =30,bg="#202A44")
spicejet_img_price_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/spicejet-logo.jpg")
spicejet_resize_image_price_sort_descending = spicejet_img.resize((70,50))
#Convert To photoimage
spicejet_tkimage_price_sort_descending= ImageTk.PhotoImage(spicejet_resize_image_price_sort_descending)
#Display the Image
label=Label(price_sort_descending,image=spicejet_tkimage_price_sort_descending)
label.place(x=40,y=325)

departure_time_label_3 = Label(price_sort_descending,text="08:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_3.place(x=155,y=325)

arrival_time_label_3 = Label(price_sort_descending,text="09:25",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_3.place(x=290,y=325)

duration_time_label_3 = Label(price_sort_descending,text="1h 25m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_3.place(x=405,y=325)

price_show_label_3 = Label(price_sort_descending,textvariable=var_price_3,fg="darkorange",font =30,bg="#202A44")
price_show_label_3.place(x=520,y=325)

book_button_3= Button(price_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=flight3,bd=0)
book_button_3["font"] = ("Consolas",13,"bold")
book_button_3.place(x=605,y=325)

airlines_name_label_4 = Label(price_sort_descending,text="Air Asia",fg="darkorange",font =30,bg="#202A44")
airasia_img_price_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/airasia-logo.jpg")
airasia_resize_image_price_sort_descending = airasia_img.resize((70,50))
#Convert To photoimage
airasia_tkimage_price_sort_descending= ImageTk.PhotoImage(airasia_resize_image_price_sort_descending)
#Display the Image
label=Label(price_sort_descending,image=airasia_tkimage_price_sort_descending)
label.place(x=40,y=100)

departure_time_label_4 = Label(price_sort_descending,text="17:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_4.place(x=155,y=100)

arrival_time_label_4 = Label(price_sort_descending,text="18:15",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_4.place(x=290,y=100)

duration_time_label_4 = Label(price_sort_descending,text="1h 15m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_4.place(x=405,y=100)

price_show_label_4 = Label(price_sort_descending,textvariable=var_price_4,fg="darkorange",font =30,bg="#202A44")
price_show_label_4.place(x=520,y=100)

book_button_4= Button(price_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=flight4,bd=0)
book_button_4["font"] = ("Consolas",13,"bold")
book_button_4.place(x=605,y=100)




                                                                #DURATION SORT ASCENDING:
bracket = Frame(duration_sort,bg="darkorange",width=650,height=50)
bracket.place(x=30,y=40)


back_button = Button(duration_sort)
back_button["text"] = ("Back")
back_button["font"] = ("Consolas",13,"bold")
back_button["fg"] = ("#202A44")
back_button["bg"] = ("darkorange")
back_button["bd"] = 0
back_button["activebackground"] = ("darkorange")
back_button["activeforeground"] = ("#202A44")
back_button["command"] = lambda:show_frame(frame1)
back_button.place(x=50,y=450)

airline_label = Button(duration_sort)
airline_label["text"] = ("Airline")
airline_label["font"] = ("Consolas",13,"bold")
airline_label["fg"] = ("#202A44")
airline_label["bg"] = ("darkorange")
airline_label["bd"] = (0)
airline_label["activebackground"] = ("darkorange")
airline_label["activeforeground"] = ("#202A44")
airline_label.place(x=50,y=55)


departure_label = Button(duration_sort)
departure_label["text"] = ("Departure ↑↓")
departure_label["font"] = ("Consolas",13,"bold")
departure_label["fg"] = ("#202A44")
departure_label["bg"] = ("darkorange")
departure_label["bd"] = (0)
departure_label["activebackground"] = ("darkorange")
departure_label["activeforeground"] = ("#202A44")
departure_label["command"] = lambda:show_frame(departure_sort)
departure_label.place(x=150,y=55)

arrival_label = Button(duration_sort)
arrival_label["text"] = ("Arrival")
arrival_label["font"] = ("Consolas",13,"bold")
arrival_label["fg"] = ("#202A44")
arrival_label["bg"] = ("darkorange")
arrival_label["bd"] = (0)
arrival_label["activebackground"] = ("darkorange")
arrival_label["activeforeground"] = ("#202A44")
arrival_label.place(x=285,y=55)

duration_button = Button(duration_sort)
duration_button["text"] = ("Duration ↑")
duration_button["font"] = ("Consolas",13,"bold")
duration_button["fg"] = ("#202A44")
duration_button["bg"] = ("darkorange")
duration_button["bd"] = (0)
duration_button["activebackground"] = ("darkorange")
duration_button["activeforeground"] = ("#202A44")
duration_button["command"] = lambda:show_frame(duration_sort_descending)
duration_button.place(x=400,y=55)

price_button = Button(duration_sort)
price_button["text"] = ("Price ↑↓")
price_button["font"] = ("Consolas",13,"bold")
price_button["fg"] = ("#202A44")
price_button["bg"] = ("darkorange")
price_button["bd"] = (0)
price_button["activebackground"] = ("darkorange")
price_button["activeforeground"] = ("#202A44")
price_button["command"] = lambda:show_frame(price_sort_ascending)
price_button.place(x=520,y=55)

totalenger = Label(duration_sort)
totalenger["fg"] = "darkorange"
totalenger["bg"] = "#202A44"
totalenger["textvariable"] = var_total
totalenger.place(x=520,y=130)

arrival_label = Label(duration_sort)
arrival_label["bg"] = ("#202A44")
arrival_label["fg"] = ("darkorange")
arrival_label["textvariable"] = (var_arrival)
arrival_label.place(x=285,y=130)

departure_label = Label(duration_sort)
departure_label["bg"] = ("#202A44")
departure_label["fg"] = ("darkorange")
departure_label["textvariable"] = (var_departure)
departure_label.place(x=150,y=130)

airline_logo = Label(duration_sort,font=30,bg="#202A44",fg="darkorange")
airline_logo["text"] = ("Indigo")
indigo_img_duration_sort= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/indigo-logo.jpg")
indigo_resize_image_duration_sort = indigo_img.resize((70,50))
#Convert To photoimage
indigo_tkimage_duration_sort= ImageTk.PhotoImage(indigo_resize_image_duration_sort)
#Display the Image
label=Label(duration_sort,image=indigo_tkimage_duration_sort)
label.place(x=40,y=175)

departure_time_label = Label(duration_sort,fg="darkorange",bg="#202A44")
departure_time_label["text"] = ("05:05")
departure_time_label["font"] = (18)
departure_time_label.place(x=155,y=175)

arrival_time_label = Label(duration_sort,fg="darkorange",bg="#202A44",)
arrival_time_label["text"] = ("06:15")
arrival_time_label["font"] = (18)
arrival_time_label.place(x=290,y=175)

duration_label = Label(duration_sort,fg="darkorange",bg="#202A44")
duration_label["text"] = ("1h 10m")
duration_label["font"] = (18)
duration_label.place(x=405,y=175)

price_show_label = Label(duration_sort,textvariable=var_price_1,fg="darkorange",font =30,bg="#202A44")
price_show_label.place(x=520,y=175) 

book_button= Button(duration_sort,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button["font"] = ("Consolas",13,"bold")
book_button.place(x=605,y=175)

airlines_name_label_2 = Label(duration_sort,text="Vistara",fg="darkorange",font =30,bg="#202A44")
vistara_img_duration_sort= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/vistara-logo.jpg")
vistara_resize_image_duration_sort = vistara_img_ascending.resize((70,50))
#Convert To photoimage
vistara_tkimage_duration_sort= ImageTk.PhotoImage(vistara_resize_image_duration_sort)
#Display the Image
label=Label(duration_sort,image=vistara_tkimage_duration_sort)
label.place(x=40,y=100)

departure_time_label_2 = Label(duration_sort,text="16:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_2.place(x=155,y=100)

arrival_time_label_2 = Label(duration_sort,text="17:05",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_2.place(x=290,y=100)

duration_time_label_2 = Label(duration_sort,text="1h 05m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_2.place(x=405,y=100)

price_show_label_2 = Label(duration_sort,textvariable=var_price_2,fg="darkorange",font =30,bg="#202A44")
price_show_label_2.place(x=520,y=100)

book_button_2= Button(duration_sort,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command= lambda:show_frame(frame3),bd=0)
book_button_2["font"] = ("Consolas",13,"bold")
book_button_2.place(x=605,y=100)

airlines_name_label_3 = Label(duration_sort,text="Spicejet",fg="darkorange",font =30,bg="#202A44")
spicejet_img_duration_sort= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/spicejet-logo.jpg")
spicejet_resize_image_duration_sort = spicejet_img.resize((70,50))
#Convert To photoimage
spicejet_tkimage_duration_sort= ImageTk.PhotoImage(spicejet_resize_image_duration_sort)
#Display the Image
label=Label(duration_sort,image=spicejet_tkimage_duration_sort)
label.place(x=40,y=325)

departure_time_label_3 = Label(duration_sort,text="08:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_3.place(x=155,y=325)

arrival_time_label_3 = Label(duration_sort,text="09:25",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_3.place(x=290,y=325)

duration_time_label_3 = Label(duration_sort,text="1h 25m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_3.place(x=405,y=325)

price_show_label_3 = Label(duration_sort,textvariable=var_price_3,fg="darkorange",font =30,bg="#202A44")
price_show_label_3.place(x=520,y=325)

book_button_3= Button(duration_sort,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_3["font"] = ("Consolas",13,"bold")
book_button_3.place(x=605,y=325)

airlines_name_label_4 = Label(duration_sort,text="Air Asia",fg="darkorange",font =30,bg="#202A44")
airasia_img_duration_sort= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/airasia-logo.jpg")
airasia_resize_image_duration_sort = airasia_img.resize((70,50))
#Convert To photoimage
airasia_tkimage_duration_sort= ImageTk.PhotoImage(airasia_resize_image_duration_sort)
#Display the Image
label=Label(duration_sort,image=airasia_tkimage_duration_sort)
label.place(x=40,y=250)


departure_time_label_4 = Label(duration_sort,text="17:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_4.place(x=155,y=250)

arrival_time_label_4 = Label(duration_sort,text="18:15",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_4.place(x=290,y=250)

duration_time_label_4 = Label(duration_sort,text="1h 15m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_4.place(x=405,y=250)

price_show_label_4 = Label(duration_sort,textvariable=var_price_4,fg="darkorange",font =30,bg="#202A44")
price_show_label_4.place(x=520,y=250)

book_button_4= Button(duration_sort,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_4["font"] = ("Consolas",13,"bold")
book_button_4.place(x=605,y=250)




                                                                #DURATION SORT DESCENDING:
bracket = Frame(duration_sort_descending,bg="darkorange",width=650,height=50)
bracket.place(x=30,y=40)


back_button = Button(duration_sort_descending)
back_button["text"] = ("Back")
back_button["font"] = ("Consolas",13,"bold")
back_button["fg"] = ("#202A44")
back_button["bg"] = ("darkorange")
back_button["bd"] = 0
back_button["activebackground"] = ("darkorange")
back_button["activeforeground"] = ("#202A44")
back_button["command"] = lambda:show_frame(frame1)
back_button.place(x=50,y=450)

airline_label = Button(duration_sort_descending)
airline_label["text"] = ("Airline")
airline_label["font"] = ("Consolas",13,"bold")
airline_label["fg"] = ("#202A44")
airline_label["bg"] = ("darkorange")
airline_label["bd"] = (0)
airline_label["activebackground"] = ("darkorange")
airline_label["activeforeground"] = ("#202A44")
airline_label.place(x=50,y=55)

departure_label = Button(duration_sort_descending)
departure_label["text"] = ("Departure ↑↓")
departure_label["font"] = ("Consolas",13,"bold")
departure_label["fg"] = ("#202A44")
departure_label["bg"] = ("darkorange")
departure_label["bd"] = (0)
departure_label["activebackground"] = ("darkorange")
departure_label["activeforeground"] = ("#202A44")
departure_label["command"] = lambda:show_frame(departure_sort)
departure_label.place(x=150,y=55)

arrival_label = Button(duration_sort_descending)
arrival_label["text"] = ("Arrival")
arrival_label["font"] = ("Consolas",13,"bold")
arrival_label["fg"] = ("#202A44")
arrival_label["bg"] = ("darkorange")
arrival_label["bd"] = (0)
arrival_label["activebackground"] = ("darkorange")
arrival_label["activeforeground"] = ("#202A44")
arrival_label.place(x=285,y=55)

duration_button = Button(duration_sort_descending)
duration_button["text"] = ("Duration ↓")
duration_button["font"] = ("Consolas",13,"bold")
duration_button["fg"] = ("#202A44")
duration_button["bg"] = ("darkorange")
duration_button["bd"] = (0)
duration_button["activebackground"] = ("darkorange")
duration_button["activeforeground"] = ("#202A44")
duration_button["command"] = lambda:show_frame(frame2)
duration_button.place(x=400,y=55)

price_button = Button(duration_sort_descending)
price_button["text"] = ("Price ↑↓")
price_button["font"] = ("Consolas",13,"bold")
price_button["fg"] = ("#202A44")
price_button["bg"] = ("darkorange")
price_button["bd"] = (0)
price_button["activebackground"] = ("darkorange")
price_button["activeforeground"] = ("#202A44")
price_button["command"] = lambda:show_frame(price_sort_ascending)
price_button.place(x=520,y=55)

totalenger = Label(duration_sort_descending)
totalenger["fg"] = "darkorange"
totalenger["bg"] = "#202A44"
totalenger["textvariable"] = var_total
totalenger.place(x=520,y=130)

arrival_label = Label(duration_sort_descending)
arrival_label["bg"] = ("#202A44")
arrival_label["fg"] = ("darkorange")
arrival_label["textvariable"] = (var_arrival)
arrival_label.place(x=285,y=130)

departure_label = Label(duration_sort_descending)
departure_label["bg"] = ("#202A44")
departure_label["fg"] = ("darkorange")
departure_label["textvariable"] = (var_departure)
departure_label.place(x=150,y=130)

airline_logo = Label(duration_sort_descending,font=30,bg="#202A44",fg="darkorange")
airline_logo["text"] = ("Indigo")
indigo_img_duration_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/indigo-logo.jpg")
indigo_resize_image_duration_sort_descending = indigo_img.resize((70,50))
#Convert To photoimage
indigo_tkimage_duration_sort_descending= ImageTk.PhotoImage(indigo_resize_image_duration_sort_descending)
#Display the Image
label=Label(duration_sort_descending,image=indigo_tkimage_duration_sort_descending)
label.place(x=40,y=250)

departure_time_label = Label(duration_sort_descending,fg="darkorange",bg="#202A44")
departure_time_label["text"] = ("05:05")
departure_time_label["font"] = (18)
departure_time_label.place(x=155,y=250)

arrival_time_label = Label(duration_sort_descending,fg="darkorange",bg="#202A44",)
arrival_time_label["text"] = ("06:15")
arrival_time_label["font"] = (18)
arrival_time_label.place(x=290,y=250)

duration_label = Label(duration_sort_descending,fg="darkorange",bg="#202A44")
duration_label["text"] = ("1h 10m")
duration_label["font"] = (18)
duration_label.place(x=405,y=250)

price_show_label = Label(duration_sort_descending,textvariable=var_price_1,fg="darkorange",font =30,bg="#202A44")
price_show_label.place(x=520,y=250) 

book_button= Button(duration_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button["font"] = ("Consolas",13,"bold")
book_button.place(x=605,y=250)

airlines_name_label_2 = Label(duration_sort_descending,text="Vistara",fg="darkorange",font =30,bg="#202A44")
vistara_img_duration_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/vistara-logo.jpg")
vistara_resize_image_duration_sort_descending = vistara_img_ascending.resize((70,50))
#Convert To photoimage
vistara_tkimage_duration_sort_descending= ImageTk.PhotoImage(vistara_resize_image_duration_sort_descending)
#Display the Image
label=Label(duration_sort_descending,image=vistara_tkimage_duration_sort_descending)
label.place(x=40,y=325)

departure_time_label_2 = Label(duration_sort_descending,text="16:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_2.place(x=155,y=325)

arrival_time_label_2 = Label(duration_sort_descending,text="17:05",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_2.place(x=290,y=325)

duration_time_label_2 = Label(duration_sort_descending,text="1h 05m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_2.place(x=405,y=325)

price_show_label_2 = Label(duration_sort_descending,textvariable=var_price_2,fg="darkorange",font =30,bg="#202A44")
price_show_label_2.place(x=520,y=325)

book_button_2= Button(duration_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command= lambda:show_frame(frame3),bd=0)
book_button_2["font"] = ("Consolas",13,"bold")
book_button_2.place(x=605,y=325)

airlines_name_label_3 = Label(duration_sort_descending,text="Spicejet",fg="darkorange",font =30,bg="#202A44")
spicejet_img_duration_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/spicejet-logo.jpg")
spicejet_resize_image_duration_sort_descending = spicejet_img.resize((70,50))
#Convert To photoimage
spicejet_tkimage_duration_sort_descending= ImageTk.PhotoImage(spicejet_resize_image_duration_sort_descending)
#Display the Image
label=Label(duration_sort_descending,image=spicejet_tkimage_duration_sort_descending)
label.place(x=40,y=100)

departure_time_label_3 = Label(duration_sort_descending,text="08:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_3.place(x=155,y=100)

arrival_time_label_3 = Label(duration_sort_descending,text="09:25",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_3.place(x=290,y=100)

duration_time_label_3 = Label(duration_sort_descending,text="1h 25m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_3.place(x=405,y=100)

price_show_label_3 = Label(duration_sort_descending,textvariable=var_price_3,fg="darkorange",font =30,bg="#202A44")
price_show_label_3.place(x=520,y=100)

book_button_3= Button(duration_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_3["font"] = ("Consolas",13,"bold")
book_button_3.place(x=605,y=100)

airlines_name_label_4 = Label(duration_sort_descending,text="Air Asia",fg="darkorange",font =30,bg="#202A44")
airasia_img_duration_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/airasia-logo.jpg")
airasia_resize_image_duration_sort_descending = airasia_img.resize((70,50))
#Convert To photoimage
airasia_tkimage_duration_sort_descending= ImageTk.PhotoImage(airasia_resize_image_duration_sort_descending)
#Display the Image
label=Label(duration_sort_descending,image=airasia_tkimage_duration_sort_descending)
label.place(x=40,y=175)

departure_time_label_4 = Label(duration_sort_descending,text="17:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_4.place(x=155,y=175)

arrival_time_label_4 = Label(duration_sort_descending,text="18:15",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_4.place(x=290,y=175)

duration_time_label_4 = Label(duration_sort_descending,text="1h 15m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_4.place(x=405,y=175)

price_show_label_4 = Label(duration_sort_descending,textvariable=var_price_4,fg="darkorange",font =30,bg="#202A44")
price_show_label_4.place(x=520,y=175)

book_button_4= Button(duration_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_4["font"] = ("Consolas",13,"bold")
book_button_4.place(x=605,y=175)




                                                                #DEPARTURE SORT ASCENDING:
bracket = Frame(departure_sort,bg="darkorange",width=650,height=50)
bracket.place(x=30,y=40)


back_button = Button(departure_sort)
back_button["text"] = ("Back")
back_button["font"] = ("Consolas",13,"bold")
back_button["fg"] = ("#202A44")
back_button["bg"] = ("darkorange")
back_button["bd"] = 0
back_button["activebackground"] = ("darkorange")
back_button["activeforeground"] = ("#202A44")
back_button["command"] = lambda:show_frame(frame1)
back_button.place(x=50,y=450)

airline_label = Button(departure_sort)
airline_label["text"] = ("Airline")
airline_label["font"] = ("Consolas",13,"bold")
airline_label["fg"] = ("#202A44")
airline_label["bg"] = ("darkorange")
airline_label["bd"] = (0)
airline_label["activebackground"] = ("darkorange")
airline_label["activeforeground"] = ("#202A44")
airline_label.place(x=50,y=55)


departure_label = Button(departure_sort)
departure_label["text"] = ("Departure ↑")
departure_label["font"] = ("Consolas",13,"bold")
departure_label["fg"] = ("#202A44")
departure_label["bg"] = ("darkorange")
departure_label["bd"] = (0)
departure_label["activebackground"] = ("darkorange")
departure_label["activeforeground"] = ("#202A44")
departure_label["command"] = lambda:show_frame(departure_sort_descending)
departure_label.place(x=150,y=55)

arrival_label = Button(departure_sort)
arrival_label["text"] = ("Arrival")
arrival_label["font"] = ("Consolas",13,"bold")
arrival_label["fg"] = ("#202A44")
arrival_label["bg"] = ("darkorange")
arrival_label["bd"] = (0)
arrival_label["activebackground"] = ("darkorange")
arrival_label["activeforeground"] = ("#202A44")
arrival_label.place(x=285,y=55)

duration_button = Button(departure_sort)
duration_button["text"] = ("Duration ↑↓")
duration_button["font"] = ("Consolas",13,"bold")
duration_button["fg"] = ("#202A44")
duration_button["bg"] = ("darkorange")
duration_button["bd"] = (0)
duration_button["activebackground"] = ("darkorange")
duration_button["activeforeground"] = ("#202A44")
duration_button["command"] = lambda:show_frame(duration_sort)
duration_button.place(x=400,y=55)

price_button = Button(departure_sort)
price_button["text"] = ("Price ↑↓")
price_button["font"] = ("Consolas",13,"bold")
price_button["fg"] = ("#202A44")
price_button["bg"] = ("darkorange")
price_button["bd"] = (0)
price_button["activebackground"] = ("darkorange")
price_button["activeforeground"] = ("#202A44")
price_button["command"] = lambda:show_frame(price_sort_ascending)
price_button.place(x=520,y=55)

totalenger = Label(departure_sort)
totalenger["fg"] = "darkorange"
totalenger["bg"] = "#202A44"
totalenger["textvariable"] = var_total
totalenger.place(x=520,y=130)

arrival_label = Label(departure_sort)
arrival_label["bg"] = ("#202A44")
arrival_label["fg"] = ("darkorange")
arrival_label["textvariable"] = (var_arrival)
arrival_label.place(x=285,y=130)

departure_label = Label(departure_sort)
departure_label["bg"] = ("#202A44")
departure_label["fg"] = ("darkorange")
departure_label["textvariable"] = (var_departure)
departure_label.place(x=150,y=130)

airline_logo = Label(departure_sort,font=30,bg="#202A44",fg="darkorange")
airline_logo["text"] = ("Indigo")
indigo_img_departure_sort= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/indigo-logo.jpg")
indigo_resize_image_departure_sort = indigo_img.resize((70,50))
#Convert To photoimage
indigo_tkimage_departure_sort= ImageTk.PhotoImage(indigo_resize_image_departure_sort)
#Display the Image
label=Label(departure_sort,image=indigo_tkimage_departure_sort)
label.place(x=40,y=100)

departure_time_label = Label(departure_sort,fg="darkorange",bg="#202A44")
departure_time_label["text"] = ("05:05")
departure_time_label["font"] = (18)
departure_time_label.place(x=155,y=100)

arrival_time_label = Label(departure_sort,fg="darkorange",bg="#202A44",)
arrival_time_label["text"] = ("06:15")
arrival_time_label["font"] = (18)
arrival_time_label.place(x=290,y=100)

duration_label = Label(departure_sort,fg="darkorange",bg="#202A44")
duration_label["text"] = ("1h 10m")
duration_label["font"] = (18)
duration_label.place(x=405,y=100)

price_show_label = Label(departure_sort,textvariable=var_price_1,fg="darkorange",font =30,bg="#202A44")
price_show_label.place(x=520,y=100) 

book_button= Button(departure_sort,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button["font"] = ("Consolas",13,"bold")
book_button.place(x=605,y=100)

airlines_name_label_2 = Label(departure_sort,text="Vistara",fg="darkorange",font =30,bg="#202A44")
vistara_img_departure_sort= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/vistara-logo.jpg")
vistara_resize_image_departure_sort = vistara_img_ascending.resize((70,50))
#Convert To photoimage
vistara_tkimage_departure_sort= ImageTk.PhotoImage(vistara_resize_image_departure_sort)
#Display the Image
label=Label(departure_sort,image=vistara_tkimage_departure_sort)
label.place(x=40,y=250)

departure_time_label_2 = Label(departure_sort,text="16:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_2.place(x=155,y=250)

arrival_time_label_2 = Label(departure_sort,text="17:05",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_2.place(x=290,y=250)

duration_time_label_2 = Label(departure_sort,text="1h 05m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_2.place(x=405,y=250)

price_show_label_2 = Label(departure_sort,textvariable=var_price_2,fg="darkorange",font =30,bg="#202A44")
price_show_label_2.place(x=520,y=250)

book_button_2= Button(departure_sort,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command= lambda:show_frame(frame3),bd=0)
book_button_2["font"] = ("Consolas",13,"bold")
book_button_2.place(x=605,y=250)

airlines_name_label_3 = Label(departure_sort,text="Spicejet",fg="darkorange",font =30,bg="#202A44")
spicejet_img_departure_sort= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/spicejet-logo.jpg")
spicejet_resize_image_departure_sort = spicejet_img.resize((70,50))
#Convert To photoimage
spicejet_tkimage_departure_sort= ImageTk.PhotoImage(spicejet_resize_image_departure_sort)
#Display the Image
label=Label(departure_sort,image=spicejet_tkimage_departure_sort)
label.place(x=40,y=175)

departure_time_label_3 = Label(departure_sort,text="08:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_3.place(x=155,y=175)

arrival_time_label_3 = Label(departure_sort,text="09:25",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_3.place(x=290,y=175)

duration_time_label_3 = Label(departure_sort,text="1h 25m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_3.place(x=405,y=175)

price_show_label_3 = Label(departure_sort,textvariable=var_price_3,fg="darkorange",font =30,bg="#202A44")
price_show_label_3.place(x=520,y=175)

book_button_3= Button(departure_sort,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_3["font"] = ("Consolas",13,"bold")
book_button_3.place(x=605,y=175)

airlines_name_label_4 = Label(departure_sort,text="Air Asia",fg="darkorange",font =30,bg="#202A44")
airasia_img_departure_sort= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/airasia-logo.jpg")
airasia_resize_image_departure_sort = airasia_img.resize((70,50))
#Convert To photoimage
airasia_tkimage_departure_sort= ImageTk.PhotoImage(airasia_resize_image_departure_sort)
#Display the Image
label=Label(departure_sort,image=airasia_tkimage_departure_sort)
label.place(x=40,y=325)

departure_time_label_4 = Label(departure_sort,text="17:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_4.place(x=155,y=325)

arrival_time_label_4 = Label(departure_sort,text="18:15",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_4.place(x=290,y=325)

duration_time_label_4 = Label(departure_sort,text="1h 15m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_4.place(x=405,y=325)

price_show_label_4 = Label(departure_sort,textvariable=var_price_4,fg="darkorange",font =30,bg="#202A44")
price_show_label_4.place(x=520,y=325)

book_button_4= Button(departure_sort,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_4["font"] = ("Consolas",13,"bold")
book_button_4.place(x=605,y=325)




                                                                #DEPARTURE SORT DESCENDING:
bracket = Frame(departure_sort_descending,bg="darkorange",width=650,height=50)
bracket.place(x=30,y=40)


back_button = Button(departure_sort_descending)
back_button["text"] = ("Back")
back_button["font"] = ("Consolas",13,"bold")
back_button["fg"] = ("#202A44")
back_button["bg"] = ("darkorange")
back_button["bd"] = 0
back_button["activebackground"] = ("darkorange")
back_button["activeforeground"] = ("#202A44")
back_button["command"] = lambda:show_frame(frame1)
back_button.place(x=50,y=450)

airline_label = Button(departure_sort_descending)
airline_label["text"] = ("Airline")
airline_label["font"] = ("Consolas",13,"bold")
airline_label["fg"] = ("#202A44")
airline_label["bg"] = ("darkorange")
airline_label["bd"] = (0)
airline_label["activebackground"] = ("darkorange")
airline_label["activeforeground"] = ("#202A44")
airline_label.place(x=50,y=55)


departure_label = Button(departure_sort_descending)
departure_label["text"] = ("Departure ↓")
departure_label["font"] = ("Consolas",13,"bold")
departure_label["fg"] = ("#202A44")
departure_label["bg"] = ("darkorange")
departure_label["bd"] = (0)
departure_label["activebackground"] = ("darkorange")
departure_label["activeforeground"] = ("#202A44")
departure_label["command"] = lambda:show_frame(frame2)
departure_label.place(x=150,y=55)

arrival_label = Button(departure_sort_descending)
arrival_label["text"] = ("Arrival")
arrival_label["font"] = ("Consolas",13,"bold")
arrival_label["fg"] = ("#202A44")
arrival_label["bg"] = ("darkorange")
arrival_label["bd"] = (0)
arrival_label["activebackground"] = ("darkorange")
arrival_label["activeforeground"] = ("#202A44")
arrival_label.place(x=285,y=55)

duration_button = Button(departure_sort_descending)
duration_button["text"] = ("Duration ↑↓")
duration_button["font"] = ("Consolas",13,"bold")
duration_button["fg"] = ("#202A44")
duration_button["bg"] = ("darkorange")
duration_button["bd"] = (0)
duration_button["activebackground"] = ("darkorange")
duration_button["activeforeground"] = ("#202A44")
duration_button["command"] = lambda:show_frame(duration_sort)
duration_button.place(x=400,y=55)

price_button = Button(departure_sort_descending)
price_button["text"] = ("Price ↑↓")
price_button["font"] = ("Consolas",13,"bold")
price_button["fg"] = ("#202A44")
price_button["bg"] = ("darkorange")
price_button["bd"] = (0)
price_button["activebackground"] = ("darkorange")
price_button["activeforeground"] = ("#202A44")
price_button["command"] = lambda:show_frame(price_sort_ascending)
price_button.place(x=520,y=55)

totalenger = Label(departure_sort_descending)
totalenger["fg"] = "darkorange"
totalenger["bg"] = "#202A44"
totalenger["textvariable"] = var_total
totalenger.place(x=520,y=130)

arrival_label_1 = Label(departure_sort_descending)
arrival_label_1["bg"] = ("#202A44")
arrival_label_1["fg"] = ("darkorange")
arrival_label_1["textvariable"] = (var_arrival)
arrival_label_1.place(x=285,y=130)

departure_label_1 = Label(departure_sort_descending)
departure_label_1["bg"] = ("#202A44")
departure_label_1["fg"] = ("darkorange")
departure_label_1["textvariable"] = (var_departure)
departure_label_1.place(x=150,y=130)

airline_logo = Label(departure_sort_descending,font=30,bg="#202A44",fg="darkorange")
airline_logo["text"] = ("Indigo")
indigo_img_departure_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/indigo-logo.jpg")
indigo_resize_image_departure_sort_descending = indigo_img.resize((70,50))
#Convert To photoimage
indigo_tkimage_departure_sort_descending= ImageTk.PhotoImage(indigo_resize_image_departure_sort_descending)
#Display the Image
label=Label(departure_sort_descending,image=indigo_tkimage_departure_sort_descending)
label.place(x=40,y=325)

departure_time_label = Label(departure_sort_descending,fg="darkorange",bg="#202A44")
departure_time_label["text"] = ("05:05")
departure_time_label["font"] = (18)
departure_time_label.place(x=155,y=325)

arrival_time_label = Label(departure_sort_descending,fg="darkorange",bg="#202A44",)
arrival_time_label["text"] = ("06:15")
arrival_time_label["font"] = (18)
arrival_time_label.place(x=290,y=325)

duration_label = Label(departure_sort_descending,fg="darkorange",bg="#202A44")
duration_label["text"] = ("1h 10m")
duration_label["font"] = (18)
duration_label.place(x=405,y=325)

price_show_label = Label(departure_sort_descending,textvariable=var_price_1,fg="darkorange",font =30,bg="#202A44")
price_show_label.place(x=520,y=325) 

book_button= Button(departure_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button["font"] = ("Consolas",13,"bold")
book_button.place(x=605,y=325)

airlines_name_label_2 = Label(departure_sort_descending,text="Vistara",fg="darkorange",font =30,bg="#202A44")
vistara_img_departure_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/vistara-logo.jpg")
vistara_resize_image_departure_sort_descending = vistara_img_ascending.resize((70,50))
#Convert To photoimage
vistara_tkimage_departure_sort_descending= ImageTk.PhotoImage(vistara_resize_image_departure_sort_descending)
#Display the Image
label=Label(departure_sort_descending,image=vistara_tkimage_departure_sort_descending)
label.place(x=40,y=175)

departure_time_label_2 = Label(departure_sort_descending,text="16:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_2.place(x=155,y=175)

arrival_time_label_2 = Label(departure_sort_descending,text="17:05",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_2.place(x=290,y=175)

duration_time_label_2 = Label(departure_sort_descending,text="1h 05m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_2.place(x=405,y=175)

price_show_label_2 = Label(departure_sort_descending,textvariable=var_price_2,fg="darkorange",font =30,bg="#202A44")
price_show_label_2.place(x=520,y=175)

book_button_2= Button(departure_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command= lambda:show_frame(frame3),bd=0)
book_button_2["font"] = ("Consolas",13,"bold")
book_button_2.place(x=605,y=175)

airlines_name_label_3 = Label(departure_sort_descending,text="Spicejet",fg="darkorange",font =30,bg="#202A44")
spicejet_img_departure_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/spicejet-logo.jpg")
spicejet_resize_image_departure_sort_descending = spicejet_img.resize((70,50))
#Convert To photoimage
spicejet_tkimage_departure_sort_descending= ImageTk.PhotoImage(spicejet_resize_image_departure_sort_descending)
#Display the Image
label=Label(departure_sort_descending,image=spicejet_tkimage_departure_sort_descending)
label.place(x=40,y=250)

departure_time_label_3 = Label(departure_sort_descending,text="08:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_3.place(x=155,y=250)

arrival_time_label_3 = Label(departure_sort_descending,text="09:25",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_3.place(x=290,y=250)

duration_time_label_3 = Label(departure_sort_descending,text="1h 25m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_3.place(x=405,y=250)

price_show_label_3 = Label(departure_sort_descending,textvariable=var_price_3,fg="darkorange",font =30,bg="#202A44")
price_show_label_3.place(x=520,y=250)

book_button_3= Button(departure_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_3["font"] = ("Consolas",13,"bold")
book_button_3.place(x=605,y=250)

airlines_name_label_4 = Label(departure_sort_descending,text="Air Asia",fg="darkorange",font =30,bg="#202A44")
airasia_img_departure_sort_descending= Image.open("C:/Users/91816/PycharmProjects/pythonProject3/airasia-logo.jpg")
airasia_resize_image_departure_sort_descending = airasia_img.resize((70,50))
#Convert To photoimage
airasia_tkimage_departure_sort_descending= ImageTk.PhotoImage(airasia_resize_image_departure_sort_descending)
#Display the Image
label=Label(departure_sort_descending,image=airasia_tkimage_departure_sort_descending)
label.place(x=40,y=100)

departure_time_label_4 = Label(departure_sort_descending,text="17:00",fg="darkorange",font =30,bg="#202A44")
departure_time_label_4.place(x=155,y=100)

arrival_time_label_4 = Label(departure_sort_descending,text="18:15",fg="darkorange",font =30,bg="#202A44")
arrival_time_label_4.place(x=290,y=100)

duration_time_label_4 = Label(departure_sort_descending,text="1h 15m",fg="darkorange",font =30,bg="#202A44")
duration_time_label_4.place(x=405,y=100)

price_show_label_4 = Label(departure_sort_descending,textvariable=var_price_4,fg="darkorange",font =30,bg="#202A44")
price_show_label_4.place(x=520,y=100)

book_button_4= Button(departure_sort_descending,text="Book",fg="#202A44",bg="darkorange",activeforeground="#202A44",activebackground="darkorange",command=lambda:show_frame(frame3),bd=0)
book_button_4["font"] = ("Consolas",13,"bold")
book_button_4.place(x=605,y=100)








                                                                #FRAME 3:
passenger_details_label = Label(frame3,text="Passenger Details",bg="#202A44",fg="darkorange")
passenger_details_label.place(x=80,y=10)
passenger_details_label["font"] = ("Arial",25,"bold")

passenger1_label = Label(frame3,text="Passenger 1",bg="#202A44",fg="darkorange")
passenger1_label.place(x=80,y=60)
passenger1_label["font"] = ("Arial",13)

first_name_1 = Label(frame3,text="FIRST NAME",fg="darkorange",bg="#202A44")
first_name_1.place(x=80,y=120)

last_name_1 = Label(frame3,text="LAST NAME",fg="darkorange",bg="#202A44")
last_name_1.place(x=350,y=120)

passenger1_firstname_textbox = Entry(frame3,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass1_firstname)
passenger1_firstname_textbox["bg"] = ("#202A44")
passenger1_firstname_textbox["fg"] = ("darkorange")
passenger1_firstname_textbox.place(x=80,y=100)

passenger1_lastname_textbox = Entry(frame3,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass1_lastname)
passenger1_lastname_textbox["bg"] = ("#202A44")
passenger1_lastname_textbox["fg"] = ("darkorange")
passenger1_lastname_textbox.place(x=350,y=100)

gender_list = ["Male","Female"]
gender_1.set("")
pass1_gender_dropdown = OptionMenu(frame3,gender_1,*gender_list)  
pass1_gender_dropdown["fg"]=("darkorange")
pass1_gender_dropdown["activeforeground"]=("darkorange")
pass1_gender_dropdown["bg"]=("#202A44")
pass1_gender_dropdown["activebackground"]=("#202A44")  
pass1_gender_dropdown["bd"] = 0
pass1_gender_dropdown.place(x=440,y=150)

gender1_label = Label(frame3,text="Gender",fg="darkorange",bg="#202A44")
gender1_label.place(x=440,y=180)


pass1_DOB_dropdown = Spinbox(frame3,from_=1,to=30,width=5)  
pass1_DOB_dropdown["fg"]=("darkorange")
pass1_DOB_dropdown["bg"]=("#202A44")
pass1_DOB_dropdown["activebackground"]=("#202A44")  
pass1_DOB_dropdown["bd"] = 0
pass1_DOB_dropdown.place(x=80,y=150)

pass1_DOB_label = Label(frame3,text="DOB",fg="darkorange",bg="#202A44")
pass1_DOB_label.place(x=80,y=180)


pass1_MOB_dropdown = Spinbox(frame3,from_=1,to=12,width=5)  
pass1_MOB_dropdown["fg"]=("darkorange")
pass1_MOB_dropdown["bg"]=("#202A44")
pass1_MOB_dropdown["activebackground"]=("#202A44")  
pass1_MOB_dropdown["bd"] = 0
pass1_MOB_dropdown.place(x=200,y=150)

pass1_MOB_label = Label(frame3,text="Month",fg="darkorange",bg="#202A44")
pass1_MOB_label.place(x=200,y=180)

pass1_YOB_dropdown = Spinbox(frame3,from_=1920,to=2021,width=5)  
pass1_YOB_dropdown["fg"]=("darkorange")
pass1_YOB_dropdown["bg"]=("#202A44")
pass1_YOB_dropdown["activebackground"]=("#202A44")  
pass1_YOB_dropdown["bd"] = 0
pass1_YOB_dropdown.place(x=320,y=150)

pass1_YOB_label = Label(frame3,text="Year",fg="darkorange",bg="#202A44")
pass1_YOB_label.place(x=320,y=180)

add_pass2_button = Button(frame3,text="+ Add Passenger",bg="#202A44",fg="darkorange",activeforeground="darkorange",activebackground="#202A44")
add_pass2_button["command"] = second_passenger
add_pass2_button["font"] = ("Arial",10,"bold")
add_pass2_button.place(x=80,y=200)
add_pass2_button["bd"] = (0)

next_button_3= Button(frame3,text="Next",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
next_button_3["command"] = frame_3_next
next_button_3["font"] = ("Arial",13,"bold")
next_button_3.place(x=650,y=450)
next_button_3["bd"] = (0)

back_button_3 = Button(frame3,text="Back",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
back_button_3["command"] = lambda:show_frame(frame2)
back_button_3["font"] = ("Arial",13,"bold")
back_button_3.place(x=50,y=450)
back_button_3["bd"] = (0)





                                                                    #FRAME4:
passenger_details_label = Label(frame4,text="Passenger Details",bg="#202A44",fg="darkorange")
passenger_details_label.place(x=80,y=10)
passenger_details_label["font"] = ("Arial",25,"bold")

passenger1_label = Label(frame4,text="Passenger 1",bg="#202A44",fg="darkorange")
passenger1_label.place(x=80,y=60)
passenger1_label["font"] = ("Arial",13)

first_name_1 = Label(frame4,text="FIRST NAME",fg="darkorange",bg="#202A44")
first_name_1.place(x=80,y=120)

last_name_1 = Label(frame4,text="LAST NAME",fg="darkorange",bg="#202A44")
last_name_1.place(x=350,y=120)

passenger1_firstname_textbox = Entry(frame4,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass1_firstname)
passenger1_firstname_textbox["bg"] = ("#202A44")
passenger1_firstname_textbox["fg"] = ("darkorange")
passenger1_firstname_textbox.place(x=80,y=100)

passenger1_lastname_textbox = Entry(frame4,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass1_lastname)
passenger1_lastname_textbox["bg"] = ("#202A44")
passenger1_lastname_textbox["fg"] = ("darkorange")
passenger1_lastname_textbox.place(x=350,y=100)

gender_list = ["Male","Female"]
gender_1.set("")
pass1_gender_dropdown = OptionMenu(frame4,gender_1,*gender_list)  
pass1_gender_dropdown["fg"]=("darkorange")
pass1_gender_dropdown["activeforeground"]=("darkorange")
pass1_gender_dropdown["bg"]=("#202A44")
pass1_gender_dropdown["activebackground"]=("#202A44")  
pass1_gender_dropdown["bd"] = 0
pass1_gender_dropdown.place(x=440,y=150)

gender1_label = Label(frame4,text="Gender",fg="darkorange",bg="#202A44")
gender1_label.place(x=440,y=180)


pass1_DOB_dropdown = Spinbox(frame4,from_=1,to=30,width=5)  
pass1_DOB_dropdown["fg"]=("darkorange")
pass1_DOB_dropdown["bg"]=("#202A44")
pass1_DOB_dropdown["activebackground"]=("#202A44")  
pass1_DOB_dropdown["bd"] = 0
pass1_DOB_dropdown.place(x=80,y=150)

pass1_DOB_label = Label(frame4,text="DOB",fg="darkorange",bg="#202A44")
pass1_DOB_label.place(x=80,y=180)


pass1_MOB_dropdown = Spinbox(frame4,from_=1,to=12,width=5)  
pass1_MOB_dropdown["fg"]=("darkorange")
pass1_MOB_dropdown["bg"]=("#202A44")
pass1_MOB_dropdown["activebackground"]=("#202A44")  
pass1_MOB_dropdown["bd"] = 0
pass1_MOB_dropdown.place(x=200,y=150)

pass1_MOB_label = Label(frame4,text="Month",fg="darkorange",bg="#202A44")
pass1_MOB_label.place(x=200,y=180)

pass1_YOB_dropdown = Spinbox(frame4,from_=1920,to=2021,width=5)  
pass1_YOB_dropdown["fg"]=("darkorange")
pass1_YOB_dropdown["bg"]=("#202A44")
pass1_YOB_dropdown["activebackground"]=("#202A44")  
pass1_YOB_dropdown["bd"] = 0
pass1_YOB_dropdown.place(x=320,y=150)

pass1_YOB_label = Label(frame4,text="Year",fg="darkorange",bg="#202A44")
pass1_YOB_label.place(x=320,y=180)

passenger2_label = Label(frame4,text="Passenger 2",bg="#202A44",fg="darkorange")
passenger2_label.place(x=80,y=230)
passenger2_label["font"] = ("Arial",13)

first_name_2 = Label(frame4,text="FIRST NAME",fg="darkorange",bg="#202A44")
first_name_2.place(x=80,y=290)

last_name_2 = Label(frame4,text="LAST NAME",fg="darkorange",bg="#202A44")
last_name_2.place(x=350,y=290)

passenger2_firstname_textbox = Entry(frame4,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass2_firstname)
passenger2_firstname_textbox["bg"] = ("#202A44")
passenger2_firstname_textbox["fg"] = ("darkorange")
passenger2_firstname_textbox.place(x=80,y=270)

passenger2_lastname_textbox = Entry(frame4,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass2_lastname)
passenger2_lastname_textbox["bg"] = ("#202A44")
passenger2_lastname_textbox["fg"] = ("darkorange")
passenger2_lastname_textbox.place(x=350,y=270)

gender_list = ["Male","Female"]
gender_2.set("")
pass2_gender_dropdown = OptionMenu(frame4,gender_2,*gender_list)  
pass2_gender_dropdown["fg"]=("darkorange")
pass2_gender_dropdown["activeforeground"]=("darkorange")
pass2_gender_dropdown["bg"]=("#202A44")
pass2_gender_dropdown["activebackground"]=("#202A44")  
pass2_gender_dropdown["bd"] = 0
pass2_gender_dropdown.place(x=440,y=320)

gender2_label = Label(frame4,text="Gender",fg="darkorange",bg="#202A44")
gender2_label.place(x=440,y=350)


pass2_DOB_dropdown = Spinbox(frame4,from_=1,to=30,width=5)  
pass2_DOB_dropdown["fg"]=("darkorange")
pass2_DOB_dropdown["bg"]=("#202A44")
pass2_DOB_dropdown["activebackground"]=("#202A44")  
pass2_DOB_dropdown["bd"] = 0
pass2_DOB_dropdown.place(x=80,y=320)

pass2_DOB_label = Label(frame4,text="DOB",fg="darkorange",bg="#202A44")
pass2_DOB_label.place(x=80,y=350)


pass2_MOB_dropdown = Spinbox(frame4,from_=1,to=12,width=5)  
pass2_MOB_dropdown["fg"]=("darkorange")
pass2_MOB_dropdown["bg"]=("#202A44")
pass2_MOB_dropdown["activebackground"]=("#202A44")  
pass2_MOB_dropdown["bd"] = 0
pass2_MOB_dropdown.place(x=200,y=320)

pass2_MOB_label = Label(frame4,text="Month",fg="darkorange",bg="#202A44")
pass2_MOB_label.place(x=200,y=350)

pass2_YOB_dropdown = Spinbox(frame4,from_=1920,to=2021,width=5,bd=500)  
pass2_YOB_dropdown["fg"]=("darkorange")
pass2_YOB_dropdown["bg"]=("#202A44")
pass2_YOB_dropdown["activebackground"]=("#202A44")  
pass2_YOB_dropdown["bd"] = 0
pass2_YOB_dropdown.place(x=320,y=320)

pass2_YOB_label = Label(frame4,text="Year",fg="darkorange",bg="#202A44")
pass2_YOB_label.place(x=320,y=350)

add_pass3_button = Button(frame4,text="+ Add Passenger",bg="#202A44",fg="darkorange",activeforeground="darkorange",activebackground="#202A44")
add_pass3_button["command"] = third_passenger
add_pass3_button["font"] = ("Arial",10,"bold")
add_pass3_button.place(x=80,y=400)
add_pass3_button["bd"] = (0)

next_button_4= Button(frame4,text="Next",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
next_button_4["command"] = frame_4_next
next_button_4["font"] = ("Arial",13,"bold")
next_button_4.place(x=650,y=450)
next_button_4["bd"] = (0)

back_button_4 = Button(frame4,text="Back",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
back_button_4["command"] = lambda:show_frame(frame4)
back_button_4["font"] = ("Arial",13,"bold")
back_button_4.place(x=50,y=450)
back_button_4["bd"] = (0)






                                            #PASSENGER 3 FRAME:
passenger3_label = Label(passenger_3_frame,text="Passenger 3",bg="#202A44",fg="darkorange")
passenger3_label.place(x=80,y=60)
passenger3_label["font"] = ("Arial",13)

first_name_3 = Label(passenger_3_frame,text="FIRST NAME",fg="darkorange",bg="#202A44")
first_name_3.place(x=80,y=120)

last_name_3 = Label(passenger_3_frame,text="LAST NAME",fg="darkorange",bg="#202A44")
last_name_3.place(x=350,y=120)

passenger3_firstname_textbox = Entry(passenger_3_frame,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass3_firstname)
passenger3_firstname_textbox["bg"] = ("#202A44")
passenger3_firstname_textbox["fg"] = ("darkorange")
passenger3_firstname_textbox.place(x=80,y=100)

passenger3_lastname_textbox = Entry(passenger_3_frame,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass3_lastname)
passenger3_lastname_textbox["bg"] = ("#202A44")
passenger3_lastname_textbox["fg"] = ("darkorange")
passenger3_lastname_textbox.place(x=350,y=100)

gender_list = ["Male","Female"]
pass3_gender_dropdown = OptionMenu(passenger_3_frame,gender_3,*gender_list)  
pass3_gender_dropdown["fg"]=("darkorange")
pass3_gender_dropdown["activeforeground"]=("darkorange")
pass3_gender_dropdown["bg"]=("#202A44")
pass3_gender_dropdown["activebackground"]=("#202A44")  
pass3_gender_dropdown["bd"] = 0
pass3_gender_dropdown.place(x=440,y=150)

gender3_label = Label(passenger_3_frame,text="Gender",fg="darkorange",bg="#202A44")
gender3_label.place(x=440,y=180)


pass3_DOB_dropdown = Spinbox(passenger_3_frame,from_=1,to=30,width=5)  
pass3_DOB_dropdown["fg"]=("darkorange")
#pass3_DOB_dropdown["activeforeground"]=("darkorange")
pass3_DOB_dropdown["bg"]=("#202A44")
pass3_DOB_dropdown["activebackground"]=("#202A44")  
pass3_DOB_dropdown["bd"] = 0
pass3_DOB_dropdown.place(x=80,y=150)

pass3_DOB_label = Label(passenger_3_frame,text="DOB",fg="darkorange",bg="#202A44")
pass3_DOB_label.place(x=80,y=180)


pass3_MOB_dropdown = Spinbox(passenger_3_frame,from_=1,to=12,width=5)  
pass3_MOB_dropdown["fg"]=("darkorange")
#pass3_MOB_dropdown["activeforeground"]=("darkorange")
pass3_MOB_dropdown["bg"]=("#202A44")
pass3_MOB_dropdown["activebackground"]=("#202A44")  
pass3_MOB_dropdown["bd"] = 0
pass3_MOB_dropdown.place(x=200,y=150)

pass3_MOB_label = Label(passenger_3_frame,text="Month",fg="darkorange",bg="#202A44")
pass3_MOB_label.place(x=200,y=180)

pass3_YOB_dropdown = Spinbox(passenger_3_frame,from_=1920,to=2021,width=5)  
pass3_YOB_dropdown["fg"]=("darkorange")
#pass3_YOB_dropdown["activeforeground"]=("darkorange")
pass3_YOB_dropdown["bg"]=("#202A44")
pass3_YOB_dropdown["activebackground"]=("#202A44")  
pass3_YOB_dropdown["bd"] = 0
pass3_YOB_dropdown.place(x=320,y=150)

pass3_YOB_label = Label(passenger_3_frame,text="Year",fg="darkorange",bg="#202A44")
pass3_YOB_label.place(x=320,y=180)

num_adults = count0.get()
num_child = count1.get()
num_infant = count2.get()
total_pass = int(f"{int(num_adults)+int(num_child)+int(num_infant)}")

next_button3 = Button(passenger_3_frame,text="Next",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
next_button3["command"] = lambda:show_frame(frame5)
next_button3["font"] = ("Arial",13,"bold")
next_button3.place(x=650,y=450)
next_button3["bd"] = (0)


back_button3 = Button(passenger_3_frame,text="Back",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
back_button3["command"] = lambda:show_frame(frame4)
back_button3["font"] = ("Arial",13,"bold")
back_button3.place(x=50,y=450)
back_button3["bd"] = (0)

add_pass4_button = Button(passenger_3_frame,text="+ Add Passenger",fg="darkorange",bg="#202A44",activeforeground="darkorange",activebackground="#202A44")
add_pass4_button["command"] = fourth_passenger
add_pass4_button["font"] = ("Arial",10,"bold")
add_pass4_button.place(x=80,y=200)
add_pass4_button["bd"] = (0)








                                                    #PASSENGER 4 FRAME:
passenger3_label = Label(passenger_4_frame,text="Passenger 3",bg="#202A44",fg="darkorange")
passenger3_label.place(x=80,y=60)
passenger3_label["font"] = ("Arial",13)

first_name_3 = Label(passenger_4_frame,text="FIRST NAME",fg="darkorange",bg="#202A44")
first_name_3.place(x=80,y=120)

last_name_3 = Label(passenger_4_frame,text="LAST NAME",fg="darkorange",bg="#202A44")
last_name_3.place(x=350,y=120)

passenger3_firstname_textbox = Entry(passenger_4_frame,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass3_firstname)
passenger3_firstname_textbox["bg"] = ("#202A44")
passenger3_firstname_textbox["fg"] = ("darkorange")
passenger3_firstname_textbox.place(x=80,y=100)

passenger3_lastname_textbox = Entry(passenger_4_frame,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass3_lastname)
passenger3_lastname_textbox["bg"] = ("#202A44")
passenger3_lastname_textbox["fg"] = ("darkorange")
passenger3_lastname_textbox.place(x=350,y=100)

gender_list = ["Male","Female"]
pass3_gender_dropdown = OptionMenu(passenger_4_frame,gender_1,*gender_list)  
pass3_gender_dropdown["fg"]=("darkorange")
pass3_gender_dropdown["activeforeground"]=("darkorange")
pass3_gender_dropdown["bg"]=("#202A44")
pass3_gender_dropdown["activebackground"]=("#202A44")  
pass3_gender_dropdown["bd"] = 0
pass3_gender_dropdown.place(x=440,y=150)

gender3_label = Label(passenger_4_frame,text="Gender",fg="darkorange",bg="#202A44")
gender3_label.place(x=440,y=180)


pass3_DOB_dropdown = Spinbox(passenger_4_frame,from_=1,to=30,width=5)  
pass3_DOB_dropdown["fg"]=("darkorange")
#pass3_DOB_dropdown["activeforeground"]=("darkorange")
pass3_DOB_dropdown["bg"]=("#202A44")
pass3_DOB_dropdown["activebackground"]=("#202A44")  
pass3_DOB_dropdown["bd"] = 0
pass3_DOB_dropdown.place(x=80,y=150)

pass3_DOB_label = Label(passenger_4_frame,text="DOB",fg="darkorange",bg="#202A44")
pass3_DOB_label.place(x=80,y=180)


pass3_MOB_dropdown = Spinbox(passenger_4_frame,from_=1,to=12,width=5)  
pass3_MOB_dropdown["fg"]=("darkorange")
#pass3_MOB_dropdown["activeforeground"]=("darkorange")
pass3_MOB_dropdown["bg"]=("#202A44")
pass3_MOB_dropdown["activebackground"]=("#202A44")  
pass3_MOB_dropdown["bd"] = 0
pass3_MOB_dropdown.place(x=200,y=150)

pass3_MOB_label = Label(passenger_4_frame,text="Month",fg="darkorange",bg="#202A44")
pass3_MOB_label.place(x=200,y=180)

pass3_YOB_dropdown = Spinbox(passenger_4_frame,from_=1920,to=2021,width=5)  
pass3_YOB_dropdown["fg"]=("darkorange")
#pass3_YOB_dropdown["activeforeground"]=("darkorange")
pass3_YOB_dropdown["bg"]=("#202A44")
pass3_YOB_dropdown["activebackground"]=("#202A44")  
pass3_YOB_dropdown["bd"] = 0
pass3_YOB_dropdown.place(x=320,y=150)

pass3_YOB_label = Label(passenger_4_frame,text="Year",fg="darkorange",bg="#202A44")
pass3_YOB_label.place(x=320,y=180)

passenger4_label = Label(passenger_4_frame,text="Passenger 4",bg="#202A44",fg="darkorange")
passenger4_label.place(x=80,y=230)
passenger4_label["font"] = ("Arial",13)

first_name_4 = Label(passenger_4_frame,text="FIRST NAME",fg="darkorange",bg="#202A44")
first_name_4.place(x=80,y=290)

last_name_4 = Label(passenger_4_frame,text="LAST NAME",fg="darkorange",bg="#202A44")
last_name_4.place(x=350,y=290)

passenger4_firstname_textbox = Entry(passenger_4_frame,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass4_firstname)
passenger4_firstname_textbox["bg"] = ("#202A44")
passenger4_firstname_textbox["fg"] = ("darkorange")
passenger4_firstname_textbox.place(x=80,y=270)

passenger4_lastname_textbox = Entry(passenger_4_frame,width=30,highlightthickness=1,bd=0,highlightbackground="darkorange",textvariable=pass4_lastname)
passenger4_lastname_textbox["bg"] = ("#202A44")
passenger4_lastname_textbox["fg"] = ("darkorange")
passenger4_lastname_textbox.place(x=350,y=270)

gender_list = ["Male","Female"]
pass4_gender_dropdown = OptionMenu(passenger_4_frame,gender_4,*gender_list)  
pass4_gender_dropdown["fg"]=("darkorange")
pass4_gender_dropdown["activeforeground"]=("darkorange")
pass4_gender_dropdown["bg"]=("#202A44")
pass4_gender_dropdown["activebackground"]=("#202A44")  
pass4_gender_dropdown["bd"] = 0
pass4_gender_dropdown.place(x=440,y=320)

gender4_label = Label(passenger_4_frame,text="Gender",fg="darkorange",bg="#202A44")
gender4_label.place(x=440,y=350)


pass4_DOB_dropdown = Spinbox(passenger_4_frame,from_=1,to=30,width=5)  
pass4_DOB_dropdown["fg"]=("darkorange")
pass4_DOB_dropdown["bg"]=("#202A44")
pass4_DOB_dropdown["activebackground"]=("#202A44")  
pass4_DOB_dropdown["bd"] = 0
pass4_DOB_dropdown.place(x=80,y=320)

pass4_DOB_label = Label(passenger_4_frame,text="DOB",fg="darkorange",bg="#202A44")
pass4_DOB_label.place(x=80,y=350)

pass4_MOB_dropdown = Spinbox(passenger_4_frame,from_=1,to=12,width=5)  
pass4_MOB_dropdown["fg"]=("darkorange")
pass4_MOB_dropdown["bg"]=("#202A44")
pass4_MOB_dropdown["activebackground"]=("#202A44")  
pass4_MOB_dropdown["bd"] = 0
pass4_MOB_dropdown.place(x=200,y=320)

pass4_MOB_label = Label(passenger_4_frame,text="Month",fg="darkorange",bg="#202A44")
pass4_MOB_label.place(x=200,y=350)

yob_4 = IntVar()
pass4_YOB_dropdown = Spinbox(passenger_4_frame,from_=1920,to=2021,width=5,bd=500)  
pass4_YOB_dropdown["fg"]=("darkorange")
pass4_YOB_dropdown["bg"]=("#202A44")
pass4_YOB_dropdown["activebackground"]=("#202A44")  
pass4_YOB_dropdown["bd"] = 0
pass4_YOB_dropdown.place(x=320,y=320)

pass4_YOB_label = Label(passenger_4_frame,text="Year",fg="darkorange",bg="#202A44")
pass4_YOB_label.place(x=320,y=350)

next_button4 = Button(passenger_4_frame,text="Next",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
next_button4["command"] = lambda:show_frame(frame5)
next_button4["font"] = ("Arial",13,"bold")
next_button4.place(x=650,y=450)
next_button4["bd"] = (0)

back_button_pass4 = Button(passenger_4_frame,text="Back",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
back_button_pass4["command"] = lambda:show_frame(frame4)
back_button_pass4["font"] = ("Arial",13,"bold")
back_button_pass4.place(x=50,y=450)
back_button_pass4["bd"] = (0)



                                                                #FRAME 5:

select_seat_label = Label(frame5,text="Select Seats",bg="#202A44",fg="darkorange")
select_seat_label["font"] = ("Consolas",25,"bold")
select_seat_label.place(x=80,y=20)

s1 = Button(frame5,bg="white",fg="#202A44",text="1A",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s1["font"] = ("Consolas",9,"bold")
s1["command"] = lambda:select_seat("1A")
s1.place(x=100,y=100)

s2 = Button(frame5,bg="white",fg="#202A44",text="1B",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s2["font"] = ("Consolas",9,"bold")
s2["command"] = lambda:select_seat("1B")
s2.place(x=150,y=100)

s3 = Button(frame5,bg="white",fg="#202A44",text="2A",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s3["font"] = ("Consolas",9,"bold")
s3["command"] = lambda:select_seat("2A")
s3.place(x=100,y=150)

s4 = Button(frame5,bg="white",fg="#202A44",text="2B",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s4["font"] = ("Consolas",9,"bold")
s4["command"] = lambda:select_seat("2B")
s4.place(x=150,y=150)

s5 = Button(frame5,bg="white",fg="#202A44",text="3A",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s5["font"] = ("Consolas",9,"bold")
s5["command"] = lambda:select_seat("3A")
s5.place(x=100,y=200)

s6 = Button(frame5,bg="white",fg="#202A44",text="3B",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s6["font"] = ("Consolas",9,"bold")
s6["command"] = lambda:select_seat("3B")
s6.place(x=150,y=200)

s7 = Button(frame5,bg="white",fg="#202A44",text="4A",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s7["font"] = ("Consolas",9,"bold")
s7["command"] = lambda:select_seat("4A")
s7.place(x=100,y=250)

s8 = Button(frame5,bg="white",fg="#202A44",text="4B",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s8["font"] = ("Consolas",9,"bold")
s8["command"] = lambda:select_seat("4B")
s8.place(x=150,y=250)

s9 = Button(frame5,bg="white",fg="#202A44",text="5A",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s9["font"] = ("Consolas",9,"bold")
s9["command"] = lambda:select_seat("5A")
s9.place(x=100,y=300)

s10 = Button(frame5,bg="white",fg="#202A44",text="5B",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s10["font"] = ("Consolas",9,"bold")
s10["command"] = lambda:select_seat("5B")
s10.place(x=150,y=300)

s11 = Button(frame5,bg="white",fg="#202A44",text="1C",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s11["font"] = ("Consolas",9,"bold")
s11["command"] = lambda:select_seat("1C")
s11.place(x=250,y=100)

s12 = Button(frame5,bg="white",fg="#202A44",text="1D",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s12["font"] = ("Consolas",9,"bold")
s12["command"] = lambda:select_seat("1D")
s12.place(x=300,y=100)

s13 = Button(frame5,bg="white",fg="#202A44",text="2C",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s13["font"] = ("Consolas",9,"bold")
s13["command"] = lambda:select_seat("2C")
s13.place(x=250,y=150)

s14 = Button(frame5,bg="white",fg="#202A44",text="2D",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s14["font"] = ("Consolas",9,"bold")
s14["command"] = lambda:select_seat("2D")
s14.place(x=300,y=150)

s15 = Button(frame5,bg="white",fg="#202A44",text="3C",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s15["font"] = ("Consolas",9,"bold")
s15["command"] = lambda:select_seat("3C")
s15.place(x=250,y=200)

s16 = Button(frame5,bg="white",fg="#202A44",text="3D",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s16["font"] = ("Consolas",9,"bold")
s16["command"] = lambda:select_seat("3D")
s16.place(x=300,y=200)

s17 = Button(frame5,bg="white",fg="#202A44",text="4C",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s17["font"] = ("Consolas",9,"bold")
s17["command"] = lambda:select_seat("4C")
s17.place(x=250,y=250)

s18 = Button(frame5,bg="white",fg="#202A44",text="4D",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s18["font"] = ("Consolas",9,"bold")
s18["command"] = lambda:select_seat("4D")
s18.place(x=300,y=250)

s19 = Button(frame5,bg="white",fg="#202A44",text="5C",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s19["font"] = ("Consolas",9,"bold")
s19["command"] = lambda:select_seat("5C")
s19.place(x=250,y=300)

s20 = Button(frame5,bg="white",fg="#202A44",text="5D",padx=10,pady=10,bd=0,activebackground="white",activeforeground="#202A44")
s20["font"] = ("Consolas",9,"bold")
s20["command"] = lambda:select_seat("5D")
s20.place(x=300,y=300)

snacks_label = Label(frame5,fg="darkorange",bg="#202A44",text="Would you like to pre-order some snacks or beverages?")
snacks_label["font"] = ("Consolas",10,"bold")
snacks_label.place(x=30,y=400)

yes_button = Button(frame5,text="Yes",fg="darkorange",bg="#202A44",activeforeground="darkorange",activebackground="#202A44",bd=0)
yes_button["font"] = ("Consolas",10,"bold")
yes_button["command"] = seat_yes
yes_button.place(x=300,y=450)

no_button = Button(frame5,text="No",fg="darkorange",bg="#202A44",activeforeground="darkorange",activebackground="#202A44",bd=0)
no_button["font"] = ("Consolas",10,"bold")
no_button["command"] = seat_no
no_button.place(x=350,y=450)                 

clear_button = Button(frame5,text="Clear all selections",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44",bd=0)
clear_button["font"] = ("Consolas",11,"bold")
clear_button["command"] = clear_seat
clear_button.place(x=500,y=360)

back_button_seat = Button(frame5,text="Back",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
back_button_seat["command"] = lambda:show_frame(frame3)
back_button_seat["font"] = ("Arial",13,"bold")
back_button_seat.place(x=50,y=450)
back_button_seat["bd"] = (0)




                                                                #SNACKS:        
chicken_sandwhich_label = Label(snack,text = "Chicken Sandwhich",bg="#202A44",fg="darkorange",font=20)
chicken_sandwhich_label.place(x=50,y=70)

chicken_sandwhich_price_label = Label(snack,text="₹250",bg="#202A44",fg="darkorange",font=10)
chicken_sandwhich_price_label.place(x=200,y=70)

chicken_sandwhich_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=chicken_sandwhich_num)
chicken_sandwhich_spinbox.place(x=300,y=70)

veg_sandwhich_label = Label(snack,text="Veg Sandwhich",bg="#202A44",fg="darkorange",font=20)
veg_sandwhich_label.place(x=50,y=125)

veg_sandwhich_price_label = Label(snack,text="₹150",bg="#202A44",fg="darkorange",font=10)
veg_sandwhich_price_label.place(x=200,y=125)

Veg_sandwhich_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=veg_sandwhich_num)
Veg_sandwhich_spinbox.place(x=300,y=125)

veg_biryani_label = Label(snack,text="Veg Biryani",bg="#202A44",fg="darkorange",font=20)
veg_biryani_label.place(x=50,y=180)

veg_biryani_price_label = Label(snack,text="₹350",bg="#202A44",fg="darkorange",font=10)
veg_biryani_price_label.place(x=200,y=180)

veg_biryani_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=veg_biryani_num)
veg_biryani_spinbox.place(x=300,y=180)

chicken_biryani_label = Label(snack,text="Chicken Biryani",bg="#202A44",fg="darkorange",font=20)
chicken_biryani_label.place(x=50,y=235)

chicken_biryani_price_label = Label(snack,text="₹390",bg="#202A44",fg="darkorange",font=10)
chicken_biryani_price_label.place(x=200,y=235)

chicken_biryani_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=chicken_biryani_num)
chicken_biryani_spinbox.place(x=300,y=235)

cup_noodles_label = Label(snack,text="Cup Noodles",bg="#202A44",fg="darkorange",font=20)
cup_noodles_label.place(x=50,y=290)

cup_noodles_price_label = Label(snack,text="₹250",bg="#202A44",fg="darkorange",font=10)
cup_noodles_price_label.place(x=200,y=290)

cup_noodles_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=cup_noodles_num)
cup_noodles_spinbox.place(x=300,y=290)

cookie_label = Label(snack,text="Cookies",bg="#202A44",fg="darkorange",font=20)
cookie_label.place(x=50,y=345)

cookie_price_label = Label(snack,text="₹70",bg="#202A44",fg="darkorange",font=10)
cookie_price_label.place(x=200,y=345)

cookie_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=cookie_num)
cookie_spinbox.place(x=300,y=345)

fries_label = Label(snack,text="French Fries",bg="#202A44",fg="darkorange",font=20)
fries_label.place(x=50,y=400)

fries_price_label = Label(snack,text="₹200",bg="#202A44",fg="darkorange",font=10)
fries_price_label.place(x=200,y=400)

fries_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=fries_num)
fries_spinbox.place(x=300,y=400)

coca_cola_label = Label(snack,text="Coca Cola",bg="#202A44",fg="darkorange",font=20)
coca_cola_label.place(x=400,y=70)

coca_cola_price_label = Label(snack,text="₹95",bg="#202A44",fg="darkorange",font=10)
coca_cola_price_label.place(x=550,y=70)

coca_cola_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=coca_cola_num)
coca_cola_spinbox.place(x=650,y=70)

pepsi_label = Label(snack,text="Pepsi",bg="#202A44",fg="darkorange",font=20)
pepsi_label.place(x=400,y=125)

pepsi_price_label = Label(snack,text="₹95",bg="#202A44",fg="darkorange",font=10)
pepsi_price_label.place(x=550,y=125)

pepsi_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=pepsi_num)
pepsi_spinbox.place(x=650,y=125)

sprite_label = Label(snack,text="Sprite",bg="#202A44",fg="darkorange",font=20)
sprite_label.place(x=400,y=180)

sprite_price_label = Label(snack,text="₹95",bg="#202A44",fg="darkorange",font=10)
sprite_price_label.place(x=550,y=180)

sprite_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=sprite_num)
sprite_spinbox.place(x=650,y=180)


tea_label = Label(snack,text="Tea",bg="#202A44",fg="darkorange",font=20)
tea_label.place(x=400,y=235)

tea_price_label = Label(snack,text="₹100",bg="#202A44",fg="darkorange",font=10)
tea_price_label.place(x=550,y=235)

tea_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=tea_num)
tea_spinbox.place(x=650,y=235)


coffee_label = Label(snack,text="Coffee",bg="#202A44",fg="darkorange",font=20)
coffee_label.place(x=400,y=290)

coffee_price_label = Label(snack,text="₹120",bg="#202A44",fg="darkorange",font=10)
coffee_price_label.place(x=550,y=290)

coffee_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=coffee_num)
coffee_spinbox.place(x=650,y=290)

mango_label = Label(snack,text="Mango Smoothie",bg="#202A44",fg="darkorange",font=20)
mango_label.place(x=400,y=345)

mango_price_label = Label(snack,text="₹150",bg="#202A44",fg="darkorange",font=10)
mango_price_label.place(x=550,y=345)

mango_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=mango_num)
mango_spinbox.place(x=650,y=345)

water_label = Label(snack,text="Mineral Water",bg="#202A44",fg="darkorange",font=20)
water_label.place(x=400,y=400)

water_price_label = Label(snack,text="₹50",bg="#202A44",fg="darkorange",font=10)
water_price_label.place(x=550,y=400)

water_spinbox = Spinbox(snack,bg="#202A44",fg="darkorange",from_=0,to=10,width=4,textvariable=water_num)
water_spinbox.place(x=650,y=400)

next_button = Button(snack,text="Next",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
next_button["command"] = food_bill
next_button["font"] = ("Consolas",13,"bold")
next_button.place(x=630,y=450)
next_button["bd"] = (0)

#show  Food bill button
back_button5 = Button(snack,text="Back",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
back_button5["command"] = lambda:show_frame(frame5)
back_button5["font"] = ("Consolas",13,"bold")
back_button5.place(x=50,y=450)
back_button5["bd"] = (0)



                                                                #FRAME 6:

bill_label = Label(frame6,text="Bill",fg="darkorange", bg="#202A44", font=['Consolas', 30, 'bold'])
bill_label.place(x=300,y=10)

#Label to Display item names
l_bill_name=Label(frame6,anchor="w",textvariable=var_item_name,fg="darkorange", bg="#202A44", font=['Consolas', 14, 'bold'])
l_bill_name.place(x=75,y=150)

#Label to Display item quantity
l_bill_qty=Label(frame6,anchor="w",textvariable=var_item_quantity,fg="darkorange",bg="#202A44",font=['Consolas',14,"bold"])
l_bill_qty.place(x=320,y=150)

#Label to Display item amount
l_bill_amt=Label(frame6,anchor="w",textvariable=var_item_amt,fg="darkorange", bg="#202A44", font=['Consolas', 14, 'bold'])
l_bill_amt.place(x=520,y=150)

#Label to Display Total Amount without GST
l_amt_wo_gst=Label(frame6,anchor="w",textvariable=var_total_amt_wo_gst,fg="darkorange", bg="#202A44", font=['Consolas', 14, 'bold'])
l_amt_wo_gst.place(x=100,y=310)

#Label to show GST Amount
l_gst_amt=Label(frame6,anchor="w",textvariable=var_gst_amt,fg="darkorange", bg="#202A44", font=['Consolas', 14, 'bold'])
l_gst_amt.place(x=100,y=340)

#Label to show Total Amount with GST
l_amt_w_gst=Label(frame6,anchor="w",textvariable=var_total_amt_w_gst,fg="darkorange", bg="#202A44", font=['Consolas', 14, 'bold'])
l_amt_w_gst.place(x=100,y=370)

back_button_bill = Button(frame6,text="Back",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
back_button_bill["command"] = lambda:show_frame(snack)
back_button_bill["font"] = ("Consolas",13,"bold")
back_button_bill.place(x=50,y=450)
back_button_bill["bd"] = (0)

next_button_bill = Button(frame6,text="Show Ticket",bg="darkorange",fg="#202A44",activebackground="darkorange",activeforeground="#202A44")
next_button_bill["command"] = open_window
next_button_bill["font"] = ("Consolas",13,"bold")
next_button_bill.place(x=580,y=450)
next_button_bill["bd"] = (0)


show_frame(frame1)

root.mainloop()