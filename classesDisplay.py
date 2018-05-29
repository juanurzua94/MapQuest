#This module implements the various outputs
#of the program. Each output is its own class.


class lat_long:
    def display(self, info):
        '''This function displays the latitudes and longitudes
    of a location.'''
        ltlng = []
        counter = 0
        for x in info:
            if counter == 0:
                y = x['locations']   
                b = y[0]
                c = y[1]
                ltlng.append(b['latLng'])
                ltlng.append(c['latLng'])
                counter += 1
            else:
                y = x['locations']
                z = y[1]
                ltlng.append(z['latLng'])
        latlong = self.adjust_locations(ltlng)
        return latlong
        
        
    def adjust_locations(self, ltlng):
        '''This function determines if the latitude is on the north 
        or south and if the longitude is on the east or west and then prints
        them out for display.'''
        print('LATLONGS')
        ltlng2 = {}
        ltlng2['LATLONG'] = ''
        for x in ltlng:
            lat = x['lat']
            long = x['lng']
            if lat > 0:
                lat = '{0:.2f}{1}'.format(lat, 'N')
            else:
                lat = lat * -1
                lat = '{0:.2f}{1}'.format(lat, 'S')
            if long > 0:
                long = '{0:.2f}{1}'.format(long, 'E')
            else:
                long = long * -1
                long = '{0:.2f}{1}'.format(long, 'W')
            ltlng2['LATLONG'] += str(lat)
            ltlng2['LATLONG'] += ' '
            ltlng2['LATLONG'] += str(long)
            ltlng2['LATLONG'] += '\n'
        return ltlng2
            
        

class steps:
    def display(self, info):
        '''This function displays the directions for the route specified
    by the user.'''
        step = {}
        step['DIRECTIONS'] = ''
        for x in info:
            a = x['legs']
            b = a[0]
            c = b['maneuvers']
            steps = len(c)
            for d in range(steps):
                e = c[d]
                for f in e:
                    if f == 'narrative':
                        string = e[f]
                        step['DIRECTIONS'] += string
                        step['DIRECTIONS'] += '\n'
                        
        return step
    
class total_distance:
    def __init__(self):
        self._totalDistance = 0
    def display(self, info):
        '''This function displays the total distance of the route
    specified by the user.'''
        distance = {}
        distance['TOTALDISTANCE'] = ''
        for y in info:
            for x in y:
                if x == 'distance':
                    self._totalDistance += y[x]
        self._totalDistance = int(self._totalDistance)
        distance['TOTALDISTANCE'] += 'TOTAL DISTANCE: ' + str(self._totalDistance) + ' miles'
        return distance

class total_time:
    def display(self, info):
        '''This function displays the total time to get through the route
        that was specified by the user.'''
        times = []
        time = {}
        time['TOTALTIME'] = ''
        totalSeconds = 0.000000
        for y in info:
            for x in y:
                if x == 'time':
                    a = y[x]
                    totalSeconds += a
                    break
        totalSeconds = totalSeconds/60.000000
        totalSeconds = int(totalSeconds)
        time['TOTALTIME'] += 'TOTAL TIME: ' + str(totalSeconds) + ' minutes'
        return time
        
        
                    

class elevations:
    def display(info):
        '''This function displays the elevation of each location
    specified by the user.'''
        x = info['elevationProfile']
        a = x[0]
        return str(int(a['height']))
        
        
def run_display(dis, info, elevation_info):
    '''This function runs the display of each output the user specified
    by looping through a list of the relevant classes for each display.'''
    information = []
    elevation = {}
    elevation['ELEVATION'] = ''
    for counter in dis:
        if counter == 'ELEVATION':
            print('ELEVATIONS')
            for y in elevation_info:
                 elevation['ELEVATION'] += elevations.display(y)
                 elevation['ELEVATION'] += '\n'
            
        else:
             information.append(counter.display(info))
    information.append(elevation)
    print(information)
    return information
            
               
    
