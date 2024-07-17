number_list = [1,2,3,4,5]   #Lista di numeri
string_list = ['Ferrari', 'Mercedes', 'Red Bull', 'Racing Bull', 'Haas']    #Lista di stringhe

if 2 in number_list:
    print(number_list[1])

print('The last Formula 1 race was won by {}'.format(string_list[0]))

BestSellingManga_dict = {'Naruto': 250, 'Bleach': 220, 'One Piece': 350, 'Dragon Ball': 200}    #Dizionario con i manga più venduti
print('Naruto has sold {} million copies'.format(BestSellingManga_dict['Naruto']))

if ('Naruto' < 'One Piece'):
    print('Naruto has sold less copies than One Piece')

for MangaName, Copies in BestSellingManga_dict():
    print('{} has sold {} million copies'.format(MangaName, Copies))