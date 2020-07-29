import csv
import datetime
class covid_19(object):
    def __init__(self, state, country, lat, long, dates ):
        self.state = state
        self.country = country
        self.lat = lat
        self.long = long
        self.dates = dates

def reader1(path_name_csv):
    with open(path_name_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_data = []
        for row in csv_reader:
            state , country , lat , long, dates = '','','','',[]
            for idx,col in enumerate(row):
                if idx is 0:
                    state = col
                elif idx is 1:
                    country = col
                elif idx is 2:
                    lat = col
                elif idx is 3:
                    long = col
                else:
                    dates.append(col)
            list_data.append(covid_19(state , country , lat , long, dates))
    return list_data


def reader2(path_name_csv):
    with open(path_name_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_data = []
        state , country , lat , long, dates = '','','','',[]
        for idx,col in enumerate(csv_reader):#112 dates
            if col[3] == '2020-01-01':
                state=col[2]
                country=col[1]
                lat=col[42]
                long=col[43]
            if col[3] != '2019-12-31' and idx !=0:
                avg=(float(col[14])+float(col[16]))/2
                Classification = 1 if avg>72 else -1
                dates.append([col[3],Classification])
            if col[3] == '2020-04-20':
                list_data.append(covid_19(state , country , lat , long, dates))
                state , country , lat , long, dates = '','','','',[]
    return list_data

class covid_19_cf(object):
    def __init__(self, country,cf ):
        self.country = country
        self.cf = cf

def parser():
    list_deaths = reader1('dataset/covid_19_deaths.csv')
    list_confirmed = reader1('dataset/covid_19_confirmed.csv')
    list_weather = reader2('dataset/daily_weather_2020.csv')
    list_data=[]
    for i,d in enumerate(list_deaths):
        for w in list_weather:
            temp_d,temp_c,temp_w=[],[],[]
            if w.lat == d.lat and w.long == d.long:
                for j,x in enumerate(d.dates):
                    if j < len(d.dates)-63:
                        temp_d.append(d.dates[j])
                        temp_c.append(list_confirmed[i].dates[j])
                for j,x in enumerate(w.dates):
                    if j > 20:
                        temp_w.append(w.dates[j][1])
                temp_d,temp_c=per_day(temp_d,temp_c)
                temp_d,temp_c,temp_w=temp_d[45:],temp_c[45:],temp_w[45:]
                list_data.append(covid_19_cf(d.country ,list(zip(temp_d,temp_c,temp_w))))
    return list_data

def per_day(temp_d,temp_c):
    floats_d = [float(item) for item in temp_d]
    floats_c = [float(item) for item in temp_c]
    temp_d=[y - x for x, y in zip(floats_d, floats_d[1:])]
    temp_c=[y - x for x, y in zip(floats_c, floats_c[1:])]
    return temp_d,temp_c

def writer(list_data):
    with open('dataset/corona.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i,x in enumerate(list_data):
            for j,y in enumerate(x.cf):
                writer.writerow([y[0],y[1],y[2]])

# def main():
#     writer(parser())
# if __name__== "__main__":
#   main()
