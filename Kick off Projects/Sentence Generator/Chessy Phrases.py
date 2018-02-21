#This is a sentence generator that generates cheesy compliments/pickup lines. Just made your loved one angry? Use this
import random
#Import is used to call a specific name (in this case, we are calling a random module - Math function)
def make_sentence(start, middle1, middle2, end, n=1):
#def is used to define a function, make_sentence is the funcion identifier/name, and start, middle, end, and n=1 are the named parameters (x,y,z). 
# We use def because we are constructing a new function.
        # this will shuffle (makes it random) the lists
        random.shuffle(start)
        random.shuffle(middle1)
        random.shuffle(middle2)
        random.shuffle(end)
        
        # concatinate the parts of the sentences
        list_of_sentences = []
        for word in range(n):
         #Remember that n =1            
                try:
                #Processing an error (normal processing block)
                        list_of_sentences = start[word] + ',' + ' ' + middle1 [word] + ' ' + middle2[word] + ' ' + end[word]
                        #Structure of the sentence
                        list_of_sentences = list_of_sentences.capitalize() + '. '
                        #Capitalizes the first letter of the sentence and adds a point in the end
                except IndexError:
                    # Except if I am providing an index for which a list element does not exist
                        break
                        #In this case, it immediatly exit
        return list_of_sentences 
        
part1 = [ "Denis", 
        "Martin",
        "Marcin", 
        "Per", 
        "Fabian", 
        "Kim", 
        "Julian", 
        "Juliane", 
        "Nicolas", 
        "Thomas", 
        "Teresa", 
        "Pedro", 
        "Toby", 
        "Anka", 
        "Sarah", 
        "Antónia", 
        "Bozhidar", 
        "Gonçalo", 
        "Mathias", 
        "Tomás", 
        "Georgy", 
        "Thomas"
        ]

#part1 of the sentence---noun/subject
part2 = [
        "You", 
        ]
        
#part2 of the sentence--the verb/action
part3 = [
       "Are",
        ]
        
#part3 of the sentence--the ending(noun)
part4 = [
        "Extremely intuitive",
        "A searcher of hidden meanings",
        "Sensitive and perceptive", 
        "Gifted at reading others", 
        "A holder of strong convictions and beliefs",
        "A person who will not compromise their ideals",
        "Genuinely warm and affirming by nature",
        "Capable of trusting your own instincts (and with good reason)",
        "Usually right and you usually know it", 
        "Typically gentle and caring", 
        "Usually have good communication skills", 
        "A gifted writer", 
        "Committed and you take commitment seriously",
        "The reason why I admire you deeply",
        "A seeker of lifelong relationships",
        "A good listener",
        "Deep, complex and intense",
        "Artistic and creative",
        "A inspirator, a motivator, an achiever",
        "Extremely insightful about people and situations",
        "a Perfectionist",
        "Natural nurturer",
        "Devoted to and protective of those they care about",
        "The rarest of all types", 
        "An independent worker", 
        "In some ways, be easy-going",
        "Everything I want to be", 
        "Very important to me",
        "Not a failure", 
        "Special and idiosyncratic (heh, in a good way)",
        "Beautiful, not just outside, but deep inside as well", 
        "The person I want to risk myself for because God risk Himself on me", 
        "Perfection, even the sun is jealous of the way you shine", 
        "So kind to others", 
        "A believer that there is good in this world", 
        "Constantly racing through my mind", 
        "The next Victoria Secret Model", 
        "Loved always", 
        "Pretty, witty, and gracious", 
        "Important",
        "Geniune and sincere", 
        "One I went to spend my time with, even the future", 
        "Hotter than donut grease", 
       
        ]
     

list_of_sentences = make_sentence(part1, part2, part3, part4)

print (list_of_sentences)