"""Plotting utilities for forecast verification results."""

import matplotlib.pyplot as plt
import pandas as pd

from src.database import get_connection


def plot_forecast_vs_observed(location_id: str) -> None:
    """Plot matched forecast and observed temperatures.

    Parameters
    ----------
    location_id : str
        Configured location identifier.
        
    Returns
    -------
    None
    """
    with get_connection() as connection:
        data = pd.read_sql_query(
            """
            SELECT valid_time, forecast_temperature_f, observed_temperature_f
            FROM verification_results
            WHERE location_id = ?
            ORDER BY valid_time
            """,
            connection,
            params=(location_id,),
        )
        
    if data.empty:
        print("No verification results available to plot.")
        return
    
    data["valid_time"] = pd.to_datetime(data["valid_time"])
    
    plt.figure(figsize=(10, 6))
    plt.plot(data["valid_time"], data["forecast_temperature_f"], label="Forecast")
    plt.plot(data["valid_time"], data["observed_temperature_f"], label="Observed")
    plt.xlabel("Valid Time")
    plt.ylabel("Temperature (°F)")
    plt.title(f"Forecast vs Observed Temperature: {location_id}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    output_path = f"dashboard/{location_id}_forecast_vs_observed.png"
    plt.savefig(output_path, dpi=150)
    print(f"Saved plot: {output_path}")
    
    
if __name__ == "__main__":
    plot_forecast_vs_observed("central_kansas_test")