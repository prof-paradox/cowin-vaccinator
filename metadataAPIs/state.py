import requests
from states import States

class State(States):
    """ Fetch district wise data for a particular state """
    
    def __init__(self):
        super().__init__()    
        self._id = -1
        self.name = ""
        self.districts_endpoint = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"
        self.districts = dict()
    
    def get_districts(self):
        states_data = self.get_states()
        if len(states_data) == 0:
            print("Error fetching States. System Exit!")
            exit(0)
            
        print("+" + "-"*48 + "+")
        print("|  ID  |" + " "*18 + "NAME" + " "*19 + "|")
        print("+" + "-"*48 + "+")
        
        for sid in states_data:
            if sid < 10:
                print(f"|   {sid}  | {states_data[sid]}" + (40-len(states_data[sid]))*" " + "|")
            else:
                print(f"|  {sid}  | {states_data[sid]}" + (40-len(states_data[sid]))*" " + "|")
        print("+" + "-"*48 + "+")
        
        try:
            self._id = int(input("Enter your State ID : "))
            if self._id not in range(min(states_data.keys()), max(states_data.keys()) + 1):
                print("Invalid State ID! Do you really live in India?\nSystem Exit!")
                exit(0)
            print(f'\nYou live in {states_data[self._id]}\n')
            
            self.name = states_data[self._id]
            
            resp = requests.get(self.districts_endpoint + str(self._id), headers = self.hdrs)
            if resp.status_code == 200:
                tdist = dict()
                for district in resp.json()['districts']:
                    tdist[district['district_id']] = district['district_name']
                    self.districts = tdist
                return self.districts
            elif resp.status_code >= 400 and resp.status_code < 500:
                print(f"[{resp.status_code}] Error fetching states data. Client request forbidden.")
                return self.districts
            else: 
                print(f"[{resp.status_code}] Error.")
                return self.districts
        except (ValueError, Exception) as err: 
            print(f"Error - {err}. System Exit!")
            exit(0)
            
            