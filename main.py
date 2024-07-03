import requests

#1. Fetch data from the API
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

flight_schedules_all_data = fetch_data("https://challenge.usecosmos.cloud/flight_schedules.json")
flight_schedules_flight_data = flight_schedules_all_data['FlightStatusResource']['Flights']['Flight']

flight_delays_flight_data = fetch_data("https://challenge.usecosmos.cloud/flight_delays.json")


#2. Processing the data
def process_data(schedules, delays):
    flights = {}
    for schedule in schedules:
        flight_id = schedule['OperatingCarrier']['AirlineID'] + schedule['OperatingCarrier']['FlightNumber'] + schedule['Departure']['ActualTimeUTC']['DateTime']
        print(flight_id)
        flights[flight_id] = {
            "id": flight_id,
            "flight_number": schedule['OperatingCarrier']['FlightNumber'],
            "airline": schedule['OperatingCarrier']['AirlineID'],
            "origin": schedule['Departure']['AirportCode'],
            "destination": schedule['Arrival']['AirportCode'],
            "scheduled_departure_at": schedule['Departure']['ScheduledTimeUTC']['DateTime'],
            "actual_departure_at": schedule['Departure']['ActualTimeUTC']['DateTime'],
            "delays": []
        }
    
    for delay in delays:
        flight_id = delay['Flight']['OperatingFlight']['flightCode'] + delay['FlightLegs'][0]['Departure']['ActualDepartureTime'][:-4] + "Z"
        delay_details = delay["FlightLegs"][0]['Departure']['Delay']
        if flight_id in flights:
            for key, value in delay_details.items():
                print(delay_details)
                if (value is not None):
                    flights[flight_id]['delays'].append({
                        "code": delay_details[key]['Code'],
                        "time_minutes": delay_details[key]['DelayTime'],
                        "description": delay_details[key]['Description']
                    })
    
    return list(flights.values())
    
processed_flights = process_data(flight_schedules_flight_data, flight_delays_flight_data)
print(processed_flights)


#3 API Design
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/flights', methods=['GET'])
# def get_flights():
#     destination = request.args.get('destination')
#     airlines = request.args.getlist('airlines')
#     result = processed_flights
    
#     if destination:
#         result = [flight for flight in result if flight['destination'] == destination]
    
#     if airlines:
#         result = [flight for flight in result if flight['airline'] in airlines]
    
#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)
