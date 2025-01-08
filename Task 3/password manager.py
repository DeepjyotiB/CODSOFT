#task 3
import random
import string

def get_chars(level):
  return {
    "easy": string.ascii_letters,
    "medium": string.ascii_letters + string.digits,
    "hard": string.ascii_letters + string.digits + string.punctuation
  }.get(level, string.ascii_letters)

def gen_pass(length):
  level = input("Difficulty (easy/medium/hard): ").lower()
  chars = get_chars(level)
  return ''.join(random.choice(chars) for _ in range(length))

def get_length():
  while True:
    try:
      l = int(input("Enter desired password length: "))
      return l if l >= 4 else None 
    except ValueError:
      pass

def main():
  print("Password Generator")
  while True:
    print("\n1. Generate\n2. Exit")
    c = input("Choice: ")
    if c == '1':
      l = get_length()
      if l: print(f"Password: {gen_pass(l)}")
    elif c == '2':
      break

main()