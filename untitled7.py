from tkinter import *

root=Tk()
root.title("SALES APPLICATION")
root.geometry("700x500")
root.configure(bg="yellow")
month=["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

def maxProfit():
    max_profit=max(profits)
    max_profit_index=profits.index(max_profit)
    max_profit_month=month[max_profit_index]
    max_label["text"]="Maximum Profit Of "+str(max_profit)+" Was Given In The Month Of "+str(max_profit_month)

def minProfit():
    min_profit=min(profits)
    min_profit_index=profits.index(min_profit)
    min_profit_month=month[min_profit_index]
    min_label["text"]="Minimum Profit Of "+str(min_profit)+" Was Given In The Month Of "+str(min_profit_month)


month_label=Label(root,text="Month:['January','Feburary','March','April','May','June','July','August','September','October','November','December']")
profit_label=Label(root,text="Profit:(20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)")
max_btn=Button(root,text="Show Max Profiable Month",command=maxProfit,fg="white",bg="#1874CD")
max_label=Label(root)
min_btn=Button(root,text="Show Min Profiable Month",command=minProfit,fg="white",bg="#1874CD")
min_label=Label(root)

month_label.place(relx=0.5,rely=0.2,anchor=CENTER)
profit_label.place(relx=0.5,rely=0.3,anchor=CENTER)
max_btn.place(relx=0.5,rely=0.4,anchor=CENTER)
max_label.place(relx=0.5,rely=0.5,anchor=CENTER)
min_btn.place(relx=0.5,rely=0.6,anchor=CENTER)
min_label.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()