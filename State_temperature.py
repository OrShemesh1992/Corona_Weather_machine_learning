from weatherbit.api import Api
from datetime import timedelta
import datetime

def weather(lat,lon,date):
    dt=datetime.datetime.strptime(date, '%m/%d/%y').strftime('20%y-%m-%d')
    dt1=(datetime.datetime.strptime(date, '%m/%d/%y')+ timedelta(days=1)).strftime('20%y-%m-%d')
    api_key = "b2dbf04ebf96490cbe539aefcd3ee381"
    api = Api(api_key)
    api.set_granularity('daily')
    history = api.get_history(lat=lat, lon=lon, start_date=dt,end_date=dt1)
    temperature=list(history.get_series('temp')[0].items())[0][1]
    return 1 if temperature>18 else -1 # -1 cool 1 hot on 00:00->18c

def main():
    print(weather(34.235,32.9253,'1/22/20'))
if __name__== "__main__":
  main()
