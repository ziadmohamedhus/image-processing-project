import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
import sv_ttk
  
import dm_0
import DM_1


import F1_Ideal_Low_Pass_Filter  
import F2_ideal_high_pass_filter  
import F3_butterworth_low_pass   
import F4_butterworth_high_pass
import F5_gaussian_low_pass 
import F6_gaussian_high_pass


import P1_add
import P2_sub
import P3_britgness
import P4_contrast  
import P5_power_law        
import P6_quantization   
import P7_negative   
import P8_histo   
import P9_histogram_equalization   
import P10_avg 
import P11_hist_matched


import N1_average
import N2_median
import N3_edge_detection
import N4_sharpinnig
import N5_unsharp
import N6_weghite
import N7_max_smoothing
import N8_min_smoothing



   





root = tk.Tk()
root.title("    فلترني  شكراً  ")
# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

my_canvas=tk.Canvas(root,scrollregion=(0,0,2000,5000))

my_canvas.pack(expand=True,fill="both")





#my_canvas.bind('<Configure>',lambda event:my_canvas.yview_scroll(int(event.delta /60),"units"))
#my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
root_fram=tk.Frame(my_canvas)
my_canvas.create_window((0,0),window=root_fram,anchor="nw")
my_scroll=tk.Scrollbar(my_canvas,orient="vertical",command=my_canvas.yview,)
my_scroll.pack(side="right",fill="both")
my_canvas.configure(yscrollcommand=my_scroll.set)
###########################  DIRECT MAPING #######################################

Geometry_fram = ttk.LabelFrame(root_fram, text="GEOMETRY OPERATION")
Geometry_fram.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

DM_list=[1,2,3,4,5,6,7,8]
DM_value=tk.StringVar()

DM=tk.StringVar()
DM.set(None)
d1=1
d2=2

def DM_submet():
    s=int(DM.get())
    x=int(DM_value.get())
    if(s==1):
        dm_0.DM0(filename,x)
    elif(s==2):
        DM_1.DM1(filename,x)
        

# Create a Frame for the Direct maping
Direct_frame = ttk.LabelFrame(Geometry_fram, text="DIRECT MAPING", padding=(20, 10))
Direct_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
# input
Direct_input = ttk.Combobox(Direct_frame, state="readonly", values=DM_list , textvariable=DM_value)
Direct_input.current(0)
Direct_input.grid(row=0, column=0, padx=5, pady=10,  sticky="ew")
# Checkbuttons
Direct_check_1 = ttk.Checkbutton(Direct_frame, text="0 Order", variable=DM,onvalue=1,offvalue=0)
Direct_check_1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
Direct_check_2 = ttk.Checkbutton(Direct_frame, text="1 Order", variable=DM,onvalue=2,offvalue=0)
Direct_check_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
# Submet
Direct_submet = ttk.Button(Direct_frame, text="submet",command=DM_submet)
Direct_submet.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
###########################  REVERS MAPING #######################################

RM_list=[1,2,3,4,5,6,7,8]
RM_value1=tk.StringVar()
RM_value2=tk.StringVar()

RM=tk.StringVar()
RM.set(None)
r1=1
r2=2
def RM_submet():
    s=int(RM.get())
    x=int(RM_value1.get())
    if (s==1):
        dm_0.DM0(filename,x)
    elif(s==2):
        DM_1.DM1(filename,x)


# Create a Frame for the Revers maping
Revers_frame = ttk.LabelFrame(Geometry_fram, text="REVERS MAPING", padding=(20, 10))
Revers_frame.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
# input
Revers_input1 = ttk.Combobox(Revers_frame, state="readonly", values=RM_list , textvariable=RM_value1)
Revers_input1.current(0)
Revers_input1.grid(row=0, column=0, padx=5, pady=10,  sticky="ew")
Revers_input2 = ttk.Combobox(Revers_frame, state="readonly", values=RM_list , textvariable=RM_value2)
Revers_input2.current(0)
Revers_input2.grid(row=1, column=0, padx=5, pady=10,  sticky="ew")
# Checkbuttons
Revers_check_1 = ttk.Checkbutton(Revers_frame, text="0 Order", variable=RM,onvalue=1,offvalue=0)
Revers_check_1.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
Revers_check_2 = ttk.Checkbutton(Revers_frame, text="1 Order", variable=RM,onvalue=2,offvalue=0)
Revers_check_2.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
# Submet
Revers_submet = ttk.Button(Revers_frame, text="submet",command=RM_submet)
Revers_submet.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

