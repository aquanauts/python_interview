from interview import weather
import io


def test_process_csv():
    reader = io.StringIO("Station Name,Measurement Timestamp,Air Temperature\n"
                         "Foster Weather Station,12/31/2016 11:00:00 PM,-1.56\n"
                         "63rd Street Weather Station,12/31/2016 11:00:00 PM,-1.3\n")
    writer = io.StringIO()
    weather.process_csv(reader, writer)
