import random



OPTIMAL     = "Machine Learning"
DNA_SIZE    = len(OPTIMAL)
POP_SIZE    = 20
GENERATIONS = 100000 # To avoid infinite loop, main will stop when optimal string is found



def weighted_choice(items):
  weight_total = sum((item[1] for item in items))
  n = random.uniform(0, weight_total)
  for item, weight in items:
    if n < weight:
      return item
    n = n - weight
  return item

def random_char():
  return chr(int(random.randrange(32, 126, 1)))

def random_population():
  pop = []
  for i in xrange(POP_SIZE):
    dna = ""
    for c in xrange(DNA_SIZE):
      dna += random_char()
    pop.append(dna)
  return pop

#
# GA functions
# These make up the bulk of the actual GA algorithm.
#

def fitness(dna):
  fitness = 0
  for c in xrange(DNA_SIZE):
    fitness += abs(ord(dna[c]) - ord(OPTIMAL[c]))
  return fitness

def mutate(dna):
  dna_out = ""
  mutation_chance = 100
  for c in xrange(DNA_SIZE):
    if int(random.random()*mutation_chance) == 1:
      dna_out += random_char()
    else:
      dna_out += dna[c]
  return dna_out

def mutate2(dna):
  dna_out = ""
  mutation_chance = 100
  mutationcount = 0
  for c in xrange(DNA_SIZE):
    if mutationcount > 1: mutation_chance = -100
    if int(random.random()*mutation_chance) == 1:
      if int(random.random()*100)%2 == 1:
        if (ord(dna[c]) + 1) in range(32, 126):
          dna_out += chr(ord(dna[c]) + 1)
          mutationcount += 1
        else:
          dna_out += dna[c]
      else:
        if (ord(dna[c]) - 1) in range(32, 126):
          dna_out += chr(ord(dna[c]) - 1)
          mutationcount += 1
        else:
          dna_out += dna[c]
    else:
      dna_out += dna[c]
  return dna_out

def crossover(dna1, dna2):
  pos = int(random.random()*DNA_SIZE)
  return (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])

#
# Main driver
# Generate a population and simulate GENERATIONS generations.
#

if __name__ == "__main__":
  # Generate initial population. This will create a list of POP_SIZE strings,
  # each initialized to a sequence of random characters.
  population = random_population()

  # Simulate all of the generations.
  for generation in xrange(GENERATIONS):

    print "Generation %s... Random sample: '%s'" % (generation, population[0])
    weighted_population = []

    # Add individuals and their respective fitness levels to the weighted
    # population list. This will be used to pull out individuals via certain
    # probabilities during the selection phase. Then, reset the population list
    # so we can repopulate it after selection.
    for individual in population:
      if individual == OPTIMAL:
        print "Optimal String: %s" % individual
        exit(0)
      fitness_val = fitness(individual)

      # Generate the (individual,fitness) pair, taking in account whether or
      # not we will accidently divide by zero.
      if fitness_val == 0:
        pair = (individual, 1.0)
      else:
        pair = (individual, 1.0/fitness_val)

      weighted_population.append(pair)

    population = []

    # Select two random individuals, based on their fitness probabilites, cross
    # their genes over at a random point, mutate them, and add them back to the
    # population for the next iteration.
    for _ in xrange(POP_SIZE/2):
      # Selection
      ind1 = weighted_choice(weighted_population)
      ind2 = weighted_choice(weighted_population)

      # Crossover
      ind1, ind2 = crossover(ind1, ind2)

      # Mutate and add back into the population.
      population.append(mutate2(ind1))
      population.append(mutate2(ind2))

  # Display the highest-ranked string after all generations have been iterated
  # over. This will be the closest string to the OPTIMAL string, meaning it
  # will have the smallest fitness value. Finally, exit the program.
  fittest_string = population[0]
  minimum_fitness = fitness(population[0])

  for individual in population:
    ind_fitness = fitness(individual)
    if ind_fitness <= minimum_fitness:
      fittest_string = individual
      minimum_fitness = ind_fitness


  print "Fittest String: %s" % fittest_string
  exit(0)