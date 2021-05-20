import requests

class States:
    """ Fetches all the states in India along with their unique identifier """
    
    states_endpoint = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    
    def __init__(self):
        self.states = dict()
        self.hdrs = requests.structures.CaseInsensitiveDict()
        self.hdrs["accept"] = "application/json"
        self.hdrs["Accept-Language"] = "en_US"    
        self.hdrs["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"
        
    
    def get_states(self):
        resp = requests.get(self.states_endpoint, headers = self.hdrs)
        if resp.status_code == 200:
            for state in resp.json()['states']:
                self.states[state['state_id']] = state['state_name']     
            return self.states
        elif resp.status_code >= 400 and resp.status_code < 500:
            print(f"[{resp.status_code}] Error fetching states data. Client request forbidden.")
            return self.states
        else: 
            print(f"[{resp.status_code}] Error.")
            return self.states
    