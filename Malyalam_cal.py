Malayalam_month_conv = {
    1: "Chingam",
    2: "Kanni",
    3: "Thulam",
    4: "Vrishchikam",
    5: "Dhanu",
    6: "Makaram",
    7: "Kumbham",
    8: "Meenam",
    9: "Medam",
    10: "Edavam",
    11: "Midhuam",
    12: "Karkidakam"

}

mon_num = int(input("Enter a number to know the corresponding month in Malayalam: "))

if mon_num > 0 and mon_num < 13:
    print ("The Malayalam month is " + Malayalam_month_conv.get(mon_num))
else:
    print("Malayalam calender only has 12 months")
   
