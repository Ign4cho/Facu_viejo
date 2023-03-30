import csv

if __name__ == '__main__':
    archivo = open('calefactor-electrico.csv', 'w', newline='')
    writer = csv.writer(archivo)

    writer.writerow(['Liliana', '12', '400'])
    writer.writerow(['Philips', '44', '350'])
    writer.writerow(['Liliana', '22', '500'])
    writer.writerow(['Calor', '13', '320'])
    writer.writerow(['Vento', '32', '510'])
    archivo.close()

    archi = open('calefactor-a-gas.csv', 'w', newline='')
    write = csv.writer(archi)
    write.writerow(['Gasol', '15', 'GN03', '6000'])
    write.writerow(['Pirex', '21', 'GN05', '6100'])
    write.writerow(['Natu', '19', 'GN07', '5500'])
    archi.close()
