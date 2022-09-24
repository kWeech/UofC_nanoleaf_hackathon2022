"""
Written by: Tysy and Kenny and Isaiah and Kim

Description:
Nanoleaf Devices OpenAPI Documentation: https://forum.nanoleaf.me/docs (requires registering for a developer account)
"""

import sys
import socket  # Used to stream data to the devices when in streaming mode, in DGRAM mode to facilitate communication to a udp socket
import json  # Used to convert dictionaries to jsons and vice versa, device data is stored in a json
import time
# Used for communication with the devices, changing modes and such
import http.client as httplib
import random
import numpy as np
import codecs
import re
import pandas as pd
import os

API_PORT = "16021"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send is used heavily in the other functions to send the API commands needed. Read the nanoleaf open API documentation to get all of the
# possible functionality of this function!


def send(verb, endpoint, body, ip):
    '''
    Sends an API command to the Nanoleaf device at a given IP address
    '''
    LISTENER = ip + ":" + API_PORT
    try:
        conn = httplib.HTTPConnection(LISTENER)
        if len(body) != 0:
            conn.request(verb, endpoint, body, {
                         "Content-Type": "application/json"})
        else:
            conn.request(verb, endpoint)
        response = conn.getresponse()
        body = response.read()
        # status is equivalent to the 200 phrase in the api docs,
        return response.status, response.reason, body
        # reason is the text next to the number (OK, No Content, etc.) body, as defined in the line above is found using
        # the .read() method, and returns the response body as defined in the api docs.
    except (httplib.HTTPException, socket.error) as ex:
        print("Error: %s" % ex)

# these next few functions are specified commands from the open API, the "section" referred to in the docstring is
# the section of the open API that this command is in.


def getDeviceData(ip, auth):
    '''
    Gets all panel info from the Nanoleaf device, returns in the format of the API JSON in the documentation
    can be accessed using json.loads() to create a dictionary, then by using regular python dictionary syntax

    Section 4.1 "API JSON Structure > Light Panels"
    '''
    endpoint = "/api/v1/" + auth
    status, __, body = send("GET", endpoint, {}, ip)  # body is the json
    if not status == 200:
        print("could not connect: " + str(status))
        # exit(1)
    return body


def setStreamControlMode(ip, auth, version):
    '''
    Enables stream control mode on the Nanoleaf device version should be 1, all controllers need to be set to be streamed to

    Section 3.2.6.2 "External Control (extControl)" && Section 5.7 "External Control (Streaming)"
    '''
    end_point = "/api/v1/" + auth + "/effects"
    ext_control_version = "v" + str(version)
    ext_control_command = {
        'write': {'command': 'display', 'animType': 'extControl', 'extControlVersion': ext_control_version}}
    status, __, __ = send("PUT", end_point, json.dumps(
        ext_control_command), ip)  # json.dumps() changes the dict to
    # json format to be used by the devices
    if not (status == 200 or status == 204):
        print("could not connect: " + str(status))

# This function is how the panel data is sent to the controllers, if you


def sendStreamControlFrames(frames, ip):
    '''
    frames: An array of frames, with each frame consisting of a dictionary with the panelId and the color
    the panel must go to in the specified time. Color is specified as R, G, B and transTime (T) in multiples of 100ms.

    Section 3.2.6.2 "External Control (extControl)" && Section 5.7 "External Control (Streaming)"
    '''
    stream = bytearray()
    stream.append(len(frames) & 0xFF)
    # Port is 60221 for v1 (original Light Panels), v2 for our newer products (Shapes, Elements, Canvas)
    # this number can be found by returning the body in the setStreamControlMode function
    port = 60221
    for frame in frames:
        stream.append(frame['panelId'] & 0xFF)
        # This & 0xFF term makes is so only the last 8 bytes are used,
        # not sure if it is necessary here but it doesn't hurt
        stream.append(1 & 0xFF)
        stream.append(frame['R'] & 0xFF)
        stream.append(frame['G'] & 0xFF)
        stream.append(frame['B'] & 0xFF)
        # White channel is automatically controlled, no need to set it
        stream.append(0 & 0xFF)
        stream.append(frame['T'] & 0xFF)
    sock.sendto(stream, (ip, port))


def hex_to_rgb(row):
    colour = row['Colour'].lstrip('#')
    rgb = []
    for i in (0, 2, 4):
        decimal = int(colour[i:i+2], 16)
        rgb.append(decimal)
    return pd.Series([row['Number'], rgb[0], rgb[1], rgb[2]])


