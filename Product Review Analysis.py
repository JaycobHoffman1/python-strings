reviews = [
'This product is really good. I\'m impressed with its quality.', 
'The performance of this product is excellent. Highly recommended!', 
'I had a bad experience with this product. It didn\'t meet my expectations.', 
'Poor quality product. Wouldn\'t recommend it to anyone.', 
'The product was average. Nothing extraordinary about it.'
]

# Task 1: Keyword Highlighter

print('Task 1: Keyword Highlighter')

keywords = ['good', 'excellent', 'bad', 'poor', 'average']

for i in range(len(keywords)):
    for j in range(len(reviews)):
        if keywords[i] in reviews[j]:
            print(reviews[j].replace(keywords[i], keywords[i].upper()))
        elif keywords[i].capitalize() in reviews[j]:
            print(reviews[j].replace(keywords[i].capitalize(), keywords[i].upper()))


# Task 2: Sentiment Tally

print('Task 2: Sentiment Tally')

positive_words = ['good', 'excellent', 'great', 'awesome', 'fantastic', 'superb', 'amazing']
negative_words = ['bad', 'poor', 'terrible', 'horrible', 'awful', 'disappointing', 'subpar']

def tally(lst1, lst2, lst3):
    def tally_list(a, b):
        for i in range(len(b)):
            counter = 0

            for j in range(len(a)):
                if b[i] in a[j]:
                    counter += a[j].count(b[i])
                elif b[i].capitalize() in a[j]:
                    counter += a[j].count(b[i].capitalize())

            print(f'"{b[i]}" appears {counter} {'time' if counter == 1 else 'times'} in the reviews.'\
            if counter > 0 else f'"{b[i]}" does not appear in the reviews.')

    print('Positive Words')
    tally_list(lst1, lst2)

    print('Negative Words')
    tally_list(lst1, lst3)
tally(reviews, positive_words, negative_words)


# Task 3: Review Summary

print('Task 3: Review Summary')

for i in range(len(reviews)):
    print(f'{reviews[i][:30 + reviews[i][31:].index(' ') + 1]\
    if reviews[i][30] != ' ' else reviews[i][:30]}{' ' if reviews[i][29] != ' ' else ''}...')