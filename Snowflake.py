import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (0, 128, 255)
y = 400
x = 100
y2 = 350
x2 = 150
while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=45)
    y -= 10
    if y < 50:
       break
    x = x + 10

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=25)
    y2 -= 10
    if y2 < 50:
       break
    x2 = x2 + 20

    sd.sleep(0.05)
    if sd.user_want_exit():
        break
