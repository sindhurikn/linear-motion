import sys
import math

print "Let's do linear motion!"
print "==\nLet's lay down some ground rules first:"
print "1. All units are assumed to be in the SI system."
print "2. Because we make this assumption, do not specify the units while entering values."
print "3. Needless to say, the answers you'll get will be in SI units as well."
print "==\nOkay, let's begin!"
print "Tell me what you know (just hit enter where you don't know it)"
distance = raw_input ("Distance? ")
distance = distance.rstrip()
initial_speed = raw_input("Initial Speed? ")
initial_speed = initial_speed.rstrip()
final_speed = raw_input("Final Speed? ")
final_speed = final_speed.rstrip()
average_speed = raw_input("Average Speed? ")
average_speed = average_speed.rstrip()
accln = raw_input("Acceleration? ")
accln = accln.rstrip()
time = raw_input("Time taken? ")
time = time.rstrip()

calc_distance = distance if distance != '' else None
calc_ispeed = initial_speed if initial_speed != '' else None
calc_fspeed = final_speed if final_speed != '' else None
calc_aspeed = average_speed if average_speed != '' else None
calc_accln = accln if accln != '' else None
calc_time = time if time != '' else None

def find_distance():
# s = avg v * t
# s = ut + (0.5*a*t^2)
# s = (v^2 - u^2)/(2a)
# s = (v + u)t/(2)
    global calc_distance; global calc_ispeed; global calc_fspeed; global calc_aspeed; global calc_accln; global calc_time;
    if calc_distance is None:
        if calc_aspeed and calc_time:
            calc_distance = float(calc_aspeed) * float(calc_time)
        elif calc_ispeed and calc_time and calc_accln:
            calc_distance = (float(calc_ispeed) * float(calc_time)) + (0.5 * float(calc_accln) * float(calc_time)^2)
        elif calc_fspeed and calc_ispeed and calc_accln and float(calc_accln) != 0:
            calc_distance = (float(calc_fspeed)^2 - float(calc_ispeed)^2) / (2 * float(calc_accln))
        elif calc_ispeed and calc_fspeed and calc_time:
            calc_aspeed = (float(calc_ispeed) + float(calc_final_speed)) / 2
            calc_distance = float(calc_aspeed) * float(calc_time)
    if calc_distance is None:
        return "I couldn't find the distance :( Please teach me if you know how to."
    else:
        return str(calc_distance)+' m'

def find_ispeed():
# u = v - at
# u = 2*(avg v) - v
# u = (s - (0.5 * a * t^2) ) / t
# u = root (v^2 - 2as)
    global calc_distance; global calc_ispeed; global calc_fspeed; global calc_aspeed; global calc_accln; global calc_time;
    if calc_ispeed is None:
        if calc_fspeed and calc_accln and calc_time:
            calc_ispeed = float(calc_fspeed) - (float(calc_accln) * float(calc_time))
        elif calc_aspeed and calc_fspeed:
            calc_ispeed = 2 * (float(calc_aspeed)) - float(calc_fspeed)
        elif calc_distance and calc_accln and calc_time and float(calc_time) != 0:
            calc_ispeed = (float(calc_distance) - (0.5 * float(calc_accln) * float(calc_distance))) / float(calc_time)
        elif calc_fspeed and calc_accln and calc_distance: 
            calc_ispeed = math.sqrt( float(calc_fspeed)^2 - (2 * float(calc_accln) * float(calc_distance)))
    if calc_ispeed is None:
        return "I couldn't find the initial speed :( Please teach me if you know how to."
    else:
        return str(calc_ispeed)+' m/s'

