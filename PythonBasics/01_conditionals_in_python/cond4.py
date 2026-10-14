# you're building a smart thermostat alert system
# if the device status is "active", and temp > 35 warn : "Hight temp alert!"
# else temp normal
# if device is off - device is offline

device_status = 'active'
temp = 38

if device_status == 'active':
    if temp > 35:
        print("High Temp alert!")
    else:
        print("Temp is normal")
else:
    print('Device is offline')