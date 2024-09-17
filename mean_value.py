# Medelvärde
def medel(tal):
        tal_lista = tal.split()
        ant = len(tal_lista)
        sum = 0
        for tal in tal_lista:
            sum = sum + int(tal)
        mv = sum/ant
        return mv

def main():
    tal = input("")
    medel(tal)
        
        

if __name__ == "__main__":
    main()
