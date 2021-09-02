#This is desktop app written in python
#User fills values such as weight, height, age, etc. and selects which formulas wants ot calculate
#Result is shown in text field
#imports
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm


def get_calories_multiplier(activ_text):
    if activ_text == "žádná, nízká":
        return 1.2
    elif activ_text == "lehká=1-3 dny/týden":
        return 1.375
    elif activ_text == "střední=3-5 dnů/týden":
        return 1.55
    elif activ_text == "vysoká=6-7 dnů/týden":
        return 1.725
    elif activ_text == "velmi vysoká=fyzická práce":
        return 1.9
    else:
        tkm.showwarning("Aktivita", "Pravděpodobně jsi nevybral aktivitu\nVyber a klikni na Vypočítej")
        return 0


def check_input_var(inp_var, var_name):
    try:
        return_val = float(str(inp_var).replace(",", "."))
    except:
        tkm.showwarning("Špatná hodnota", "{} byla špatně zadána.\nOprav ji a klikni na Vypočítej".format(var_name))
        return -1

    return return_val


def click_exit():
    exit()


def click_count():
    height = check_input_var(height_e.get(), "Výška")
    if height == -1:
        return

    weight = check_input_var(weight_e.get(), "Váha")
    if weight == -1:
        return

    prot_multiplier = check_input_var(protein_e.get(), "Množství bílkovin")
    if prot_multiplier == -1:
        return

    cal_multiplier = get_calories_multiplier(activity_var.get())
    #waist = float(str(waist_e.get()).replace(",", "."))
    age = int(age_e.get())
    print_text = ""

    if height > 3:
        height = height/100

    #BMI
    if bmi_tf.get():
        print_text = print_text + "BMI: {}\n".format(round(weight / (height * height), 2))

    #Protein amount
    if protein_count_tf.get():
        print_text = print_text + "Množství bílkovin(g): {}\n".format(int(round(prot_multiplier * weight, 0)))

    #BMR
    if gender_var.get() == "M":
        bmr_hbe = 66.47 + (13.75 * weight) + (5.003 * height * 100) - (6.775 * age)
        bmr_msj = (10 * weight) + (6.25 * height * 100) - (5 * age) + 5
    elif gender_var.get() == "F":
        bmr_hbe = 655.1 + (9.563 * weight) + (1.85 * height * 100) - (4.676 * age)
        bmr_msj = (10 * weight) + (6.25 * height * 100) - (5 * age) - 161
    else:
        tkm.showwarning("Volba pohlaví", "Nevybral jsi pohlaví.\nVyber a pokračuj kliknutím na vypočítej.")
        return

    if bmr_hbe_tf.get():
        print_text = print_text + "BMR(Harris-Benedict): {}\n".format(round(bmr_hbe, 2))
    if bmr_msj_tf.get():
        print_text = print_text + "BMR(Mifflin-St. Jeor): {}\n".format(round(bmr_msj, 2))

    if cal_count_hbe_tf.get():
        print_text = print_text + "Minimum kalorií(Harris-Benedict)(kcal): {}\n".format(round(cal_multiplier * bmr_hbe, 2))
    if cal_count_msj_tf.get():
        print_text = print_text + "Minimum kalorií(Mifflin-St. Jeor)(kcal): {}\n".format(round(cal_multiplier * bmr_msj, 2))

    if len(print_text) > 0:
        print_text = print_text + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    print(print_text)
    solution_t.insert(tk.END, print_text)


def click_clear():
    solution_t.delete("1.0", "end")
    weight_e.delete(0, "end")
    height_e.delete(0, "end")
    protein_e.delete(0, "end")
    age_e.delete(0, "end")
    waist_e.delete(0, "end")
    protein_e.insert(0, 1.5)

wnd = tk.Tk()

#variables declaring
weight_var = tk.IntVar
height_var = tk.IntVar
protein_var = tk.IntVar
age_var = tk.IntVar
gender_var = tk.StringVar()
waist_var = tk.IntVar
activity_var = tk.StringVar()
bmi_tf = tk.IntVar()
protein_count_tf = tk.IntVar()
bmr_hbe_tf = tk.IntVar()
bmr_msj_tf = tk.IntVar()
cal_count_hbe_tf = tk.IntVar()
cal_count_msj_tf = tk.IntVar()


wnd.wm_title("Kalkulacka hubnoucich velicin")
wnd.geometry("650x350")

#frames
upper_frame = tk.Frame(wnd, width=1150, height=450)
upper_frame.grid(row=0, column=0)

input_frame = tk.Frame(upper_frame, width=800, height=300, bg="turquoise2")
input_frame.grid(row=0, column=0)

