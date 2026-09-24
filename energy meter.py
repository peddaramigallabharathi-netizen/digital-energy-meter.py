import time
from datetime import datetime


def calculate_power(voltage, current):
    return voltage * current


def calculate_energy(power, seconds):
    return (power * seconds) / 3600000  # Wh


def main():
    print("=" * 45)
    print("       DIGITAL ENERGY METER")
    print("=" * 45)

    total_energy = 0.0

    try:
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))
        duration = int(input("Enter monitoring time (seconds): "))

        power = calculate_power(voltage, current)

        print("\nMeter started...")
        print(f"Voltage : {voltage:.2f} V")
        print(f"Current : {current:.2f} A")
        print(f"Power   : {power:.2f} W")
        print("-" * 45)

        start_time = time.time()

        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            energy = calculate_energy(power, elapsed)
            total_energy = energy

            print(
                f"\rTime: {elapsed:.0f}s | "
                f"Power: {power:.2f} W | "
                f"Energy: {total_energy:.4f} Wh",
                end=""
            )

            time.sleep(1)

        print("\n\n" + "=" * 45)
        print("           FINAL READING")
        print("=" * 45)
        print(f"Date/Time : {datetime.now()}")
        print(f"Voltage   : {voltage:.2f} V")
        print(f"Current   : {current:.2f} A")
        print(f"Power     : {power:.2f} W")
        print(f"Energy    : {total_energy:.4f} Wh")
        print(f"Energy    : {total_energy / 1000:.6f} kWh")
        print("=" * 45)

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
