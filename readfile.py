def printInfo(filename):
  try:
    with open('test.txt') as file:
      linecount = 0
      wordcount = 0
      for line in file:
        wordcount += len(line.split())
        linecount +=1
      print(f"\nLine Count: {linecount}")
      print(f"Word Count: {wordcount}")
  except Exception as e:
    print(f"Error: {e}")