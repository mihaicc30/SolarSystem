import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """
    categories = {}
    with open("types.txt", "r") as file:
        x = file.readline()
        y = file.readline()
        print(x, y)
    labels = ["Planets", "Non-Planets"]
    data = [x, y]  # need to link categories
    explode = [0.5, 0]
    plt.pie(data, labels=labels, startangle=90, explode=explode, shadow=True)
    plt.show()


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    with open("gravities.txt") as f:
        lista = []
        for line in f:
            lista.append(line.strip())
        low = lista[0]
        med = lista[1]
        high = lista[2]
    x = ["Low", "Medium", "High"]
    y = [low, med, high]  # need to link categories

    plt.bar(x, [int(z) for z in y], color='blue', width=0.4)
    plt.ylabel("Number of planets")
    plt.xlabel("Types of gravity")
    plt.title("Solar System")
    plt.show()


def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """
    with open("to_orbit.txt") as f:
        lista = []
        for line in f:
            lista.append(line.strip())
        small = lista[0]
        large = lista[1]
    fig, ax = plt.subplots(1, 2)
    x = 0
    y1 = int(small)
    y2 = int(large)
    print(y1, y2)
    # ax[0].bar(x,y1)
    # ax[1].bar(x,y2)

    plt.show()


def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    categories = {}
    fig, ax = plt.subplots(1, 3)

    def animate(frame):
        ax[0].cla()
        ax[0].set_xlim(0, 2 * np.pi)
        ax[0].set_ylim(-8, 8)
        x = np.arange(0, 2 * np.pi, 0.01)
        y = np.sin(x + frame)
        ax[0].plot(x, y)
        ax[0].set_xlabel('Low Gravity')
        ax[0].axes.get_yaxis().set_visible(False)
        ax[0].set_xticklabels([])
        ax[0].set_xticks([])
        #
        ax[1].cla()
        ax[1].set_xlim(0, 2 * np.pi)
        ax[1].set_ylim(-2, 2)
        x = np.arange(0, 2 * np.pi, 0.01)
        y = np.sin(x + frame)
        ax[1].plot(x, y)
        ax[1].set_xlabel('Medium Gravity')
        ax[1].axes.get_yaxis().set_visible(False)
        ax[1].set_xticklabels([])
        ax[1].set_xticks([])
        #
        ax[2].cla()
        ax[2].set_xlim(0, 2 * np.pi)
        ax[2].set_ylim(-1, 1)
        x = np.arange(0, 2 * np.pi, 0.01)
        y = np.sin(x + frame)
        ax[2].plot(x, y)
        ax[2].set_xlabel('High Gravity')
        ax[2].axes.get_yaxis().set_visible(False)
        ax[2].set_xticklabels([])
        ax[2].set_xticks([])

    def run():
        some_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)

        plt.show()

    run()
