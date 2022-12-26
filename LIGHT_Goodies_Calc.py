
from tkinter import *
import datetime as dt
from tkinter import messagebox
import gspread
from oauth2client.service_account import ServiceAccountCredentials

GREY = "#cdc2ae"
LIGHT_GREY = "#ece5c7"
FONT_NAME = "Comic Sans MS"
FONT_COLOR = "#354259"
LABEL_COLOR = "#42032C"

# ------------------------FUNCTIONS----------------------------------- #
class GoodiesData:

    light_sheet = []
    current_data = []
    nicklist = []
    current_values = {}
    data_to_send = []
    credentialsy = {
      "type": "service_account",
      "project_id": "light-goodies-calc-369121",
      "private_key_id": "0959313568809bb9669041ffc2825218d56bc881",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDkEJtNp/fGr7D2\nJqfDejgrWK96RLEZzUUGK+RhI1TnqRviUxK6e9IJzYlPbcUt+czlB3Ejd8mxPTtp\nJO3/Y29Dq0K0O8/mV39Pio8rfW6FKKWU54jW/s67qUTq39tSngcc3Mgw90QTrSKV\n4OTggPUbx9XCtvhoVH6Tpo0YthdFFi5tXHqP0pW+1WM0uqQWMFR37l22Mdk/rAWU\nLBqIY3NDKM9h/L6tT6KCtZrrFZyEcI25TOcl+P9M58DO8IK5fwyfDRq4J2FSW1Hm\nkKdIroTVAZlgiaGXP4xU/Ov2jVbFi05pmPf/tJGcLMud9C1DiGDgwiF6t9aisGSR\nBtmgHtetAgMBAAECggEABk8MflqKCNJ9j2MxWwxx9yAy0BIlx53W7d1GXSBVLgiO\nopudFh1S7/3iCv++QRyhL0K3imO7AUg9PclAovYITJoCGqpyGiAyGUXiQP5tKyM2\nzvnHd/imryh3C68M/TbG4csC598Nk74p1nVZD3n+jcatrv9Q7tEYV60Q4SEEX5JS\nOYR/eFfESi6C9lC+o8i+zPBj49hioRb/6hmCJxwXwpTwCovpzUD2RR1v427BWhZk\nYdHWfKyP6+FuGMxLhbtr0FCWIpW0XSXKf3qZsG5AWMMEmlyMAD64vCYf4+n49ZCX\ngzL1sdS0nezh8llJs/TnYztIfAP2/N+tYcsR2qttAQKBgQD9uMD3UP9GEH6JPa3j\nSw3JIrUCHJBVFOMLpwR3rWHc93pDvHM5BcHM8tR8qAev8fY29cFpmZPhXJ3hAZUG\ny17WyWhk6RNqQKjs6PiR3OlG/m6Rq8qaxrIPLSz/vDtmrINJOlreuRdAKR4nZeLu\nPw9+Hl+6Bu4qs74xNdQ2xctsLQKBgQDmHN+4DWHt0MQguL8071Cqal1R6HjZ8RUd\nwGNRfNOgnybIYiTcUeMNHgx/XMM54PTQmS3TIl4OnHy2jPsTtpTp/+S6VOlTrnmN\nCsTsJA7mZiI1Rwhu2Go3p/Ac99fzPdLQwSUXXu5PQZ6b98iZrqhlkkrVeCiJQsX+\ncu2MpibJgQKBgHFj5VFiMIO2kWZyW0kuXL3cNfr4mwR7LjEh9lwp74eaTlkBWplM\nWl1m1NHVIoJeZ4QOdt7j1PQtuR064MhFkV/6aR5YD+Y3eYdPYu+FQ/gHc5DErupX\nDHK95NNx4zYyuQW7/6p0G9D/z0saPL3vDtR1bKCtwjjxVXmWrf3AjfYNAoGBAIlQ\nyZ/HPJzxa1grZs5r0LMg7bcnBpbnajZqy9mgp5i94CLLjjt7EgaN299Ut5seRnkE\nL3hCleYaM8Grt1g4J/zLGu6mJOYuw5IKzyArFEkgwWERllKvChNUP9DJhTA9wEOa\nPkwH9iWNftyLrEUpGIwkFEv2fBoMoqIIawD3VUYBAoGAJ3nLGuneYx53/UyzMkBg\nQGOGey6xsyC0/zr7s26PtMO1/dmix9cT7JMNBT/CciL6SR6FFx7J5grdgt8mB43a\n7BLklwMLo9mG5T73hW2MaJDF/9mryvM1QWTud20m+anhr2OKSJorNFFvlUDiy8yJ\nLumo07p2Sfs/myJ0Xfw7eAI=\n-----END PRIVATE KEY-----\n",
      "client_email": "legendarymight@light-goodies-calc-369121.iam.gserviceaccount.com",
      "client_id": "106693453803529435454",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/legendarymight%40light-goodies-calc-369121.iam.gserviceaccount.com"
    }
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        lightCreds = ServiceAccountCredentials.from_json_keyfile_dict(self.credentialsy)
        light_client = gspread.authorize(lightCreds)
        self.light_sheet = light_client.open("Goodies_Calc").sheet1
        self.current_data = self.light_sheet.get_all_records()
        self.get_nick_list(self.current_data)

    def start(self, parametry):
        self.get_data(parametry)
        # self.get_nick_list(self.current_data)
        self.send_data()


    def get_data(self, parametry):
        nickname = parametry["nickname"]
        uni_nickname = nickname.lower()


        today = dt.datetime.now()
        obrobione_today = today.strftime("%d/%m/%Y")
        # obrobiony_time = today.strftime("%X")

        current_values = self.get_user_rowdata(uni_nickname)

        if parametry["future_points"] == "":
            if current_values["futureRuneweekScore"] == "":
                f_points = 0
            else:
                f_points = int(current_values["futureRuneweekScore"])
            print(current_values)
        else:
            f_points = int(parametry["future_points"])

        if parametry["current_points"] == "":
            if current_values["currentRuneweekScore"] == "":
                c_points = 0
            else:
                c_points = int(current_values["currentRuneweekScore"])
        else:
            c_points = int(parametry["current_points"])

        if parametry["maps"] == "":
            maps = int(current_values["maps"])
        else:
            maps = parametry["maps"]

        if parametry["blueprints"] == "":
            blueprints = current_values["blueprints"]
        else:
            blueprints = parametry["blueprints"]

        if parametry["horns"] == "":
            horns = current_values["horns"]
        else:
            horns = parametry["horns"]

        if parametry["peaches"] == "":
            peaches = current_values["peaches"]
        else:
            peaches = parametry["peaches"]

        self.data_to_send = {
                "nickname": nickname,
                "dateOfUpdate": obrobione_today,
                "futureRuneweekScore": f_points,
                "currentRuneweekScore": c_points,
                "left points": None,
                "maps": maps,
                "mp": None,
                "blueprints": blueprints,
                "bp": None,
                "horns": horns,
                "hp": None,
                "peaches": peaches,
            }

    def get_user_rowdata(self, user):
        goodies_data = self.current_data
        nick_list = self.nicklist

        # nr_wiersza = nick_list.index(user)
        nr_wiersza = self.find_in_list(user, nick_list)
        try:
            user_current_values = goodies_data[nr_wiersza]
        except IndexError:
            user_current_values = {
                    "nickname": "",
                    "dateOfUpdate": "",
                    "futureRuneweekScore": 0,
                    "currentRuneweekScore": 0,
                    "left points": None,
                    "maps": 0,
                    "mp": None,
                    "blueprints": 0,
                    "bp": None,
                    "horns": 0,
                    "hp": None,
                    "peaches": 0,
                }

        # print(user_current_values)
        return user_current_values

    def find_in_list(self, needle, haystack):
        needle_index = -1
        empty_row = -1
        idx = 0
        for cus in haystack:
            if cus == needle:
                return idx
            elif cus == '' and empty_row == -1:
                empty_row = idx
            idx += 1
        if empty_row != -1:
            needle_index = empty_row
        else:
            needle_index = idx
        return needle_index


    def get_nick_list(self, data):
        nick_list = []
        for cus in data:
            if "nickname" in cus.keys():
                nickname = cus["nickname"].lower()
                nick_list.append(nickname)
        self.nicklist = nick_list
        return nick_list

    def send_data(self):

        nr_wiersza = self.find_in_list(self.data_to_send["nickname"], self.nicklist) +2
        odp = self.light_sheet.update('B' + str(nr_wiersza), [list(self.data_to_send.values())])


        messagebox.showinfo(title=None, message="Thanks")
        exit()
    def checkWprowadzoneDane(self, user_input):
        listerr = []
        if user_input["nickname"] == "":
            messagebox.showwarning(title=None, message="You left empty field 'nickname'")
            return False
        if(user_input["future_points"] != "" and type(int(user_input["future_points"])) != int):
            messagebox.showwarning(title=None, message=f"{user_input['future_points']} is not a number")
            return False
        if(user_input["current_points"] != "" and type(int(user_input["current_points"])) != int):
            messagebox.showwarning(title=None, message=f"{user_input['current_points']} is not a number")
            return False

        return True

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Goodies Calc")
window.config(padx=20, pady=20, bg=GREY)



