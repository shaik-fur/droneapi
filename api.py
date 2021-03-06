
from fastapi import FastAPI
from geolocation import Address, GeoLoc, distance, polyzone, df2


app = FastAPI()

'''http://127.0.0.1:8000/API'''
'''Address format source='potheri,chennai,India'
dest='guindy,chennai,India' '''

@app.post("/API")
def read(source, dest):
    d1 = source.split(",")
    d2 = dest.split(",")
    loc1 = Address(area=d1[0], city=d1[1], country=d1[2])
    loc2 = Address(area=d2[0], city=d2[1], country=d2[2])
    if(loc1.coord() is None or loc2.coord() is None):
        if loc1.coord() is None:
           return {"Error":"Source Address is Invalid"}
        else:
            return {"Error": "Destination Address is Invalid"}
    else:
        geo = GeoLoc(loc1.coord().latitude, loc1.coord().longitude)
        geo2 = GeoLoc(loc2.coord().latitude, loc2.coord().longitude)
        points = [(geo.lat, geo.long), (geo2.lat, geo2.long)]
        polyzones = polyzone()
        return {"points": points, "weather1": geo.weather(), "weather2": geo2.weather(),
                "distance": distance((geo.lat, geo.long), (geo2.lat, geo2.long)).kilometers,
                "Polygonal orange zones": polyzones[0], "Polygonal red zones": polyzones[1]}