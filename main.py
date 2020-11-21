text = "I love soccer."
try:
  with open('out.txt',"w") as file:
    tennis = text.replace("soccer","tennis")
    file.write(tennis)
except:
  print("Error!")