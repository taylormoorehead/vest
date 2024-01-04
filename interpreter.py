import sys

path = sys.argv[1]

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

program = {}
code = []
token = 0
#label = {}
for line in lines:
    parts = line.split(" ")
    operation = parts[0]

    if operation == "":
        continue

    # if operation.endswith(":"):
    #     label[operation[:-1]] = token
    #     continue

    # program.append(operation)
    # token += 1

    code.append(operation)
    token += 1

    if operation == "write":
        filename = parts[3]
        program["filename"] = filename
        token += 1

    if len(parts) > 2 and parts[2].__contains__("wacc("):
        e = float(parts[2].split("wacc(")[1].split(",")[0])
        d = float(parts[3].split(",")[0])
        re = float(parts[4].split(",")[0])
        rd = float(parts[5].split(",")[0])
        t = float(parts[6].split(")")[0])
        program["e"] = e
        program["d"] = d
        program["re"] = re
        program["rd"] = rd
        program["t"] = t

count = 0
while code[count] != "END":
    operation = code[count]
    count += 1

    if operation == "write":
        filename = program.get("filename")
        with open(filename, "w") as file:
            file.write(str(program.get("wacc")))
            file.write("\n")
    
    elif operation == "company_wacc":
        e = program.get("e")
        d = program.get("d")
        re = program.get("re")
        rd = program.get("rd")
        t = program.get("t")
        wacc = (e / (d + e)) * re + (d / (d + e)) * rd * (1 - t)
        program["wacc"] = wacc

