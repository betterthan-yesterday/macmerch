import sys

def parseArguments():
    arguments = {
        "price": float(sys.argv[1]),
        "quantity": int(sys.argv[2]),
        "province": sys.argv[3],
    }
    return arguments

def taxRate(province):
    tax = {
        "ON": 0.13,
    }
    return tax[province]

def macmerchCalculator():
    args = parseArguments()
    tax = taxRate(args["province"])
    print(args["price"] * args["quantity"] * (1+tax))

macmerchCalculator()