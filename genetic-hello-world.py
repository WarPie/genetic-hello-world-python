import string
import random

TARGET = "Hello World!"
NUM_SAMPLES = 1000
NUM_SELECTED = 100
LETTERS = string.ascii_letters + ' '

def generate_random_chromosomes():
  chromos = []
  while len(chromos) < NUM_SAMPLES:
    new_chromo = ''
    while len(new_chromo) < len(TARGET):
      new_chromo += random.choice(LETTERS)
    chromos.append(new_chromo)
  return chromos


def fitness(chromo):
  ''' Fitness of a chromo is the sum of how far each of its charactors is
  from the target string.

  A string that exactly matched the target string has a fitness of 0. Lower
  fitness is better than higher.

  Tests assume that 'Hello World!' is the target string.
  TODO(topher): this restriction could be removed
  >>> fitness('Hello World!')
  0
  >>> fitness('Iello World!')
  1
  >>> fitness('Iallo World!')
  5
  >>> fitness('Hello!')
  Traceback (most recent call last):
  except ValueError: input chromo length doesn't match target
  '''
  pass


def tourny_select_chromo():
  ''' Randomly select two chromosomes from the samples, then returns the one
  with the highest fitness.
  '''
  pass


def breed(a, b):
  ''' Breed two chromosomes by splicng them in a random spot and combining
  them together to form two new chromos.
  '''
  pass


def mutate(chromo):
  ''' Mutate a chromosome by changing a random char in the string by a small
  amount.
  '''
  pass


def main():
  # Create a random sample
  # for each generation
  #   create a selected group with tourny_select_chromo() until we have enough
  #   create a solution group by breeding random chromos in selected group
  #   print the best, worst, and average fitness, and the chromo with best
  #   stop loop if best fitness == 0
  sample = generate_random_chromosomes()
  print sample


if __name__ == "__main__":
  main()
