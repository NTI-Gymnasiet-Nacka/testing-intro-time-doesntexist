# Gradkonverterare

def main():
    def converter(celsius):
        fahrenheit = celsius * 1.8 + 32
        print(f'{fahrenheit:.2f}')

    celsius = float(input())
    converter(celsius)


if __name__ == "__main__":
    main()