###########################  HISTGRAM-QUANTIZATION  ################################################

pixel_fram = ttk.LabelFrame(root_fram, text="PIXEL OPERATION")
pixel_fram.grid(row=2, column=0, padx=(20, 20), pady=(20, 10), sticky="nsew")



#HISTOGRAM
def  histo_fun():
    P8_histo.P8(filename)
h = ttk.Button(pixel_fram, text="HISTOGRAM",command=histo_fun)
h.grid(row=0, column=0, padx=5, pady=10,  sticky="nsew")
#EQUALIZATION
def  equalization_fun():
    P9_histogram_equalization.P9(filename)
e = ttk.Button(pixel_fram, text="HISTOGRAM EQUALIZATION",command=equalization_fun)
e.grid(row=1, column=0, padx=5, pady=10,  sticky="nsew")

#GRAY
def gray_fun():
    P10_avg.P10(filename)
n = ttk.Button(pixel_fram, text="GRAY",command=gray_fun)
n.grid(row=2, column=0, padx=5, pady=10,  sticky="nsew")


#NEGATEV
def negateve_fun():
    P7_negative.P7(filename)
g = ttk.Button(pixel_fram, text="NEGATEV",command=negateve_fun)
g.grid(row=3, column=0, padx=5, pady=10,  sticky="nsew")

#Quantizatio
def Quantizatio_fun():
    P6_quantization.P6(filename)
g = ttk.Button(pixel_fram, text="QUANTIZATION",command=Quantizatio_fun)
g.grid(row=4, column=0, padx=5, pady=10,  sticky="nsew")
###########################  GRAY-NEGATEV-CONTRUST-POWER-ADD #######################################

# Create a Frame for input widgets
widgets_frame_1 = ttk.Frame(root_fram, padding=(0, 0, 0, 10))
widgets_frame_1.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame_1.columnconfigure(index=0, weight=1)

temp_widgit = ttk.Frame(widgets_frame_1, padding=(0, 0, 0, 10))
temp_widgit.grid(row=0, column=0,sticky="nsew", rowspan=3)

# TAKE IMAGE
def upload_img():
    global filename,img
    file_type=[('Png files','*.png'),('Jpg files','*.jpg'),('Jpeg files','*.jpeg')]
    filename=filedialog.askopenfilename(filetypes=file_type)
    img=Image.open(filename)
    print(filename)
    img=img.resize((350,350))
    img= ImageTk.PhotoImage(img)
    upload_img_label=ttk.Label(widgets_frame_1, image=img,width=300)
    upload_img_label.grid(row=5, column=0 , padx=5, pady=10, sticky="nsew")


Gray = ttk.Button(temp_widgit, text="READ IMAGE",command=upload_img)
Gray.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
# MOOD
def toggle_theme():
    if sv_ttk.get_theme() == "dark":
        print("Setting theme to light")
        sv_ttk.use_light_theme()
    elif sv_ttk.get_theme() == "light":
        print("Setting theme to dark")
        sv_ttk.use_dark_theme()
    else:
        print("Not Sun Valley theme")


Negatev = ttk.Button(temp_widgit, text="MOOD",command=toggle_theme)
Negatev.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
# Separator
separator = ttk.Separator(widgets_frame_1)
separator.grid(row=4, column=0, padx=(20, 10), pady=10, sticky="ew")
# CONTRUST
Contrust_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]
Contrust_value1=tk.StringVar()
Contrust_value2=tk.StringVar()
      # input
