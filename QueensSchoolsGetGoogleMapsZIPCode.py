# Purpose:
# This code takes a name of a public school in Queens, NY and returns the ZIP code from the resulting JSON data

# More on Google Maps API JSON
# Here is an example of the JSON data that the Google Maps API generates:
# https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyBbe1f_e6F1XtJ1s91KTz6VmgzU1fNRdEI

# Known Bugs:
#   1. The following schools produce an "IndexError: list index out of range error" when querying Google Maps:
#       A.C.E. Academy for Scholars at the Geraldine Ferra
#       P.S. 173 Fresh Meadows
#       P.S. 051
#       M.S. 053 Brian Piccolo
#       Goldie Maple Academy
#       P.S. 144 Col Jeromus Remsen
#       P.S. 228 Early Childhood Magnet School of the Arts
#   2. A ZIP code cannot be found for some schools.
#   3. The CSV Writer sometimes outputs a blank in place of a school name
#   The reason for this error is because Google Maps can't find the school name as it is spelled or written


import googlemaps
import csv

gmaps = googlemaps.Client(key='AIzaSyBbe1f_e6F1XtJ1s91KTz6VmgzU1fNRdEI') #initiate Google Maps

#open a file in the current directory containing a list of all Queens public schools
with open("QueensSchools.txt", encoding = 'utf-8') as inputFile:
    outputFile = open('QueensSchoolsZip.csv','w',newline='') #open an output file for writing
    outputWriter = csv.writer(outputFile) #initiate the CSV writer object
    for schoolName in inputFile: #for each school in the input file
        schoolAddress = schoolName + " Queens, NY" #create a simple address based on the school name and county (Queens)
        geocodeResult = gmaps.geocode(schoolAddress) #generate a geocode result from Google Maps based on the address
        schoolZIPCode = geocodeResult[0]["address_components"][7]["long_name"] #obtain the ZIP code from the geocode result
        print(schoolName + " " + schoolZIPCode) #print the result to the console
        outputWriter.writerow([schoolName,schoolZIPCode]) #write the school name and school ZIP code to the CSV output file
    outputFile.close() #close the file


