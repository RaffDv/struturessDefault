
file = open("input.csv", "r")

output = open("output.csv","w")

for line in file:
    line = line.replace('\'','\\\'')[0:-1]
    fixline = ''
    dentroDeAspa = False
    for letra in line:
        if(letra == '"'):
            dentroDeAspa = not dentroDeAspa
        else:
            if( letra == "," and not dentroDeAspa):
                fixline += "\t"
            else:
                fixline += letra

    fields = fixline.split("\t")

    newLine = ''

    for field in fields:
        
        newLine += f"'{field}',"
    
    newLine = 'INSERT INTO aux_IPv4Blocks values (DEFAULT,' + newLine[0:-1] + ');\n'

    output.writelines(newLine)

output.close()

