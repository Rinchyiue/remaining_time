from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from config import ARTIFACTS_DIR, FIGURES_DIR

def load_metrics():
    csv_path = Path(ARTIFACTS_DIR) / "model_metrics.csv"
    if not csv_path.exists():
        print(f"Warning: {csv_path} not found. Skipping visualization.")
        return None
    return pd.read_csv(csv_path)

def plot_comparative_metrics(metrics_df):
    """Generates 4 graphs: One per metric, comparing all models."""
    metrics_to_plot = [
        ("MAE", "Mean Absolute Error (Hours)"),
        ("RMSE", "Root Mean Squared Error (Hours)"),
        ("MedAE", "Median Absolute Error (Hours)"),
        ("R2", "R² Score")
    ]

    for metric, ylabel in metrics_to_plot:
        plt.figure(figsize=(10, 5))
        for model_name, group in metrics_df.groupby("name"):
            group = group.sort_values("prefix_length")
            plt.plot(group["prefix_length"], group[metric], marker="o", label=model_name)
        
        plt.title(f"Comparison: {metric} across Models")
        plt.xlabel("Prefix Length")
        plt.ylabel(ylabel)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.savefig(Path(FIGURES_DIR) / f"compare_{metric.lower()}.png")

def plot_individual_model_profiles(metrics_df):
    """Generates 3 graphs: One per model, showing all 4 metrics at once."""
    for model_name, group in metrics_df.groupby("name"):
        group = group.sort_values("prefix_length")
        
        fig, ax1 = plt.subplots(figsize=(10, 5))

        ax1.set_xlabel("Prefix Length")
        ax1.set_ylabel("Error (Hours)", color='tab:red')
        ax1.plot(group["prefix_length"], group["MAE"], marker="s", label="MAE", color='tab:red')
        ax1.plot(group["prefix_length"], group["RMSE"], marker="^", label="RMSE", color='tab:orange')
        ax1.plot(group["prefix_length"], group["MedAE"], marker="d", label="MedAE", color='tab:brown')
        ax1.tick_params(axis='y', labelcolor='tab:red')

        ax2 = ax1.twinx()
        ax2.set_ylabel("R² Score", color='tab:blue')
        ax2.plot(group["prefix_length"], group["R2"], marker="o", label="R2 Score", color='tab:blue', linestyle='--')
        ax2.tick_params(axis='y', labelcolor='tab:blue')
        ax2.set_ylim(-0.1, 1.1)

        plt.title(f"Performance Profile: {model_name}")
        fig.tight_layout()
        
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='center right')
        
        plt.savefig(Path(FIGURES_DIR) / f"profile_{model_name}.png")

def run_all_visualizations():
    print("\n--- Phase 4: Generating and Presenting Visualizations ---")
    metrics_df = load_metrics()
    if metrics_df is None:
        return

    plot_comparative_metrics(metrics_df)
    plot_individual_model_profiles(metrics_df)

    print(f" --- 7 Graphs saved to {FIGURES_DIR} --- ")
    print(" --- Presentation mode: Closing a window will open the next one --- ")
    
    plt.show()

if __name__ == "__main__":
    run_all_visualizations()