output_frame = tk.Frame(wnd, width=1150, height=150)
output_frame.grid(row=1, column=0)

selection_frame = tk.Frame(upper_frame, width=350, height=300, bg="khaki3")
selection_frame.grid(row=0, column=1)
#labels
weight_l = tk.Label(input_frame, text="Váha", bg="turquoise2")
height_l = tk.Label(input_frame, text="Výška", bg="turquoise2")
protein_l = tk.Label(input_frame, text="Bílkoviny/kg", bg="turquoise2")
age_l = tk.Label(input_frame, text="Věk", bg="turquoise2")
gender_l = tk.Label(input_frame, text="Pohlaví", bg="turquoise2")
waist_l = tk.Label(input_frame, text="Obvod pasu", bg="turquoise2")
activity_l = tk.Label(input_frame, text="Aktivita", bg="turquoise2")
select_l = tk.Label(selection_frame, text="Výběr hodnot", bg="khaki3")

#entry fields
weight_e = tk.Entry(input_frame, textvariable=weight_var)
height_e = tk.Entry(input_frame, textvariable=height_var)
protein_e = tk.Entry(input_frame, textvariable=protein_var)
age_e = tk.Entry(input_frame, textvariable=age_var)
waist_e = tk.Entry(input_frame, textvariable=waist_var)

protein_e.insert(0, 1.5)


#text fields
solution_t = tk.Text(output_frame, width=40, height=8)
solution_t.pack()

#radiobuttons
male_r = tk.Radiobutton(input_frame, text="Muž", variable=gender_var, value="M", bg="turquoise2")
female_r = tk.Radiobutton(input_frame, text="Žena", variable=gender_var, value="F", bg="turquoise2")

#comboboxes
activity_cb = ttk.Combobox(input_frame, width=20, textvariable=activity_var)
activity_cb['values'] = ("žádná, nízká",
                         "lehká=1-3 dny/týden",
                         "střední=3-5 dnů/týden",
                         "vysoká=6-7 dnů/týden",
                         "velmi vysoká=fyzická práce"
                         )

#checkboxes
bmi_chb = tk.Checkbutton(selection_frame, text="BMI", variable=bmi_tf, bg="khaki3")
bmi_chb.select()

protein_count_chb = tk.Checkbutton(selection_frame, text="Množství bílkovin", variable=protein_count_tf, bg="khaki3")
protein_count_chb.select()

bmr_hbe_chb = tk.Checkbutton(selection_frame, text="BMR(Harr.-Ben.)", variable=bmr_hbe_tf, bg="khaki3")
bmr_hbe_chb.select()

bmr_msj_chb = tk.Checkbutton(selection_frame, text="BMR(Miff.-St.J.)", variable=bmr_msj_tf, bg="khaki3")
bmr_msj_chb.select()

cal_count_hbe_chb = tk.Checkbutton(selection_frame, text="Kcal.(Harr.-Ben.)", variable=cal_count_hbe_tf, bg="khaki3")
cal_count_hbe_chb.select()

cal_count_msj_chb = tk.Checkbutton(selection_frame, text="Kcal.(Miff.-St.J.)", variable=cal_count_msj_tf, bg="khaki3")
cal_count_msj_chb.select()

#buttons
exit_b = tk.Button(input_frame, text="Zavřít", bg="violet red", command=click_exit)
count_b = tk.Button(input_frame, text="Vypočítej", bg="green", command=click_count)
clear_b = tk.Button(input_frame, text="Vyčisti", bg="red", command=click_clear)

#set positions
weight_l.grid(row=1, column=0)
weight_e.grid(row=1, column=1)

height_l.grid(row=2, column=0)
height_e.grid(row=2, column=1)

age_l.grid(row=3, column=0)
age_e.grid(row=3, column=1)

waist_l.grid(row=4, column=0)
waist_e.grid(row=4, column=1)

protein_l.grid(row=5, column=0)
protein_e.grid(row=5, column=1)

gender_l.grid(row=6, column=0)
male_r.grid(row=6, column=1)
female_r.grid(row=6, column=2)

activity_l.grid(row=7, column=0)
activity_cb.grid(row=7, column=1)

exit_b.grid(column=1, row=0)
count_b.grid(row=8, column=1)
clear_b.grid(row=8, column=0)

solution_t.grid(row=0, column=0)

select_l.grid(row=0, column=0)
bmi_chb.grid(row=1, column=0)
protein_count_chb.grid(row=2, column=0)
bmr_hbe_chb.grid(row=3, column=0)
bmr_msj_chb.grid(row=4, column=0)
cal_count_hbe_chb.grid(row=5, column=0)
cal_count_msj_chb.grid(row=6, column=0)


wnd.mainloop()
