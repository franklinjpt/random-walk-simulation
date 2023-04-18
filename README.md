# Random Walk Simulation
This Python code simulates a random walk, which is a mathematical concept used in probability theory and statistics to model random events. A random walk is a process where a particle moves randomly, taking steps in a random direction at each time step.

In this particular code, we simulate 500 random walks, each consisting of 100 steps. The steps are determined by the outcome of rolling a dice, with certain rules for different outcomes.

At the end of each random walk, we record the final position of the particle. We then plot a histogram of these final positions to visualize the distribution of outcomes. Finally, we calculate the probability of the particle ending up 60 or more steps away from the starting point.

## Dependencies
- numpy
- matplotlib

## Usage
1. Install the dependencies using pip or conda:
```sh
pip install numpy matplotlib
```
2. Copy and paste the code into a Python environment (e.g. Jupyter Notebook, Spyder, etc.)
2. Run the code to simulate the random walks and display the histogram of final positions
3. The calculated probability will be printed to the console