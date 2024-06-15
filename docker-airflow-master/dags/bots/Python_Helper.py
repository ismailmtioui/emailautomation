def call(**kwargs):
  try:
    result = "Hello World"
    return result
  except Exception as exception:
    print(exception)