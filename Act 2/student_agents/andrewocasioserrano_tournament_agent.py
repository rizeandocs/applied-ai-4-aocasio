#!/usr/bin/env python
"""
Tournament Agent: Cleanthes
Student: Andrew Ocasio Serrano
Generated: 2026-09-30 09:08:36

Evolution Details:
- Generations: 100
- Final Fitness: N/A
- Trained against: Adaptive, Prober, Random (0.1), Tit-for-Two-Tats, Suspicious Tit-for-Tat...

Strategy: Starts cooperative and rewards cooperation fully, but has a low tolerance for defection. Retaliates once an opponent crosses a low hostility threshold and rarely forgives, avoiding exploitation by consistently hostile opponents.
"""

from agents import Agent, INVEST, UNDERCUT
import random


class AndrewOcasioSerranoAgent(Agent):
    """
    Cleanthes

    Starts cooperative and rewards cooperation fully, but has a low tolerance for defection. Retaliates once an opponent crosses a low hostility threshold and rarely forgives, avoiding exploitation by consistently hostile opponents.

    Evolved Genes: [0.7378386062536859, 1.0, 0.3198439876294813, 0.14408434764107342, 0.3410999818473446, 0.290503294583385]
    """

    def __init__(self):
        # These genes were evolved through 100 generations
        self.genes = [0.7378386062536859, 1.0, 0.3198439876294813, 0.14408434764107342, 0.3410999818473446, 0.290503294583385]

        # Required for tournament compatibility
        self.student_name = "Andrew Ocasio Serrano"

        super().__init__(
            name="Cleanthes",
            description="Starts cooperative and rewards cooperation fully, but has a low tolerance for defection. Retaliates once an opponent crosses a low hostility threshold and rarely forgives, avoiding exploitation by consistently hostile opponents."
        )

    def choose_action(self) -> bool:
        """
        IMPROVED decision logic - AGGRESSIVE VERSION
        More likely to retaliate, less exploitable
        """

        # First 3 rounds: use initial cooperation gene
        if self.round_num < 3:
            return random.random() < self.genes[0]

        # Calculate memory window
        memory_length = max(1, int(self.genes[4] * 10) + 1)
        recent_history = self.history[-memory_length:]
        cooperation_rate = sum(recent_history) / len(recent_history)

        retaliation_threshold = self.genes[5]

        if cooperation_rate >= retaliation_threshold:
            coop_prob = self.genes[1] * min(1.0, cooperation_rate + 0.2)
            return random.random() < coop_prob
        else:
            if random.random() < self.genes[2]:
                return UNDERCUT
            else:
                return random.random() < self.genes[3]



# Convenience function for tournament loading
def get_agent():
    """Return an instance of this agent for tournament use"""
    return AndrewOcasioSerranoAgent()


if __name__ == "__main__":
    # Test that the agent can be instantiated
    agent = get_agent()
    print(f"✅ Agent loaded successfully: {agent.name}")
    print(f"   Genes: {agent.genes}")
    print(f"   Description: {agent.description}")
