#This module reads the input and constructs the objects
#that will generate the program's output.
import classesDisplay
import URLjson


def begin():
    '''This function is what begins the program by recieving the input
    from the user and calling the necessary functions to deliver the
    output.'''
    action = eval(input())
    if action > 1:
        locations = enter_locations(action)
    next_action = eval(input())
    if next_action > 0:
        outputs = enter_outputs(next_action)
    classes = determine_outputs(outputs)
    get_info(locations, classes)        
        

def enter_locations(num):
    '''This function recieves the locations from the user.'''
    locations = []
    for counter in range(num):
        loc = input()
        locations.append(loc)
    return locations

def enter_outputs(num):
    '''This function recieves the desired outputs to display from the
    user.'''
    outputs = []
    for counter in range(num):
        output = input()
        outputs.append(output)
    return outputs


def determine_outputs(output):
    '''This function determines which outputs the user wants
    the program to display.'''
    classes = []
    for x in output:
        if x == 'LATLONG':
            x = classesDisplay.lat_long()
            classes.append(x)
        if x == 'STEPS':
            y = classesDisplay.steps()
            classes.append(y)
        if x == 'TOTALDISTANCE':
            c = classesDisplay.total_distance()
            classes.append(c)
        if x == 'TOTALTIME':
            a = classesDisplay.total_time()
            classes.append(a)
        if x == 'ELEVATION':
            classes.append('ELEVATION')
    return classes


def get_info(locations, classes):
    '''This function recieves the dictionarys containing
    the information that is relevant to the route that the user
    inputted.'''
    info = []
    elevation_info = []
    elevations = False
    for counter in range(len(locations) -1):
        a = URLjson.complete_url(locations[counter], locations[counter + 1])
        info.append(a['route'])
    if 'ELEVATION' in classes:
        elevations = True
    if elevations == True:
        ltlng = get_ltlng_for_elevation(info)
        counter = 0
        counter1 = 1
        while True:
            b = URLjson.complete_elevation_url(ltlng[counter], ltlng[counter1])
            elevation_info.append(b)
            counter += 2
            counter1 += 2
            if counter1 > len(ltlng):
                break
    
    display(info, classes, elevation_info)
    
def display(info, classes, elevation_info):
    '''This function displays the outputs by calling a function from the
    module classes.'''
    classesDisplay.run_display(classes, info, elevation_info)
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

    

def get_ltlng_for_elevation(locations):
    '''This function recieves the latitude and longitude
    for the elevaiton profile API provided by MapQuest.'''
    ltlng = []
    ltlng3 = []
    counter = 0
    for x in locations:
        if counter == 0:
            y = x['locations']
            z = y[0]
            w = y[1]
            ltlng.append(z['latLng'])
            ltlng.append(w['latLng'])
            counter += 1
        else:
            y = x['locations']
            z = y[1]
            ltlng.append(z['latLng'])
            
    for a in ltlng:
        ltlng3.append(a['lat'])
        ltlng3.append(a['lng'])
    return ltlng3
    



if __name__ == '__main__':
    begin()
