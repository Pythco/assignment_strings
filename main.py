# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'
# Add your code after this line
player_1 = 	"Ruud Gullit"
player_2 =  "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = f'{player_1} {goal_0}, {player_2} {goal_1}'
print(scorers)
report = f'{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute'
print(report)
player = "Ronald Koeman"
last_name_len = len(player) - player.find("Koeman")
print(last_name_len)
index_of_space= player.find(" ")
name_short = player[0]+ ". " + player[index_of_space+1:]
print(name_short)
first_name = player[0:index_of_space]
len_first_name = len(first_name)
print(first_name)
chant = (first_name + "! ") * (len_first_name -1) + (first_name + "!")
print(chant)
good_chant = (chant[-1]!= " ")
print(good_chant)
