import random

anime_lst_1 = ['Naruto','DeathNoe','86','Kill la Kill','Hunter x Hunter','Spy x Family',"Jojo Series","Made in Abyss","Bleach"]
anime_lst_2 = ['Boruto',"Dragon Ball Series","One Piece",'Monster','Erased','Jusjutsu Kaisen',"Assasination Classroom","My Hero Academia"]
anime_lst_3 = ['Ergo Proxy',"Redo of Healer","Baccano","Promised Neverland",'Food Wars','Tokyo Ghoul',"Moriarty the Patriot","Dr.Stone","Death Parade"]

lists = [anime_lst_1, anime_lst_2, anime_lst_3]

lengths = [len(anime_lst_1), len(anime_lst_2), len(anime_lst_3)]

print("The anime we recommend is ", lists[random.randint(0, 2)][random.randint(0, max(lengths))])

