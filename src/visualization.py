import os
import pandas as pd
import matplotlib.pyplot as plt


# Load the evaluation metrics from the CSV file
# This file contains MAE, RMSE, MedAE and R2 values
# for each model and prefix length
def load_metrics(csv_path="model_metrics.csv"):
    return pd.read_csv(csv_path)


# Create and save a plot for:
# MAE vs Prefix Length
# Each model will appear as a separate line
def plot_mae_vs_prefix(metrics_df, output_dir="outputs/plots"):

    # Create output directory if it does not already exist
    os.makedirs(output_dir, exist_ok=True)

    # Group rows by model name
    # Example: baseline, ridge, ols
    for model_name, group in metrics_df.groupby("name"):

        # Sort rows by prefix length to ensure correct plotting order
        group = group.sort_values("prefix_length")

        # Plot MAE values against prefix length
        plt.plot(
            group["prefix_length"],
            group["MAE"],
            marker="o",
            label=model_name
        )

    # Add labels and title
    plt.xlabel("Prefix Length")
    plt.ylabel("MAE")
    plt.title("MAE vs Prefix Length")

    # Show model names in legend
    plt.legend()

    # Improve spacing
    plt.tight_layout()

    # Save the plot as PNG
    plt.savefig(
        os.path.join(output_dir, "mae_vs_prefix_length.png")
    )

    # Close the figure after saving
    plt.close()


# Create and save a plot for:
# RMSE vs Prefix Length
# Each model will appear as a separate line
def plot_rmse_vs_prefix(metrics_df, output_dir="outputs/plots"):

    # Create output directory if it does not already exist
    os.makedirs(output_dir, exist_ok=True)

    # Group rows by model name
    for model_name, group in metrics_df.groupby("name"):

        # Sort rows by prefix length
        group = group.sort_values("prefix_length")

        # Plot RMSE values against prefix length
        plt.plot(
            group["prefix_length"],
            group["RMSE"],
            marker="o",
            label=model_name
        )

    # Add labels and title
    plt.xlabel("Prefix Length")
    plt.ylabel("RMSE")
    plt.title("RMSE vs Prefix Length")

    # Show model names in legend
    plt.legend()

    # Improve spacing
    plt.tight_layout()

    # Save the plot as PNG
    plt.savefig(
        os.path.join(output_dir, "rmse_vs_prefix_length.png")
    )

    # Close the figure after saving
    plt.close()


# Main execution block
# This part runs only when visualization.py is executed directly
if __name__ == "__main__":

    # Load the metrics dataframe from CSV
    metrics = load_metrics()

    # Generate MAE plot
    plot_mae_vs_prefix(metrics)

    # Generate RMSE plot
    plot_rmse_vs_prefix(metrics)

    # Print confirmation message
    print("Plots saved to outputs/plots/")
