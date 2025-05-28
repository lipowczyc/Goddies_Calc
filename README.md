"""
This Python application provides a graphical interface (built with Tkinter) for updating player statistics related 
to an event-based game feature ("RuneWeek") in a Google Sheets document. It collects user-input data such as 
nickname, expected points, current progress, and items (maps, blueprints, horns, peaches), processes it, and 
sends it to a predefined spreadsheet.

Key Features:
Tkinter-based GUI for user interaction.,
Google Sheets integration via gspread and OAuth2 credentials.
Basic data validation and user-friendly alerts via message boxes.
Persistent nickname and stat tracking using live spreadsheet data.
Designed for small game communities or private event tracking.

Technologies Used:
Tkinter for the GUI,
gspread + oauth2client for Google Sheets interaction,
datetime for time-stamping updates,
messagebox for user feedback and error handling

Author: Sylwia Postnikoff
"""