# Fuel Gauge


def main():
    while True:
        fraction = input("Fraction: ").strip().split("/")
        if len(fraction) != 2:
            continue
        
        try:
            result = int(fraction[0]) / int(fraction[1])
        except (ValueError, ZeroDivisionError):
            continue
        else:
            result *= 100

        if result > 100:
            continue
        elif result >= 99:
            print("F")
        elif result <= 1:
            print("E")
        else:
            print(f"{round(result)}%")
        
        break


if __name__ == "__main__":
    main()
