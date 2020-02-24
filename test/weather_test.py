from interview import weather
import io


def test_replace_me():
    reader = io.StringIO("Line One\nLine Two\n")
    writer = io.StringIO()
    weather.process_csv(reader, writer)
    assert writer.getvalue() == "Saw 2 lines\n"
