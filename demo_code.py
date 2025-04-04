import serial
import time
def send_to_arduino(ser,value):
    ser.write(str.encode(value + "%"))
    time.sleep(0.1)

def btt_command(ser, str_command):
    ser.write(str.encode(str_command))
    time.sleep(1)
    while True:
        line = ser.readline()
        print(line)
        if line == b'ok\n':
            break

def draw_cube_limits(ser,dx, dy, dz,pos_delay_x,pos_delay_y,pos_delay_z):
 x = 0
 y = 0
 z = 0

 z += dz

 btt_command(ser, "G0 Z" + str(z) + "\r\n")
 time.sleep(pos_delay_z)

 draw_horizontal_surface_without_measuring_delay(btt,dx,dy,pos_delay_x,pos_delay_y)

 z-=dz

 btt_command(ser, "G0 Z" + str(z) + "\r\n")
 time.sleep(pos_delay_z)

 draw_horizontal_surface_without_measuring_delay(btt,dx,dy,pos_delay_x,pos_delay_y)


def draw_horizontal_surface_without_measuring_delay(ser,dx,dy,pos_delay_x,pos_delay_y):
    x = 0
    y = 0
    z = 0
    x += dx
    btt_command(ser, "G0 X" + str(x) + "\r\n")
    time.sleep(pos_delay_x)
    y += dy
    btt_command(ser, "G0 Y" + str(y) + "\r\n")
    time.sleep(pos_delay_y)
    x -= dx
    btt_command(ser, "G0 X" + str(x) + "\r\n")
    time.sleep(pos_delay_x)
    y -= dy
    btt_command(ser, "G0 Y" + str(y) + "\r\n")
    time.sleep(pos_delay_y)

def draw_horizontal_surface_measuring(btt,arduino,dx,dy,measuring_delay,pos_delay_x,pos_delay_y):
    x = 0
    y = 0
    z = 0
    x += dx
    btt_command(btt, "G0 X" + str(x) + "\r\n")
    time.sleep(pos_delay_x)
    send_to_arduino(arduino, str(1234))
    time.sleep(measuring_delay)

    y += dy
    btt_command(btt, "G0 Y" + str(y) + "\r\n")
    time.sleep(pos_delay_y)
    send_to_arduino(arduino, str(1234))
    time.sleep(measuring_delay)

    x -= dx
    btt_command(btt, "G0 X" + str(x) + "\r\n")
    time.sleep(pos_delay_x)
    send_to_arduino(arduino, str(1234))
    time.sleep(measuring_delay)

    y -= dy
    btt_command(btt, "G0 Y" + str(y) + "\r\n")
    time.sleep(pos_delay_y)
    send_to_arduino(arduino, str(1234))
    time.sleep(measuring_delay)

def draw_cube(btt,arduino,dx, dy,dz,measuring_delay,pos_delay_x,pos_delay_y,pos_delay_z):

     x = 0
     y = 0
     z = 0

     z += dz
     btt_command(btt, "G0 Z" + str(z) + "\r\n")
     time.sleep(pos_delay_z)
     send_to_arduino(arduino,str(1234))
     time.sleep(measuring_delay)

     draw_horizontal_surface_measuring(btt,arduino,dx, dy,measuring_delay,pos_delay_x,pos_delay_y)

     z -= dz
     btt_command(btt, "G0 Z" + str(z) + "\r\n")
     time.sleep(pos_delay_z)
     send_to_arduino(arduino, str(1234))
     time.sleep(measuring_delay)

     draw_horizontal_surface_measuring(btt,arduino,dx, dy,measuring_delay,pos_delay_x,pos_delay_y)


btt = serial.Serial('COM8', 115200)
arduino = serial.Serial(port='COM4', baudrate = 9600)
time.sleep(2)
"""
#btt_command(btt, "G28" + "\r\n")
#btt_command(btt, "G21" + "\r\n") regulate to millimeters

#calculating rotating delay
degrees = 180
rotating_delay = (degrees * 10) / 360
draw_cube(btt,arduino,150,850,150,5)
#rotating 180 degrees
send_to_arduino(arduino,180)
time.sleep(rotating_delay)
draw_cube(btt,arduino,150,850,150)
"""
#btt_command(btt, "G28 X Y Z" + "\r\n")
#btt_command(btt, "M119" + "\r\n")
#btt_command(btt,"G0 Y0\r\n")

btt_command(btt, "G28 X Y Z" + "\r\n")
draw_cube_limits(btt,110, 320, 25,2,5,5)
choice = input("Do you want to continue?:[y/n]")
while True:
    if choice =='y':
        draw_cube(btt,arduino,110,320,25,3,2,5,5)
        degrees = 180
        rotating_delay = (degrees * 10) / 360
        rotating_delay+=3
        send_to_arduino(arduino,str(180))
        time.sleep(rotating_delay)
        draw_cube(btt,arduino,110,320,25,3,2,5,5)
        break
    elif choice == 'n':
        exit(0)
    else:
        print("Wrong Input!")

