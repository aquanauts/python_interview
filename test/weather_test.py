from interview import weather
import io

def test_has_a_friendly_greeting():
    writer = io.StringIO()
    weather.process_csv(None, writer)
    assert writer.getvalue() == "Hello World\n"
    
