import random

def generate_barcode():
          return ''.join([str(random.randint(0,9)) for _ in range(10)])

bar1=generate_barcode()
bar2=generate_barcode()
bar3=generate_barcode()

print(bar2)