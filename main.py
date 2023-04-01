import random

adverbs = ['extremely', 'quite', 'very', 'totally', 'completely', 'utterly', 'absolutely', 'incredibly', 'awfully', 'exceptionally', 'particularly', 'remarkably', 'unbelievably', 'eminently', 'exceedingly', 'highly', 'intensely', 'mightily', 'particularly', 'terribly', 'vastly', 'deeply', 'profoundly', 'greatly', 'strongly', 'entirely', 'fully', 'perfectly', 'thoroughly', 'wholly', 'absurdly', 'amazingly', 'astonishingly', 'blatantly', 'decidedly', 'strikingly', 'uncommonly', 'significantly', 'inordinately', 'surprisingly', 'unusually', 'dramatically', 'radically', 'substantially']
adjectives = ['happy', 'sad', 'angry', 'calm', 'excited', 'nervous', 'confused', 'proud', 'embarrassed', 'frustrated', 'grateful', 'jealous', 'lonely', 'scared', 'surprised', 'tired', 'curious', 'brave', 'shy', 'optimistic', 'pessimistic', 'silly', 'serious', 'creative', 'lazy', 'energetic', 'generous', 'selfish', 'compassionate', 'cold', 'hot', 'friendly', 'hostile', 'enthusiastic', 'skeptical', 'thrilled', 'bored', 'romantic', 'passionate', 'inspired', 'determined', 'insecure', 'confident']
nouns = ['cat', 'dog', 'house', 'car', 'tree', 'book', 'phone', 'computer', 'desk', 'chair', 'table', 'guitar', 'painting', 'flower', 'bicycle', 'camera', 'coffee', 'cupcake', 'umbrella', 'suitcase', 'pen', 'piano', 'map', 'globe', 'microphone', 'telescope', 'rocket', 'planet', 'moon', 'star', 'galaxy', 'universe', 'mountain', 'river', 'ocean', 'beach', 'forest', 'park', 'zoo', 'museum', 'library', 'hospital', 'restaurant', 'airport', 'train', 'bus']
verbs = ['hates', 'dislikes', 'disapproves', 'despises', 'criticizes', 'condemns', 'rejects', 'denies', 'refuses', 'avoids', 'evades', 'escapes', 'flees', 'runs', 'hides', 'lies', 'cheats', 'steals', 'betrays', 'hurts', 'wounds', 'injures', 'damages', 'destroys', 'ruins', 'ends', 'quits', 'abandons', 'neglects', 'ignores', 'forgets', 'disregards', 'dismisses', 'belittles', 'undermines', 'demoralizes', 'discourages', 'frustrates', 'annoys', 'irritates', 'angers', 'enrages', 'offends', 'insults']

def generate_fph():
  chosenadv = random.choice(adverbs)
  chosenadj = random.choice(adjectives)
  chosennoun = random.choice(nouns)
  return chosenadv + "-" + chosenadj + "-" + str(random.randrange(0, 100)) + "-" + chosennoun

print(generate_fph() + "-" + random.choice(verbs) + "-" + generate_fph())
