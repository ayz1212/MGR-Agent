"""
MGR Agent — Interactive CLI
Run: python main.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from src.agent import run_agent


def main():
    print("=" * 55)
    print("   MGR — Movie & Games Recommender Agent")
    print("   Powered by Claude AI  |  Observe→Think→Act")
    print("=" * 55)
    print("\nTell me what you want to watch or play.")
    print("Example: 'scary horror movie tonight on Netflix'")
    print("Type 'quit' to exit.\n")

    history = []

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("\nGoodbye! Enjoy your movie or game 🎬🎮")
            break

        result = run_agent(user_input, user_history=history)

        print("\n" + "=" * 55)
        print(f"  Top {result['count']} picks for you:")
        print("=" * 55)

        for i, item in enumerate(result["recommendations"], 1):
            print(f"\n  {i}. {item['title']}  [{item['type'].upper()}]")
            print(f"     Genre  : {item['genre']}")
            print(f"     Score  : {item['score']:.1f} / 10")
            print(f"     Why    : {item['reason']}")

        print("\n" + "=" * 55)

        # Add to history
        liked = input("\nAdd any to history? (title or press Enter to skip): ").strip()
        if liked:
            history.append(liked)
            print(f"  ✓ Added '{liked}' to your history.\n")


if __name__ == "__main__":
    main()