Contrust_input1 = ttk.Combobox(temp_widgit, state="readonly", values=Contrust_list , textvariable=Contrust_value1)
Contrust_input1.current(0)
Contrust_input1.grid(row=2, column=0, padx=5, pady=10,  sticky="ew")
Contrust_input2 = ttk.Combobox(temp_widgit, state="readonly", values=Contrust_list , textvariable=Contrust_value2)
Contrust_input2.current(0)
Contrust_input2.grid(row=2, column=1, padx=5, pady=10,  sticky="ew")
      #submet
def contrust_fun():
    x=int(Contrust_value1.get())
    y=int(Contrust_value2.get())
    P4_contrast.P4(filename,y,x)
    
Contrust = ttk.Button(widgets_frame_1, text="CONTRUST",command=contrust_fun)
Contrust.grid(row=3, column=0, padx=5,  sticky="nsew")
#ملهاش لازمة اطار بس !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

k = ttk.Button(widgets_frame_1, text="this is image",)
k.grid(row=5, column=0, padx=5,  sticky="nsew")

# Separator
separator = ttk.Separator(widgets_frame_1)
separator.grid(row=6, column=0, padx=(20, 10), pady=10, sticky="ew")

#POWER-DARK-BRIGHT
      # Create a Frame for the Radiobuttons
Darkness_frame = ttk.LabelFrame(widgets_frame_1, text="Darkness&Brightness", padding=(20, 10))
Darkness_frame.grid(row=19, column=0, padx=(20, 10), pady=10, sticky="nsew")

Darkness_list=[0.1 ,0.2 ,0.3 , 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]
Darkness_value1=tk.StringVar()

Darkness_input1 = ttk.Combobox(Darkness_frame, state="readonly", values=Darkness_list , textvariable=Darkness_value1)
Darkness_input1.current(0)
Darkness_input1.grid(row=0, column=0, padx=5, pady=10,  sticky="ew")

Darkness_selection=tk.StringVar()
Darkness_selection.set(None)

      # Radiobuttons
radio_1 = ttk.Radiobutton(Darkness_frame, text="DARKNESS",variable=Darkness_selection , value=1)
radio_1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_2 = ttk.Radiobutton(Darkness_frame, text="BRIGHTNESS",variable=Darkness_selection,  value=2)
radio_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(Darkness_frame, text="POWER LOW",variable=Darkness_selection,  value=3)
radio_3.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

def print_Darkness():
    x=int(Darkness_selection.get())
    y=float(Darkness_value1.get())
    if(x==1):
        y=y*-1
        P3_britgness.P3(filename,y)
    elif(x==2):
        P3_britgness.P3(filename,y)
    elif(x==3):
        P5_power_law.P5(filename,y)
    
but_r = ttk.Button(Darkness_frame, text="submet",command=print_Darkness)
but_r.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")




###########################  LOW PASS-HIGH PASS #######################################

widgets_main = ttk.Frame(root_fram, )
widgets_main.grid(row=0, column=2, padx=3, pady=5, sticky="nsew", rowspan=3)
widgets_main.columnconfigure(index=0, weight=1)


FREQUENCY_fram = ttk.LabelFrame(widgets_main, text="FREQUENCY OPERATION")
FREQUENCY_fram.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")


# Create a Frame for input widgets
widgets_frame_2 = ttk.Frame(FREQUENCY_fram, )
widgets_frame_2.grid(row=0, column=0, padx=3, pady=5, sticky="nsew", rowspan=3)
widgets_frame_2.columnconfigure(index=0, weight=1)
#LOW PASS
      # Create a Frame for the Radiobuttons
LOW_frame = ttk.LabelFrame(widgets_frame_2, text="LOW PASS", padding=(20, 10))
LOW_frame.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="nsew")

LOW_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]
LOW_value1=tk.StringVar()

LOW_input1 = ttk.Combobox(LOW_frame, state="readonly", values=LOW_list , textvariable=LOW_value1)
LOW_input1.current(0)
LOW_input1.grid(row=0, column=0, padx=5, pady=10,  sticky="ew")

