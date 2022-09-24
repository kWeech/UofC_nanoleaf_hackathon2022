"""
Written by: Tysy and Kenny NOT KIM

Description:
    Written to display "ZETTA" and spellout zetta on u of c brand color background on a hexagon display, created with 216
    nanoleaf light panels.
    
    Each row in the display has a dedicated controller except 1st two rows and last two rows. Total there are 12 rows and 10 controllers.
    
    This code is extended from the Demo script of basic OpenAPI functionality for interacting with Nanoleaf Light Panels.
    Which Included:
    - Retrieving authentication token
    - Getting device data including orientation, panelIds, and positions of all panels
    - Activation of stream control mode
    - Building and sending of stream control frames

    Comments are to help parse the code, and simplify understanding
    
Nanoleaf Devices OpenAPI Documentation: https://forum.nanoleaf.me/docs (requires registering for a developer account)
"""

import sys
import socket  # Used to stream data to the devices when in streaming mode, in DGRAM mode to facilitate communication to a udp socket
import json  # Used to convert dictionaries to jsons and vice versa, device data is stored in a json
import time
# Used for communication with the devices, changing modes and such
import http.client as httplib
import random
from webbrowser import GenericBrowser

# send is used heavily in the other functions to send the API commands needed. Read the nanoleaf open API documentation to get all of the
# possible functionality of this function!

if __name__ == "__main__":
    ips = ["192.168.1.14", "192.168.1.13", "192.168.1.12", "192.168.1.10", "192.168.1.11",
           "192.168.1.9", "192.168.1.4", "192.168.1.5", "192.168.1.3", "192.168.1.2"]
    frames5 = []
    import numpy as np
    import codecs
    import re
    import pandas as pd
    frames5 = []
    html_info = pd.DataFrame()
    file = codecs.open(
        '/Users/Isaiah/Desktop/triangulart2.html', "r", "utf-8")
    my_file_info = file.read()
    extract_script = re.compile(
        r"fill\=\"(?P<Colour>[\#[0-9a-zA-Z]*)\" rel\=\"(?P<Number>[0-9]+)")
    matchiter = extract_script.finditer(my_file_info)
    for match in matchiter:
        print(match.groupdict())
        html_info = html_info.append(match.groupdict(), ignore_index=True)

    def hex_to_rgb(row):
        colour = row['Colour'].lstrip('#')
        rgb = []
        for i in (0, 2, 4):
            decimal = int(colour[i:i+2], 16)
            rgb.append(decimal)
        return pd.Series([row['Number'], rgb[0], rgb[1], rgb[2]])

    FinalTable = pd.DataFrame()
    FinalTable = pd.concat([FinalTable, html_info.apply(
        hex_to_rgb, axis=1)])
    FinalTable = FinalTable.rename(columns={0: "Id", 1: "R", 2: "G", 3: "B"})
    # FinalTable = FinalTable.astype(int)
    print(FinalTable.iloc[:20])

    rownum = 0
    panel_id_dict = {}
    panel_id = 0
    iterate_row = 0
    for index, panel in FinalTable.iterrows():
        if (iterate_row == 23):
            #sendStreamControlFrames(frames5, ips[rownum])
            rownum += 1
            iterate_row = 0
            panel_id = 0

        if (panel['R'] == 50 & panel['G'] == 50 & panel['B'] == 50):
            pass
        else:
            frame = {'panelId': panel_id_dict[rownum][panel_id],
                     'R': panel['R'], 'G': panel['G'], 'B': panel['B'], 'T': 1}  
            frames5 += frame
            panel_id += 1
        iterate_row += 1
