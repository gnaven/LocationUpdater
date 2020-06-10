import argparse
import requests
import pandas as pd
import os


class Location():
    
    def __init__(self,emailLoc):
        self.emailLoc = emailLoc
    
    def getLocation(self,place):
        """
        Given a location name it returns the 
        longitude and latititude of the 
        location.
        Uses geonames API assuming that the 
        first entry is the correct one
        implements fuzzy logic accounting for
        any errors
        """
        url = "http://api.geonames.org/searchJSON?q="+place+"&maxRows=10&fuzzy=0.8&username=dimagi&password=dimagi"
        response = requests.get(url)
        unstrcInfo = response.content.decode()
        dictInfo = eval(unstrcInfo)
        
        longitude = float(dictInfo['geonames'][0]['lng'])
        latitude = float(dictInfo['geonames'][0]['lat'])
        
        return longitude,latitude
    
    def createDataSet(self):
        """
        iterates through the email data
        and uses getLocation and makes
        a new dataframe
        """
        
        for i in range(len(self.emailLoc)):
            long, lat = self.getLocation(self.emailLoc[i][2])
            self.emailLoc[i].append(long)
            self.emailLoc[i].append(lat)
        df= pd.DataFrame(self.emailLoc)
        df.columns = ['email','emailSentTime','locationName','longitude','latititude']
        return df
        

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Location Updater')
    parser.add_argument('-inputfile',type=str,default='locations.csv')
    args = parser.parse_args()
    locationFname = args.inputfile
    
    if os.path.exists(locationFname) and 'csv' in locationFname:
        df_loc = pd.read_csv(locationFname)
        test_data = df_loc.values.tolist()
    else:
        
        test_data = [["nick@dimagi.com", '2011-05-19 14:05',  "Dodoma"],
                 ["alex@dimagi.com", '2011-05-22 16:22',  "Lusaka"]]
    
    locationUpdater = Location(test_data)
    df = locationUpdater.createDataSet()
    print(df)
    df.to_csv('updatedLocation.csv')
    
    #Path_Wav = args.clippath
    #Path_Meta = args.meta 