LOW_selection=tk.StringVar()
LOW_selection.set(None)

      # Radiobuttons
LOW_radio_1 = ttk.Radiobutton(LOW_frame, text="IDEAL",variable=LOW_selection , value=1)
LOW_radio_1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
LOW_radio_2 = ttk.Radiobutton(LOW_frame, text="GAUSSIAN",variable=LOW_selection,  value=2)
LOW_radio_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
LOW_radio_3 = ttk.Radiobutton(LOW_frame, text="BUTTERWORTH",variable=LOW_selection,  value=3)
LOW_radio_3.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

def print_LOW():
    s=int(LOW_selection.get())
    x1=int(LOW_value1.get())
    if(s==1):
        F1_Ideal_Low_Pass_Filter.F1(filename,x1)
    elif(s==2):
        F5_gaussian_low_pass.F5(filename,x1)
    elif(s==3):
        F3_butterworth_low_pass.F3(filename,x1)
    
low_but_r = ttk.Button(LOW_frame, text="submet",command=print_LOW)
low_but_r.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")
#HIGH PASS
      # Create a Frame for the Radiobuttons
High_frame = ttk.LabelFrame(widgets_frame_2, text="HIGH PASS", padding=(20, 10))
High_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

High_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]
High_value1=tk.StringVar()

High_input1 = ttk.Combobox(High_frame, state="readonly", values=High_list , textvariable=High_value1)
High_input1.current(0)
High_input1.grid(row=0, column=0, padx=5, pady=10,  sticky="ew")

High_selection=tk.StringVar()
High_selection.set(None)

      # Radiobuttons
High_radio_1 = ttk.Radiobutton(High_frame, text="IDEAL",variable=High_selection , value=1)
High_radio_1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
High_radio_2 = ttk.Radiobutton(High_frame, text="GAUSSIAN",variable=High_selection,  value=2)
High_radio_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
High_radio_3 = ttk.Radiobutton(High_frame, text="BUTTERWORTH",variable=High_selection,  value=3)
High_radio_3.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

def print_HIGH():
    s=int(High_selection.get())
    x1=int(High_value1.get())
    if(s==1):
        F2_ideal_high_pass_filter.F2(filename,x1)
    elif(s==2):
        F6_gaussian_high_pass.F6(filename,x1)
    elif(s==3):
        F4_butterworth_high_pass.F4(filename,x1)
    
high_but_r = ttk.Button(High_frame, text="submet",command=print_HIGH)
high_but_r.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

########################################### ADD-SUB ############################

ADD_frame = ttk.LabelFrame(widgets_main, text="ADD&SUB", padding=(20, 10))
ADD_frame.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="nsew")


# TAKE IMAGE 2
def upload_img2():
    global filename_2,img_2
    file_type=[('Png files','*.png'),('Jpg files','*.jpg'),('Jpeg files','*.jpeg')]
    filename_2=filedialog.askopenfilename(filetypes=file_type)
    img_2=Image.open(filename_2)
    print(filename_2)
    img_2=img_2.resize((350,350))
    img_2= ImageTk.PhotoImage(img_2)
    


image_2 = ttk.Button(ADD_frame, text="IMAGE 2",command=upload_img2)
image_2.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")


ADD_selection=tk.StringVar()
ADD_selection.set(None)

      # Radiobuttons
ADD_radio_1 = ttk.Radiobutton(ADD_frame, text="ADD",variable=ADD_selection , value=1)
ADD_radio_1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
ADD_radio_2 = ttk.Radiobutton(ADD_frame, text="SUB",variable=ADD_selection,  value=2)
ADD_radio_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
ADD_radio_3 = ttk.Radiobutton(ADD_frame, text="HISTOGRAM MATCHING",variable=ADD_selection,  value=3)
ADD_radio_3.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