#  -------------Labels------------
label_title = Label(text="Goodies Calc Updater", fg="#ff4c29", font=(FONT_NAME, 15, "bold"), bg=GREY)
label_title.grid(column=0, row=0, sticky="E")
label_title.config(padx=5, pady=5)
label_rights = Label(text="©pff singularities, 2022", fg="#1e5128", bg=GREY)
label_rights.grid(column=1, row=0, sticky="E")
label_rights.config(padx=5, pady=5)

label_nickname = Label(text="Nickname in the game", fg=LABEL_COLOR, font=(FONT_NAME, 15, "bold"), bg=GREY)
label_nickname.grid(column=0, row=1, sticky="E")
label_nickname.config(padx=5, pady=5)

label_future_points = Label(text="How many points during RuneWeek \nare you going to get?:", fg=LABEL_COLOR, font=(FONT_NAME, 15, "bold"), bg=GREY)
label_future_points.grid(column=0, row=4, sticky="E")
label_future_points.config(padx=5, pady=5)
label_current_points = Label(text="How many points \nare you got so far?:", fg=LABEL_COLOR, font=(FONT_NAME, 15, "bold"), bg=GREY)
label_current_points.grid(column=0, row=5, sticky="E")
label_current_points.config(padx=5, pady=5)

label_maps = Label(text="How many maps \ndo you have?:", fg=LABEL_COLOR, font=(FONT_NAME, 15, "bold"), bg=GREY)
label_maps.grid(column=0, row=6, sticky="E")
label_maps.config(padx=5, pady=5)
label_blueprints = Label(text="How many blueprints?:", fg=LABEL_COLOR, font=(FONT_NAME, 15, "bold"), bg=GREY)
label_blueprints.grid(column=0, row=7, sticky="E")
label_blueprints.config(padx=5, pady=5)
label_horns = Label(text="How many ravens/pollens?:", fg=LABEL_COLOR, font=(FONT_NAME, 15, "bold"), bg=GREY)
label_horns.grid(column=0, row=8, sticky="E")
label_horns.config(padx=5, pady=5)
label_peaches = Label(text="How many peaches/briars?:", fg=LABEL_COLOR, font=(FONT_NAME, 15, "bold"), bg=GREY)
label_peaches.grid(column=0, row=9, sticky="E")
label_peaches.config(padx=5, pady=5)

