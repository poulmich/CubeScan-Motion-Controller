import serial
import time



def command(ser, str_command):
    ser.write(str.encode(str_command))
    time.sleep(1)
    while True:
        line = ser.readline()
        print(line)
        if line == b'ok\n':
            break
def draw_yz_cube_surface(Vy,Vz,Oy,Oz,step_y,step_z,delay): #dimensions of the volume and the object and the increments of  y z
    dz = Vz-Oz   #distance that we need to cover
    dy = Vy - Oy
    step_num_y = int(dy/step_y)
    step_num_z = int(dz/step_z)
    y = 0
    z = 0
    if step_num_y!=1:
        for i in range(step_num_y // 2):
            for j in range(step_num_z):
                z += step_z
                command(ser, "G0 Z" + str(z) + "\r\n")
                time.sleep(delay)
            y += step_y
            command(ser, "G0 Y" + str(y) + "\r\n")
            time.sleep(delay)
            print("y increased")
            for k in range(step_num_z):
                z -= step_z
                command(ser, "G0 Z" + str(z) + "\r\n")
                time.sleep(delay)
            y += step_y
            command(ser, "G0 Y" + str(y) + "\r\n")
            time.sleep(delay)
            print("y increased")
            # set yz to zero
        print("finished iterations")
        if step_num_y % 2 == 1:
            for i in range(step_num_z):
                z+=step_z
                command(ser, "G0 Z" + str(z) + "\r\n")
                time.sleep(delay)
            y += step_y
            command(ser, "G0 Y" + str(y) + "\r\n")
            time.sleep(delay)
            #return zero
            z-=dz
            y-=dy
            command(ser, "G0 Z" + str(z) + "\r\n")
            command(ser, "G0 Y" + str(y) + "\r\n")
        elif step_num_y % 2 == 0:
            #return to zero
            y-=dy
            command(ser, "G0 Y" + str(y) + "\r\n")
    else:
        for i in range(step_num_z):
            z+=step_z
            command(ser, "G0 Z" + str(z) + "\r\n")
            time.sleep(delay)
        y += step_y
        command(ser, "G0 Y" + str(y) + "\r\n")
        time.sleep(delay)
        #return to zero
        y -= step_y
        z -= dz
        command(ser, "G0 Z" + str(z) + "\r\n")
        command(ser, "G0 Y" + str(y) + "\r\n")

def draw_cube_limits(Vx, Vy, Vz, Ox, Oy, Oz):
 x = 0
 y = 0
 z = 0

 dz = Vz - Oz
 dy = Vy - Oy
 dx = Vx -Ox

 z += dz
 command(ser, "G0 Z" + str(z) + "\r\n")
 x += dx
 command(ser, "G0 X" + str(x) + "\r\n")
 y += dy
 command(ser, "G0 Y" + str(y) + "\r\n")
 x -= dx
 command(ser, "G0 X" + str(x) + "\r\n")
 y -= dy
 command(ser, "G0 Y" + str(y) + "\r\n")
 z-=dz
 command(ser, "G0 Z" + str(z) + "\r\n")

def draw_cube(Vx, Vy, Vz, Ox, Oy, Oz,step_x, step_y,step_z,delay):
    x = 0
    dx = Vx-Ox
    step_num_x = int(dx/step_x)
    for x in range(step_num_x):
        x += step_x
        draw_yz_cube_surface(Vy, Vz, Oy, Oz, step_y,step_z,delay)
        command(ser,"G0 X"+str(x)+"\r\n")
        time.sleep(delay)
    #return to zero
    x-=dx
    command(ser, "G0 X" + str(x) + "\r\n")


ser = serial.Serial('COM8', 115200)
time.sleep(2)
#command(ser, "G21\r\n")
#command(ser, "M106 S255\r\n") # fan speed full
#command(ser, "M106 S0\r\n") # turn off fan

#command(ser, "G0 Y-10\r\n")

#draw_yz_cube_surface(65,65,5,10,10,10,5)

#draw_yz_cube_surface(35,65,5,5,10,10,5)

#draw_yz_cube_surface(15,65,5,5,10,10,5)

draw_cube(50,65,65,20,5,10,10,10,10,5)

#draw_cube_limits(50,65,65,20,5,10)
