import krpc
import time
import math


conn = krpc.connect(
    name='Python Scripts',
    address='127.0.0.1')
    # rpc_port=50000, stream_port=50001
# )
# print(conn.krpc.get_status().version)
# print(help(conn.space_center))


#defines and initializations for reference frames
vessel = conn.space_center.active_vessel

surface_frame = vessel.orbit.body.reference_frame
orbit_frame = vessel.orbit.body.non_rotating_reference_frame
orbit_speed = conn.add_stream(getattr, vessel.flight(orbit_frame), 'speed')
surface_speed = conn.add_stream(getattr, vessel.flight(surface_frame), 'speed')
altitude = conn.add_stream(getattr, vessel.flight(), 'surface_altitude')

# # Set this to a function to call so it doesn't have to get commented every time (Launch sequence stuff)

# # Pre-Launch Sequences
# vessel.control.sas = False #sets Stability Assist to "off" position
# vessel.control.rcs = False #Sets Reaction Control to "Off" position
# vessel.control.throttle = 1.0 #Set throttle to full open position

# #Launch Sequence
# vessel.control.activate_next_stage() #Activates next stage - in this case, thruster ignition

# # # Further planning - add ascent automation - this is being handled by MechJeb addon right now for consistency in spaceship placement for landing guidance

# LANDING AUTOPILOT / SUICIDE-BURN
# **NOTE** THIS IS VERY VERY TARGETED FOR THIS SPECIFIC SPACECRAFT UNTIL I FIGURE OUT THE CHECK STATE FOR PERIGEE!

vessel.control.speed_mode = vessel.control.speed_mode.surface
ap = vessel.auto_pilot #sets vessel.auto_pilot to a more manageable variable name for the auto pilot.
ap.sas = True #turn on Stability Assist for rocket
time.sleep(3)
# ap.target_direction = (0, -1, 0) #orient spacecraft near retrograde marker.
ap.sas_mode = ap.sas_mode.retrograde #orient spacecraft Stability Assist for Retrograde marker
time.sleep(15) #waiting 13 seconds because reaction wheels are slow.

# # **NOTE** This is an awful way to handle descent burns, but works for now until I sort out the math or having the computer do the math for proper burn phases / times.

while altitude() > 80000:        
    while orbit_speed() > 1900:
        vessel.control.throttle = 1.0
    vessel.control.throttle = 0.0
    break

# Need to add auto-staging when out of fuel

while altitude() > 65000:
    pass
vessel.control.throttle = 0.0

# stage2_fuel = conn.add_stream(stage_2_resources.amount, 'LiquidFuel')
# if stage2_fuel == 0.0:
#     vessel.control.activate_next_stage() # When stage runs out of fuel, separate stage at decoupler.
#     time.sleep(2) # Wait 2 seconds for separated stage to be far enough away before next stage engine ignition
#     vessel.control.activate_next_stage() # Engine ignition for upper stage.

while altitude() > 50000:
    while orbit_speed() > 1700:
        vessel.control.throttle = 1.0
    vessel.control.throttle = 0.0

while altitude() > 10000:
    vessel.control.throttle = 0.0
    

while altitude() > 5000:
    if vessel.control.legs == False: #check state of langing gear for rockets (rocket legs)
        vessel.control.legs = True #if landing legs were not deployed, deploy them
        # vessel.control.throttle = 0.0
    while surface_speed() > 500:
        vessel.control.throttle = 0.8
    vessel.control.throttle = 0.0

while altitude() > 2000:
    while surface_speed() > 200:
        vessel.control.throttle = 1.0
    vessel.control.throttle = 0.1

while altitude() > 50:
    if surface_speed() > altitude()/5:
        vessel.control.throttle = 0.95
    elif surface_speed() > altitude()/10:
        vessel.control.throttle = 0.1
    elif surface_speed() > altitude()/15:
        vessel.control.throttle = 0.05

while altitude() > 2:
    if surface_speed() > 7:
        vessel.control.throttle = 0.5
    else:
        vessel.control.throttle = 0
vessel.control.throttle = 0



