import streamlit as st

class IoTConnector:
    def get_client(self):
        try:
            from influxdb_client import InfluxDBClient
            return InfluxDBClient(
                url=st.secrets["influxdb"]["url"],
                token=st.secrets["influxdb"]["token"],
                org=st.secrets["influxdb"]["org"]
            )
        except Exception as e:
            # st.warning(f"InfluxDB not configured: {e}")
            return None

    def fetch_live_data(self, generator_id="G1"):
        # بيانات تجريبية ذكية (ستتغير كأنها حية)
        import random
        return {
            "voltage": round(380 + random.uniform(-5,5),1),
            "current": round(250 + random.uniform(-10,10),1),
            "frequency": round(50 + random.uniform(-0.5,0.5),2),
            "oil_pressure": round(4.5 + random.uniform(-0.3,0.3),2),
            "coolant_temp": round(85 + random.uniform(-2,5),1)
        }
