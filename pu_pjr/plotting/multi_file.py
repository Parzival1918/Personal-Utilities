from matplotlib import pyplot as plt
from . import utils

# Plot data from multiple files
def plot_multifile(
        pattern: str, dir: str = "./", xcol: int = 0, ycol: int=1, sep: str=' ',
        testing: bool = False, **kwargs
        ):
    dfs, filenames = utils.load_many_data(pattern, sep=sep, dir=dir) # Load data

    # Find the x and y ranges so that all data can be plotted on the same axes
    # x_min = min([df.iloc[:, xcol].min() for df in dfs])
    # x_max = max([df.iloc[:, xcol].max() for df in dfs])
    # y_min = min([df.iloc[:, ycol].min() for df in dfs])
    # y_max = max([df.iloc[:, ycol].max() for df in dfs])

    # Plot each file in subplots
    # Get number of files
    n_files = len(dfs)

    # Create figure and axes
    _, axes = plt.subplots(ncols=1, nrows=n_files)#, figsize=(12, 6))

    # Plot each file
    for i in range(n_files):
        df = dfs[i]
        x = df.iloc[:, xcol]
        y = df.iloc[:, ycol]
        axes[i].plot(x, y, **kwargs)
        axes[i].set_xlabel(f"File: {filenames[i]}")
        # axes[i].set_ylabel("y")
        axes[i].grid()
        # axes[i].set_xlim(x_min, x_max)
        # axes[i].set_ylim(y_min, y_max)

    plt.suptitle(pattern)
    plt.show(block=not testing)
