"""
Written by: Tysy and Kenny and Isaiah and Kim

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
import http.client as httplib  # Used for communication with the devices, changing modes and such
import random

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
            conn.request(verb, endpoint, body, {"Content-Type": "application/json"})
        else:
            conn.request(verb, endpoint)
        response = conn.getresponse()
        body = response.read()
        return response.status, response.reason, body  # status is equivalent to the 200 phrase in the api docs,
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
    status, __, __ = send("PUT", end_point, json.dumps(ext_control_command), ip)  # json.dumps() changes the dict to
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
        stream.append(0 & 0xFF)  # White channel is automatically controlled, no need to set it
        stream.append(frame['T'] & 0xFF)
    sock.sendto(stream, (ip, port))

# Personally never had to use the coordinates, I'm sure they'll be useful in some projects though!
def getCoordinateRange(pData):
    '''
    Utility function that returns the minimum and maximum values for x and y from the positionData JSON
    Helpful for determining the bounds of your coordinate system!
    '''
    xMin, yMin = 99999, 99999
    xMax, yMax = -99999, -99999
    for panel in pData:
        xMin = min(xMin, panel['x'])
        yMin = min(yMin, panel['y'])
        xMax = max(xMax, panel['x'])
        xMax = max(yMax, panel['y'])
    coordinateRange = {'xMin': xMin, 'yMin': yMin, 'xMax': xMax, 'yMax': yMax}
    return coordinateRange

if __name__ == "__main__":
    ips = ["192.168.1.14", "192.168.1.13", "192.168.1.12", "192.168.1.10", "192.168.1.11", "192.168.1.9", "192.168.1.4", "192.168.1.5", "192.168.1.3", "192.168.1.2"]
    auths =  ['4xjvV9IJAQDq83SFaROVVzvble3vHwV8', 'LlBI3Odz7EOHR3v5TPwh4fDbGrFuKSq7', 'WKiepsgP7vhnfI4zGBmxVH26Rq6KNFgg', '28vOnfDhQZXeShXjGKWocxHZJUe9NCwn', 'vioLVKiV1IgfsAA94JFFBTFy0vEUG48K', 'UY3DEDumg19xCnwrNV4Btm2FPF0CAhdO', '0AJgQMml89aa12iAYpAqEoWKrKW18JZa', '5EpekYkcVupgIjXM37bRsNG0pE38NfGC', 'cSTCTsuAgBRC7i8F3ug1cc1Z1smDyPQH', 'kAbYywuZWBWsMrFsOluxbnqAXEQqyMKr']
    ip5 = "192.168.1.2"
    auth5 = "s0M4TKH8BhTxdSIReRuAJzAHTYkHTdWU"

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

    data = [data0, data1, data2, data3, data4, data5, data6, data7, data8, data9]
    position_data_dict = {}

    for i in range(10):
        position_data_dict[i] = data[i]['panelLayout']['layout']['positionData']
    
    print(position_data_dict[1])
    positionData5 = data5['panelLayout']['layout']['positionData']
    setStreamControlMode(ip5, auth5, 1)
    frames5 = []
    T = 2

    for panel in positionData5:
        R = 19
        G = 50
        B = 255
        frame5 = [{'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}]
        #print(panel['panelId'])

        sendStreamControlFrames(frame5, ip5)