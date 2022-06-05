import random

anime_lst_1 = ['Naruto','DeathNoe','86','Kill la Kill','Hunter x Hunter','Spy x Family',"Jojo Series","Made in Abyss","Bleach"]
anime_lst_2 = ['Boruto',"Dragon Ball Series","One Piece",'Monster','Erased','Jusjutsu Kaisen',"Assasination Classroom","My Hero Academia", "Death Parade"]
anime_lst_3 = ['Ergo Proxy',"Paranoia Agent","Baccano","Promised Neverland",'Food Wars','Tokyo Ghoul',"Moriarty the Patriot","Dr.Stone"]

lists = [anime_lst_1, anime_lst_2, anime_lst_3]

print("\t\t\t****Welcome to Anime Recommender****\n\n")
try:
    inp = int(input("Enter number of recommendations you want:\n"))
except:
    print("Invalid Input. Restart the Program.")

for  i in range(inp):
    print("Recommendation ", i, " is :", lists[random.randint(0, 2)][random.randint(0, len(anime_lst_1))])

