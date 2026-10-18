
from pathlib import Path

from src.agents.coordinator import run_multi_agent_system


def main():
    print("=" * 45)
    print("MULTI-AGENT RESEARCH SYSTEM")
    print("=" * 45)

    try:
        topic = input("\nEnter a research topic: ").strip()

        # Validate user input
        if not topic:
            print("Error: Topic cannot be empty.")
            return

        if len(topic) > 200:
            print("Error: Topic must be 200 characters or fewer.")
            return

        # Run the workflow
        report = run_multi_agent_system(topic)

        # Create the output directory
        output_folder = Path("data/reports")
        output_folder.mkdir(parents=True, exist_ok=True)

        # Save a separate report for each run
        safe_name = "".join(
            c if c.isalnum() or c in "-_" else "_"
            for c in topic
        )[:60]

        report_file = output_folder / f"{safe_name}.txt"
        report_file.write_text(report, encoding="utf-8")

        print("\n" + report)
        print(f"\nReport saved to: {report_file}")

    except (OSError, UnicodeError) as error:
        print(f"File error: {error}")

    except (KeyError, IndexError, TypeError) as error:
        print(f"Agent workflow error: {error}")


if __name__ == "__main__":
    main()