def find_fspeed():
# v = u + at
# v = root (u^2 + 2as)
# v = 2(avg v) - u
    global calc_distance; global calc_ispeed; global calc_fspeed; global calc_aspeed; global calc_accln; global calc_time;
    if calc_fspeed is None:
        if calc_ispeed and calc_accln and calc_time:
            calc_fspeed = float(calc_ispeed) + (float(calc_accln) * float(calc_time))
        elif calc_ispeed and calc_accln and calc_distance:
            calc_fspeed = math.sqrt(float(calc_ispeed)^2 + 2*(float(calc_accln)*float(calc_distance)))
        elif calc_aspeed and calc_ispeed:
            calc_fspeed = (2 * float(calc_aspeed)) - float(calc_ispeed)
    if calc_fspeed is None:
        return "I couldn't find the final speed :( Please teach me if you know how to."
    else:
        return str(calc_fspeed)+' m/s'

def find_aspeed():
# avg v = (u+v)/2
# avg v = distance/time
    global calc_distance; global calc_ispeed; global calc_fspeed; global calc_aspeed; global calc_accln; global calc_time;
    if calc_aspeed is None:
        if calc_ispeed and calc_fspeed:
            calc_aspeed = (float(calc_ispeed) + float(calc_fspeed)) / 2
        elif calc_distance and calc_time:
            calc_aspeed = float(calc_distance) / float(calc_time)
    if calc_aspeed is None:
        return "I couldn't find the average speed :( Please teach me if you know how to."
    else:
        return str(calc_aspeed)+' m/s'

def find_accln():
# a = (v-u)/t
# a = (v^2 - u^2) * 2s
    global calc_distance; global calc_ispeed; global calc_fspeed; global calc_aspeed; global calc_accln; global calc_time;
    if calc_accln is None:
        if calc_ispeed and calc_fspeed and calc_time and float(calc_time) != 0:
            calc_accln = (float(calc_fspeed) - float(calc_ispeed)) / float(calc_time)
        elif calc_ispeed and calc_fspeed and calc_distance:
            calc_accln = (float(calc_fspeed)^2 - float(calc_ispeed)^2) * 2 * float(calc_distance)
    if calc_accln is None:
        return "I couldn't find the acceleration :( Please teach me if you know how to."
    else:
        return str(calc_accln)+' ms^-2'

def find_time():
# t = d /avg v
# t = (v-u) / a
# t = solve a quadratic eqn => s = ut + (1/2)at^2 => solve for t
    global calc_distance; global calc_ispeed; global calc_fspeed; global calc_aspeed; global calc_accln; global calc_time;
    if calc_time is None:
        if calc_distance and calc_aspeed and float(calc_aspeed) != 0:
            calc_time = float(calc_distance) / float(calc_aspeed)
        elif calc_fspeed and calc_ispeed and calc_accln and float(calc_accln) != 0:
            calc_time = (float(calc_fspeed) - float(calc_ispeed)) / float(calc_accln)
        elif calc_ispeed and calc_fspeed and calc_ispeed == calc_fspeed and calc_distance and float(calc_ispeed) != 0:
            calc_time = float(calc_distance) / float(calc_ispeed)
        elif calc_ispeed and calc_distance and calc_accln:
            return "solve a quadratic eqn here"
    if calc_time is None:
        return "I couldn't find the time :( Please teach me if you know how to."
    else:
        return str(calc_time)+' s'

def clean_exit():
    print "Hope you had fun, see you soon!"
    sys.exit()

choice_dict = { 1: find_distance,
                 2: find_ispeed,
                 3: find_fspeed,
                 4: find_aspeed,
                 5: find_accln,
                 6: find_time,
                 7: clean_exit,
}

while(1):
    print "==\nWhat do you want to find out?"
    print "1. Distance"
    print "2. Initial Speed"
    print "3. Final Speed"
    print "4. Average Speed"
    print "5. Acceleration"
    print "6. Time taken"
    print "7. Quit"
    choice = raw_input("==\nSo what will it be? ")
    choice = int(choice.rstrip())

    try:
#        print "choice is",choice, type(choice)
#        print "choice points to",choice_dict[choice]
        print choice_dict[choice]()
    except Exception as e:
        print e
        print "==\nDid you enter the choice number correctly?"
        print "Are you sure you can find what you need to with the info you just gave me?"
        print "Try again"
