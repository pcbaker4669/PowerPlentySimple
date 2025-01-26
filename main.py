import random
import networkx as nx

# Define Agent class
class Agent:
    def __init__(self, name, wealth, power, money):
        self.name = name
        self.wealth = wealth  # Land, capital, etc.
        self.power = power  # Military/economic influence
        self.money = money  # Gold/liquidity
        self.plenty_score = self.calculate_plenty()

    def calculate_plenty(self):
        return self.wealth * 0.4 + self.power * 0.4 + self.money * 0.2

    def trade(self, other, trade_amount):
        if self.money >= trade_amount:
            self.money -= trade_amount
            other.money += trade_amount
            self.wealth += trade_amount * 0.5
            other.wealth += trade_amount * 0.5
            self.update_scores()
            other.update_scores()

    def update_scores(self):
        self.plenty_score = self.calculate_plenty()

# Initialize agents
agents = [
    Agent("Country A", wealth=100, power=50, money=200),
    Agent("Country B", wealth=80, power=70, money=150),
    Agent("Country C", wealth=120, power=40, money=180)
]

# Simulate interactions
def simulate_round(agents):
    for agent in agents:
        trade_partner = random.choice([a for a in agents if a != agent])
        trade_amount = random.randint(10, 50)
        agent.trade(trade_partner, trade_amount)

# Run the simulation
for _ in range(10):  # Simulate 10 rounds
    simulate_round(agents)

# Display results
for agent in agents:
    print(f"{agent.name}: Wealth={agent.wealth}, Power={agent.power}, Money={agent.money}, Plenty={agent.plenty_score}")
