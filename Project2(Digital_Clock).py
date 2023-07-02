from tkinter import *     
import time             
  
def display_time():    
    hr = str(time.strftime("%H"))  
    mint = str(time.strftime("%M"))  
    sec = str(time.strftime("%S"))  
  
    if int(hr) >= 12 & int(hr) < 24 & int(mint) >= 0:  
        meridiem_label.config(text = "PM")  
 
    else:  
        meridiem_label.config(text = "AM")  
  

    if int(hr) > 24:  
        hr = str((int(hr) - 24))  
      
    elif int(hr) == 0:  
        hr = str(24)  
  
  
    hr_label.config(text = hr)  
    mint_label.config(text = mint)  
    sec_label.config(text = sec)  
  
    hr_label.after(200, display_time)  
  
# main function  
if __name__ == "__main__":    
    root = Tk()    
    root.title("Digital Clock")    
    root.geometry("550x150")     
    root.config(bg = "black")   
   
    header_frame = Frame(root, bg = "green")  
    body_frame = Frame(root, bg = "black")  
    
    header_frame.pack(pady = 15)  
    body_frame.pack(padx=10)  
  
    header_label = Label(  
        header_frame,  
        text = "Digital Clock",  
        font = ("consolas", "20", "bold"),  
        bg = "green",  
        fg = "white"  
        )    
    header_label.pack()  
    
    hr_label = Label(  
        body_frame,  
        text = "00",  
        font = ("ROG FONTS", "48"),  
        bg = "#2C3C3F",  
        fg = "red"  
        )  
    colon_label_one = Label(  
        body_frame,  
        text = ":",  
        font = ("ROG FONTS", "48", "bold"),  
        bg = "#2C3C3F",  
        fg = "red"  
        )  
    mint_label = Label(  
        body_frame,  
        text = "00",  
        font = ("ROG FONTS", "48"),  
        bg = "#2C3C3F",  
        fg = "red"  
        )  
    colon_label_two = Label(  
        body_frame,  
        text = ":",  
        font = ("ROG FONTS", "48", "bold"),  
        bg = "#2C3C3F",  
        fg = "red"  
        )  
    sec_label = Label(  
        body_frame,  
        text = "00",  
        font = ("ROG FONTS", "48"),  
        bg = "#2C3C3F",  
        fg = "red"  
        )  
    meridiem_label = Label(  
        body_frame,  
        text = "AM",  
        font = ("ROG FONTS", "48"),  
        bg = "#2C3C3F",  
        fg = "red"  
        )  
       
    hr_label.grid(row = 4, column = 0, padx = 5, pady = 5)  
    colon_label_one.grid(row = 4, column = 1, padx = 5, pady = 5)  
    mint_label.grid(row = 4, column = 2, padx = 5, pady = 5)  
    colon_label_two.grid(row = 4, column = 3, padx = 5, pady = 5)  
    sec_label.grid(row = 4, column = 4, padx = 5, pady = 5)  
    meridiem_label.grid(row = 4, column = 5, padx = 5, pady = 5)    
  
    display_time()  
    root.mainloop()  