# ------------Button & Entries & Spinboxes-----------

entry_nickname = Entry(width=17, fg=FONT_COLOR, font=(FONT_NAME, 15, "bold"), bg=LIGHT_GREY)
entry_nickname.focus()
entry_nickname.grid(column=1, row=1)

entry_future_points = Entry(width=17, fg=FONT_COLOR, font=(FONT_NAME, 15, "bold"), bg=LIGHT_GREY)
entry_future_points.focus()
entry_future_points.grid(column=1, row=4)
entry_current_points = Entry(width=17, fg=FONT_COLOR, font=(FONT_NAME, 15, "bold"), bg=LIGHT_GREY)
entry_current_points.focus()
entry_current_points.grid(column=1, row=5)

spinbox_map = Spinbox(from_=0, to=100, width=5)
spinbox_map.grid(column=1, row=6)
spinbox_blueprint = Spinbox(from_=0, to=100, width=5)
spinbox_blueprint.grid(column=1, row=7)
spinbox_horn = Spinbox(from_=0, to=100, width=5)
spinbox_horn.grid(column=1, row=8)
spinbox_peach = Spinbox(from_=0, to=100, width=5)
spinbox_peach.grid(column=1, row=9)
def zaje():
    gd = GoodiesData()
    user_params = {
        "nickname": entry_nickname.get(),
        "future_points": entry_future_points.get(),
        "current_points": entry_current_points.get(),
        "maps": spinbox_map.get(),
        "blueprints": spinbox_blueprint.get(),
        "horns": spinbox_horn.get(),
        "peaches": spinbox_peach.get(),
    }
    if gd.checkWprowadzoneDane(user_params):
        gd.start(user_params)
button_search = Button(text="Update", fg=FONT_COLOR, font=(FONT_NAME, 15, "bold"), width=17, bg=LIGHT_GREY, command=zaje)
button_search.grid(column=1, row=10)
button_search.config(padx=5, pady=5)

window.mainloop()
