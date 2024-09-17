# Vokalräkning

def main():
    vokaler=["a","o","u","å","i","y","ä","ö","e"]

    mening = input('')

    räknare = 0 #En counter som startar på noll men höjs ju fler vokaler for-loopen hittar

    for i in mening:
        if i in vokaler:
            räknare=räknare+1
    print(f"{räknare}")


if __name__ == "__main__":
    main()
