import unittest
from main import app, process_data

class TestFlightDataFunctions(unittest.TestCase):

    def test_process_data(self):
        schedules = [{'OperatingCarrier': {'AirlineID': 'XX', 'FlightNumber': '123'}, 'Departure': {'ActualTimeUTC': {'DateTime': '2023-01-01T10:00Z'}, 'AirportCode': 'ABC', 'ScheduledTimeUTC': {'DateTime': '2023-01-01T09:30Z'}, 'TimeStatus': {'Definition': 'Delayed'}}, 'Arrival': {'AirportCode': 'DEF'}}]
        delays = [{'Flight': {'OperatingFlight': {'flightCode': 'XX123'}}, 'FlightLegs': [{'Departure': {'ActualDepartureTime': '2023-01-01T10:00:00Z', 'Delay': {"Code1" : {'Code': 'ATC', 'DelayTime': 30, 'Description': 'Air traffic control delay'}}}}]}]
        processed = process_data(schedules, delays)
        print(processed)
        self.assertEqual(len(processed), 1)
        self.assertEqual(processed[0]['delays'][0]['code'], 'ATC')

class TestFlaskRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_flights_no_params(self):
        response = self.client.get('/flights')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_flights_with_params(self):
        response = self.client.get('/flights?destination=DEF&airlines=XY')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(all(flight['destination'] == 'DEF' and flight['airline'] == 'XY' for flight in data))

if __name__ == '__main__':
    unittest.main()
