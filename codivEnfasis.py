import pandas as pd
import matplotlib.pyplot as plt
import requests

class CovidDataService:
    def get_countries_data(self):
        pass
    def get_countries_historic_data(self):
        pass

class CovidDataJsonService(CovidDataService):

    def __init__(self):
        self.base_url = "https://api.covid19api.com"

    def get_countries_data(self, countries):
        data = {}
        for country in countries:
            response = requests.get(f"{self.base_url}/total/country/{country}")
            if response.status_code == 200:
                data[country] = response.json()
        return data

    def get_countries_historic_data(self, countries, start_date, end_date):
        data = {}
        for country in countries:
            response = requests.get(
                f"{self.base_url}/country/{country}?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z")
            if response.status_code == 200:
                data[country] = response.json()
        return data

class CSVAdapter(CovidDataService):

    def __init__(self, json_service):
        self.json_service = json_service

    def json_to_csv(self, data):
        csv_data = []
        for key, value in data.items():
            for item in value:
                item["Country"] = key
                csv_data.append(item)
        return csv_data

    def get_countries_data(self, countries):
        json_data = self.json_service.get_countries_data(countries)
        csv_data = self.json_to_csv(json_data)
        return csv_data

    def get_countries_historic_data(self, countries, start_date, end_date):
        json_data = self.json_service.get_countries_historic_data(
            countries, start_date, end_date)
        csv_data = self.json_to_csv(json_data)
        return csv_data


class CSVPlotter:

    def plot_data(self, csv_data):
        df = pd.DataFrame(csv_data)
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index(["Country", "Date"], inplace=True)
        df = df[["Confirmed", "Deaths", "Recovered"]]
        df = df.unstack("Country")
        df.plot(kind="line", subplots=True, layout=(3, 3), figsize=(10, 10))
        plt.show()

def main():
    # Crear instancia del servicio de datos
    json_service = CovidDataJsonService()

    # Crear adaptador de datos CSV
    csv_adapter = CSVAdapter(json_service)

    # Obtener datos en formato CSV
    countries = ["colombia", "argentina", "peru", "mexico"]
    start_date = "2020-01-01"
    end_date = "2022-04-30"
    csv_data = csv_adapter.get_countries_historic_data(countries, start_date, end_date)
    # print(csv_data)

    # Graficar datos
    plotter = CSVPlotter()
    plotter.plot_data(csv_data)

main()