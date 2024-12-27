speed = 69
car_Location = 99

SPEED_RADAR_BR = 60
RADAR_LOCATION = 100
RADAR_RANGE = 1

speed_car_go_to_Radar_br = speed > SPEED_RADAR_BR

car_went_radar_br = car_Location >= (RADAR_LOCATION - RADAR_RANGE) and \
                        car_Location <=  (RADAR_LOCATION + RADAR_RANGE)

car_fined_radar_br = speed_car_go_to_Radar_br and car_went_radar_br

if speed_car_go_to_Radar_br:
    print("speed of the car pass on radar BR")

if car_went_radar_br:
    print("car pass on radar BR")

if car_fined_radar_br:
    print("speed of the car fined on radar BR")