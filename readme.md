# Análisis de datos COVID-19

Este es un proyecto que utiliza los datos de COVID-19 proporcionados por la API de [covid19api.com](https://covid19api.com/). El objetivo es obtener los datos históricos de casos confirmados, muertes y recuperaciones para varios países y graficarlos en un gráfico de línea.

## Requisitos

* Python 3.x
* Pandas
* Matplotlib
* Requests

## Estructura del proyecto

El proyecto consta de los siguientes archivos:

* `main.py`: Este es el archivo principal que se encarga de ejecutar el código y llamar a las otras clases y funciones.
* `CovidDataService`: Este clase define la interfaz  `CovidDataService`, que define los métodos necesarios para obtener los datos de COVID-19.
* `CovidDataJsonService`: Este clase implementa la interfaz `CovidDataService` y utiliza la API de `covid19api.com` para obtener los datos de COVID-19 en formato JSON.
* `CSVAdapter`: Esta clase se encarga de convertir los datos en formato JSON a formato CSV.
* `CSVPLOTTER`: Esta clase se encarga de graficar los datos en formato CSV utilizando `pandas` y `matplotlib`.