def print_ADD():
    s=int(ADD_selection.get())
    if(s==1):
        P1_add.P1(filename,filename_2)
    elif(s==2):
        P2_sub.P2(filename,filename_2)
    elif(s==3):
        P11_hist_matched.P11(filename,filename_2)
    
ADD_but_r = ttk.Button(ADD_frame, text="submet",command=print_ADD)
ADD_but_r.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")


########################################################## FILTERS ######################################

NEIGHBORHOOD_fram = ttk.LabelFrame(root_fram, text="NEIGHBORHOOD OPERATION")
NEIGHBORHOOD_fram.grid(row=0, column=3, padx=(20, 10), pady=(20, 10), sticky="nsew")



# Create a Frame for input widgets
widgets_frame_3 = ttk.Frame(NEIGHBORHOOD_fram, )
widgets_frame_3.grid(row=0, column=3, padx=3, pady=5, sticky="nsew", rowspan=3)
widgets_frame_3.columnconfigure(index=0, weight=1)
#FILTERS 1
      # Create a Frame for the Radiobuttons
filter_frame = ttk.LabelFrame(widgets_frame_3, text="FILTERS", padding=(20, 10))
filter_frame.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="nsew")

filter_list=['3x3','5x5','7x7','9x9']
filter_value1=tk.StringVar()

filter_input1 = ttk.Combobox(filter_frame, state="readonly", values=filter_list , textvariable=filter_value1)
filter_input1.current(0)
filter_input1.grid(row=0, column=0, padx=5, pady=10,  sticky="ew")

filter_selection=tk.StringVar()
filter_selection.set(None)

      # Radiobuttons
filter_radio_1 = ttk.Radiobutton(filter_frame, text="MEAN",variable=filter_selection , value=1)
filter_radio_1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
filter_radio_2 = ttk.Radiobutton(filter_frame, text="WEIGHTED",variable=filter_selection,  value=2)
filter_radio_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
filter_radio_3 = ttk.Radiobutton(filter_frame, text="MEDIAN",variable=filter_selection,  value=3)
filter_radio_3.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
filter_radio_4 = ttk.Radiobutton(filter_frame, text="MIN",variable=filter_selection,  value=4)
filter_radio_4.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")
filter_radio_5 = ttk.Radiobutton(filter_frame, text="MAX",variable=filter_selection,  value=5)
filter_radio_5.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

def print_filter():
    x=int(filter_selection.get())

    if(x==1):
        N1_average.N1(filename)
    elif(x==2):
        N6_weghite.N6(filename)
    elif(x==3):
        N2_median.N2(filename)
    elif(x==4):
        N8_min_smoothing.N8(filename)
    elif(x==5):
        N7_max_smoothing.N7(filename)
        
    
filter_but_r = ttk.Button(filter_frame, text="submet",command=print_filter)
filter_but_r.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

#FILTERS 2
      # Create a Frame for the Radiobuttons
filter2_frame = ttk.LabelFrame(widgets_frame_3, text="FILTERS", padding=(20, 10))
filter2_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

filter2_selection=tk.StringVar()
filter2_selection.set(None)

      # Radiobuttons
filter2_radio_1 = ttk.Radiobutton(filter2_frame, text="SHARPENING",variable=filter2_selection , value=1)
filter2_radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
filter2_radio_2 = ttk.Radiobutton(filter2_frame, text="UN-SHARPEN",variable=filter2_selection,  value=2)
filter2_radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
filter2_radio_3 = ttk.Radiobutton(filter2_frame, text="EDGE DETECTION",variable=filter2_selection,  value=3)
filter2_radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")


def print_filter():
    x=int(filter2_selection.get())

    if(x==1):
        N4_sharpinnig.N4(filename)
    elif(x==2):
        N5_unsharp.N5(filename)
    elif(x==3):
        N3_edge_detection.N3(filename)
    
filter2_but_r = ttk.Button(filter2_frame, text="submet",command=print_filter)
filter2_but_r.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")



#MODE=========>s


sv_ttk.set_theme("dark")

root.update()
root.mainloop()