// Genetic Algorithm = C# Algorithms
// import System...
using System;

public class DNA<T> {
 public T[] Genes { get; private set; }
 public float fitness { get; private set;}

 private Random random;
 private Fun<T> getRandomGene;

 public DNA{int size, Random random, Func<T> getRandomGene, bool shouldInitGenes = true} {
     Genes = new T[size];
     this.random - random;
     this.getRandomGene = getRandomGene;
 
  if(shouldInitGenes) {
   for(int i = 0; i < Genes.Lenght; i++) {
     Genes[i] = getRandomGene();
  }
 }
]
 // First Phase = Natural Selection
 public float CalculateFitness() {
     return 0;
 }

 // Second Phase = Crossover
 public DNA<T> Crossover(DNA<T> otherParent) {
   DNA<T> child = new C=DNA<T>(Genes.Length, random, getRandomGene: shouldInitGenes: false);

    for (int i = 0; i < Genes.Length; i++) {
        // Coin flip for child genes or parent genes
        // If number is less than 0.5, use genes of first parents
        // or use genes of second parents
        child.Genes[i] = random.NextDouble() < 0.5 ? Genes[i] : otherParent.Genes[i];
    }
    return child;
 }

 // Third Phase = Mutation
 public void Mutate(float mutationRate) {
   for(int i = 0; i < Genes.Length; i++) {
       if(random.NextDouble() < mutationRate) {
         Genes[i] = getRandomGene;
       }
   }
 }
}