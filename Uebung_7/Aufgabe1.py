import uvicorn
from fastapi import FastAPI

app = FastAPI()

d = {} 
file = open("PLZO_CSV_LV95.csv", encoding="utf-8") 
next(file) 
 
for line in file: 
    data = line.strip().split(";") 
    gem = data[3]
    plz = data[1] 
    ortschaft = data[0] 
    kanton = data[5] 
    EKoord = data[6]
    NKoord = data[7]
    d[gem] = {  "Gemeinde" : gem,
                "PLZ": plz, 
                "Ortschaft": ortschaft, 
                "Kanton": kanton,
                "Ostkoordinaten": EKoord,
                "Nordkoordinaten": NKoord } 
file.close() 
 
@app.get("/suche") 
async def suche(gem: str): 
    if gem in d: 
        return d[gem] 
    else: 
        return {"error": "not found"}

if __name__ == "__main__": 
    uvicorn.run(app, host="127.0.0.1", port=8000) 

#Eingabe in Browser http://127.0.0.1:8000/suche?gem=cham