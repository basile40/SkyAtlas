import streamlit as st
import folium
from streamlit_folium import st_folium

# We must adjust the path so Streamlit can find our local packages
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from sky_atlas.models.location import Coordinates, Location
from sky_atlas.services.weather_service import WeatherService

# Page Configuration
st.set_page_config(
    page_title="SkyAtlas",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Header
    st.title("🌤️ SkyAtlas Dashboard")
    st.markdown("Interactive weather mapping and live conditions.")
    
    # 1. Setup default location
    toms_river = Location(
        name="Toms River",
        region="NJ",
        country="United States",
        coordinates=Coordinates(latitude=39.9532, longitude=-74.1979)
    )
    
    # Sidebar Controls
    st.sidebar.header("Settings")
    st.sidebar.markdown(f"**Current Target:** {toms_river.name}, {toms_river.region}")
    # (Later, we will add a search box here for geocoding!)

    # 2. Fetch Data
    weather_api = WeatherService()
    current = weather_api.get_current_weather(toms_river.coordinates)

    # 3. Create the Layout Columns
    col_data, col_map = st.columns([1, 2]) # The map column is twice as wide

    with col_data:
        st.subheader("Current Conditions")
        if current:
            # Display visually pleasing metric cards
            icon = "☀️" if current.is_day else "🌙"
            st.metric(label="Condition", value=f"{current.condition_text} {icon}")
            
            # Sub-columns for numerical data
            sub_c1, sub_c2 = st.columns(2)
            sub_c1.metric(label="Temperature", value=f"{current.temperature} °F")
            sub_c2.metric(label="Feels Like", value=f"{current.feels_like} °F")
            
            sub_c3, sub_c4 = st.columns(2)
            sub_c3.metric(label="Wind", value=f"{current.wind_speed} mph")
            sub_c4.metric(label="Humidity", value=f"{current.humidity} %")
        else:
            st.error("Failed to load weather data.")

    with col_map:
        st.subheader("Interactive Radar Map")
        st.markdown("*Map layers and Convective Outlooks coming soon!*")
        
        # Initialize the Folium Map
        m = folium.Map(
            location=[toms_river.coordinates.latitude, toms_river.coordinates.longitude],
            zoom_start=10, 
            tiles="OpenStreetMap" # Updated to a free, keyless map provider
        )
        
        # Add a marker for the target city
        folium.Marker(
            [toms_river.coordinates.latitude, toms_river.coordinates.longitude],
            popup=toms_river.name,
            icon=folium.Icon(color="blue", icon="cloud")
        ).add_to(m)

        # Render map in Streamlit
        st_folium(m, width=700, height=500)

if __name__ == "__main__":
    main()