if __name__ == "__main__":
    ips = ["192.168.1.14", "192.168.1.13", "192.168.1.12", "192.168.1.10", "192.168.1.11",
           "192.168.1.9", "192.168.1.4", "192.168.1.5", "192.168.1.3", "192.168.1.2"]
    auths = ['4xjvV9IJAQDq83SFaROVVzvble3vHwV8', 'LlBI3Odz7EOHR3v5TPwh4fDbGrFuKSq7', 'WKiepsgP7vhnfI4zGBmxVH26Rq6KNFgg', '28vOnfDhQZXeShXjGKWocxHZJUe9NCwn', 'vioLVKiV1IgfsAA94JFFBTFy0vEUG48K',
             'UY3DEDumg19xCnwrNV4Btm2FPF0CAhdO', '0AJgQMml89aa12iAYpAqEoWKrKW18JZa', '5EpekYkcVupgIjXM37bRsNG0pE38NfGC', 'cSTCTsuAgBRC7i8F3ug1cc1Z1smDyPQH', 'kAbYywuZWBWsMrFsOluxbnqAXEQqyMKr']

    # Setting up controllers
    data0 = json.loads(getDeviceData(ips[0], auths[0]))
    data1 = json.loads(getDeviceData(ips[1], auths[1]))
    data2 = json.loads(getDeviceData(ips[2], auths[2]))
    data3 = json.loads(getDeviceData(ips[3], auths[3]))
    data4 = json.loads(getDeviceData(ips[4], auths[4]))
    data5 = json.loads(getDeviceData(ips[5], auths[5]))
    data6 = json.loads(getDeviceData(ips[6], auths[6]))
    data7 = json.loads(getDeviceData(ips[7], auths[7]))
    data8 = json.loads(getDeviceData(ips[8], auths[8]))
    data9 = json.loads(getDeviceData(ips[9], auths[9]))

    setStreamControlMode(ips[0], auths[0], 1)
    setStreamControlMode(ips[1], auths[1], 1)
    setStreamControlMode(ips[2], auths[2], 1)
    setStreamControlMode(ips[3], auths[3], 1)
    setStreamControlMode(ips[4], auths[4], 1)
    setStreamControlMode(ips[5], auths[5], 1)
    setStreamControlMode(ips[6], auths[6], 1)
    setStreamControlMode(ips[7], auths[7], 1)
    setStreamControlMode(ips[8], auths[8], 1)
    setStreamControlMode(ips[9], auths[9], 1)

    data = [data0, data1, data2, data3, data4,
            data5, data6, data7, data8, data9]
    position_data_dict = {}

    # Creates dictionary that has each row as key and json position data as values
    for i in range(10):
        position_data_dict[i] = data[i]['panelLayout']['layout']['positionData']

    # Creates a list of lists that contain the panelIds
    panel_ids = []
    for i in position_data_dict:
        panel_ids.append([])
        # print(dictionary_data[i])
        for j in position_data_dict[i]:
            # print(j['panelId'])
            panel_ids[i].append(j['panelId'])

    # Split up first controller into two rows
    first_row = panel_ids[0][0:14]
    first_row.append(panel_ids[0][27])
    zero_row = panel_ids[0][14:27]

    # Insert new list
    panel_ids.pop(0)
    panel_ids.insert(0, first_row)
    panel_ids.insert(0, zero_row[::-1])

    nine_row = panel_ids[10][0:14]
    nine_row.append(panel_ids[10][27])

    ten_row = panel_ids[10][14:27]
    # print(ten_row)

    # Add new list of lists for last two rows
    panel_ids.pop(10)
    panel_ids.insert(10, nine_row)
    panel_ids.insert(11, ten_row[::-1])

    # Creates a new dictionary that contains only the row and panel Ids
    panel_id_dict = {}
    for i in range(12):
        panel_id_dict[i] = panel_ids[i]

    # Isaiah's code:
    file_list = [
        'image_files/background.html',
        'image_files/UofC_title.html',
        'image_files/UofC_title.html',
        'image_files/dino_standing.html',
        'image_files/dino_roar.html',
        'image_files/dino_standing.html',
        'image_files/dino_mouth_open.html',
        'image_files/dino_fire_0.html',
        'image_files/dino_fire_1.html',
        'image_files/dino_fire_2.html',
        'image_files/dino_fire_3.html',
        'image_files/dino_mouth_open.html',
        'image_files/dino_standing.html',
        'image_files/dino_front.html',
        'image_files/dino_front_open.html',
        'image_files/dino_front_fire_0.html',
        'image_files/dino_front_fire_1.html',
        'image_files/dino_front_fire_2.html',
        'image_files/dino_front_fire_3.html',
        'image_files/go_dinos.html',
        'image_files/go_dinos2.html',
        'image_files/go_dinos.html',
        'image_files/go_dinos2.html'
    ]
    while(True):
        for curr_file in file_list:
            time.sleep(0.4)
            html_info = pd.DataFrame()
            file = codecs.open(curr_file, "r", "utf-8")
            my_file_info = file.read()
            extract_script = re.compile(
                r"fill\=\"(?P<Colour>[\#[0-9a-zA-Z]*)\" rel\=\"(?P<Number>[0-9]+)")
            matchiter = extract_script.finditer(my_file_info)
            for match in matchiter:
                # print(match.groupdict())
                html_info = html_info.append(
                    match.groupdict(), ignore_index=True)

            FinalTable = pd.DataFrame()
            FinalTable = pd.concat([FinalTable, html_info.apply(
                hex_to_rgb, axis=1)])
            FinalTable = FinalTable.rename(
                columns={0: "Id", 1: "R", 2: "G", 3: "B"})
            # FinalTable = FinalTable.astype(int)
            # print(FinalTable.iloc[:20])

            ips = ["192.168.1.14", "192.168.1.14", "192.168.1.13", "192.168.1.12", "192.168.1.10", "192.168.1.11",
                   "192.168.1.9", "192.168.1.4", "192.168.1.5", "192.168.1.3", "192.168.1.2", "192.168.1.2"]
            # For loop iterating through panelId dict and color table
            frames5 = []
            rownum = 0
            panel_id = 0
            iterate_row = 0
            for index, panel in FinalTable.iterrows():
                if (iterate_row == 25):
                    sendStreamControlFrames(frames5, ips[rownum])
                    frames5 = []
                    rownum += 1
                    iterate_row = 0
                    panel_id = 0

                if (panel['R'] == 50 & panel['G'] == 50 & panel['B'] == 50):
                    pass
                else:
                    frame = {'panelId': panel_id_dict[rownum][panel_id],
                             'R': panel['R'], 'G': panel['G'], 'B': panel['B'], 'T': 1}
                    frames5.append(frame)
                    panel_id += 1
                iterate_row += 1
            sendStreamControlFrames(frames5, ips[rownum])
