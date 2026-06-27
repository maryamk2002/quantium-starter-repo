from app import app  # Import your actual Dash instance from app.py

def test_header_present(dash_duo):
    # 1. Start the local server with the app loaded
    dash_duo.start_server(app)
    
    header_element = dash_duo.wait_for_element("h1")
    
    # 3. Assert its content or presence matches expectations
    assert header_element.text == "Pink Morsel Visualiser"

def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    
    # Select by the exact ID you specified in dcc.Graph(id="...")
    graph_element = dash_duo.wait_for_element("#sales-line-chart")
    
    assert graph_element is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    
    # Select by the ID assigned to your dcc.RadioItems
    picker_element = dash_duo.wait_for_element("#region-filter")
    
    assert picker_element is not None