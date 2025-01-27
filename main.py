import matplotlib.pyplot as plt
import random
import time

# Define the Agent class
class Agent:
    def __init__(self, name, wealth, power, money):
        self.name = name
        self.wealth = wealth  # Land, capital, etc.
        self.power = power  # Military/economic influence
        self.money = money  # Gold/liquidity
        self.plenty_score = self.calculate_plenty()
        self.power_coefficient = 0.4
        self.wealth_coefficient = 0.4
        self.money_coefficient = .2
        self.trade_benefit_coefficient = .5

    def calculate_plenty(self):
        return (self.wealth * self.wealth_coefficient +
                self.power * self.power_coefficient +
                self.money * self.money_coefficient)

    def trade(self, other, trade_amount):
        if self.money >= trade_amount:
            self.money -= trade_amount
            other.money += trade_amount
            self.wealth += trade_amount * self.trade_benefit_coefficient
            other.wealth += trade_amount * self.trade_benefit_coefficient
            self.update_scores()
            other.update_scores()

    def update_scores(self):
        self.plenty_score = self.calculate_plenty()

# Initialize agents
agents = [
    Agent("Ctry A", wealth=100, power=50, money=200),
    Agent("Ctry B", wealth=80, power=70, money=150),
    Agent("Ctry C", wealth=120, power=40, money=180)
]

# Store plenty scores over time
plenty_scores = {agent.name: [agent.plenty_score] for agent in agents}

# Simulate interactions and plot dynamics
plt.ion()  # Interactive mode
fig, ax = plt.subplots()

def simulate_round(agents):
    for agent in agents:
        trade_partner = random.choice([a for a in agents if a != agent])
        trade_amount = random.randint(10, 50)
        agent.trade(trade_partner, trade_amount)

for i in range(10):  # Simulate 10 rounds
    simulate_round(agents)

    # Update plenty scores
    for agent in agents:
        plenty_scores[agent.name].append(agent.plenty_score)

    # Plot the updated scores
    ax.clear()
    print("Round, Country, Wealth, Power, Money\n")
    for agent in agents:
        lbl = "{} W:{} P:{} M:{}".format(agent.name,agent.wealth, agent.power, agent.money)
        print("{} {} {} {}".format(i,agent.wealth, agent.power, agent.money))
        ax.plot(plenty_scores[agent.name], label=lbl)

    ax.set_title("Dynamics of Plenty Scores")
    ax.set_xlabel("Rounds")
    ax.set_ylabel("Plenty Score")
    ax.legend()
    plt.pause(1)  # Pause to simulate real-time updates
    input()

plt.ioff()
plt.show()