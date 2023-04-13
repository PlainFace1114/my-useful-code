import screeninfo

# get the current screen configuration
screens = screeninfo.get_monitors()

# print the resolution of each screen
for screen in screens:
    print(f"Screen {screen.name}: {screen.width} x {screen.height}")
