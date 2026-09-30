"""Run the public analysis pipeline in dependency order."""
from step01_clean_harvest import main as clean_harvest
from step02_reshape_join import main as reshape_join
from step03_descriptive_yield import main as descriptive
from step04_growth_summary import main as growth
from step05_exploratory_factorial import main as exploratory
from step06_figures import main as figures


if __name__ == "__main__":
    clean_harvest()
    reshape_join()
    descriptive()
    growth()
    exploratory()
    figures()
    print("Reproduced clean data, derived tables, analysis outputs, and figures.")
