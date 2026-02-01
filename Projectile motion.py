import numpy as np
import matplotlib.pyplot as plt

u_y = int(input("Enter the initial velocity along the y-axis: "))
u_x = int(input("Enter the initial velocity along the x-axis: "))
g = 10 # m/s**2

delta_t = 0.01

vel_y = np.array([])
time = np.array([])
v = u_y
t = 0
while v > (-1)*(u_y):
    vel_y = np.append(vel_y , v)
    time  = np.append(time , t)
    v = v - g*(delta_t)
    t = t + delta_t

# for distance
y_dis = np.array([])
y = 0
for i in range(0 , len(vel_y)):
    y_dis = np.append(y_dis , y)
    y = y + delta_t*(vel_y[i])

x_dis = np.array([])
x= 0
for i in range(0 , len(y_dis)):
    x_dis = np.append(x_dis , x)
    x = x + (delta_t)*(u_x)

plt.scatter(x_dis , y_dis  , s=10, alpha=0.1 , label = "Without Drag")
# plt.show()
 

# including drag force along x axis

x_drag = np.array([])

x = 0
for i in range(0 , len(y_dis)):
    if i == 0:
        x = 0
        x_drag = np.append(x_drag , x)
    elif i == 1:
        x = u_x*(delta_t)
        x_drag = np.append(x_drag , x)
    else:
        x = 2*(x_drag[i-1]) - x_drag[i-2] - 1.2*(1e-3)*((x_drag[i-1] - x_drag[i-2])**2) #Drag constant along the x-axis is taken to be 1.2*(1e-3)
        x_drag = np.append(x_drag , x)

plt.scatter(x_drag , y_dis , s=10, alpha=0.5 , label = "With Drag along x axis only")
plt.legend()
# plt.show()

# including drag force along both the axis
v = u_y
# for y_1
y_drag = np.array([ 0 , v*(delta_t)])
y = v*(delta_t)

i =2

while y > 0:
    y = 2*(y_drag[i-1]) - y_drag[i-2] - 1.2*(10**(-3))*(y_drag[i-1] - y_drag[i-2])**(2) -(10)*((delta_t)**2)  #Drag constant along the y-axis is taken to be 1.2*(1e-3)
    y_drag = np.append(y_drag , y)
    i = i + 1

x_drag2 = np.array([])

x = 0
for i in range(0 , len(y_drag)):
    if i == 0:
        x = 0
        x_drag2 = np.append(x_drag2 , x)
    elif i == 1:
        x = u_x*(delta_t)
        x_drag2 = np.append(x_drag2 , x)
    else:
        x = 2*(x_drag2[i-1]) - x_drag2[i-2] - 1.2*(10**(-3))*((x_drag2[i-1] - x_drag2[i-2])**2) #Drag constant along the x-axis is taken to be 1.2*(1e-3)
        x_drag2 = np.append(x_drag2 , x)
# print(y_drag)

angle = np.arctan2(u_y, u_x) * 180/np.pi
v0 = np.sqrt(u_x**2 + u_y**2)

plt.scatter(x_drag2 , y_drag ,  s=10, alpha=0.5 , label = "With Drag along x and y axis only" )

plt.text(
    0.98, 0.95,
    f"The initial velocity is {v0:.3f} m/s\nAngle = {angle:.3f}°",
    transform=plt.gca().transAxes,
    fontsize=10,
    ha='right',
    va='top',
    bbox=dict(facecolor='yellow', alpha=0.4)
)
plt.legend()
plt.show()
