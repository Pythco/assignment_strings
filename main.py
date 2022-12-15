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
report = f'{player_1} scored in the {goal_0}nd minute' '\n' f'{player_2} scored in the {goal_1}th minute'
print(report)
player = "Ronald Koeman"
first_name = "Ronald"
print(first_name)
last_name_len = len(player) - player.find("Koeman")
print(last_name_len)
name_short = player[0]+ ". " + player[7:14]
print(name_short)
chant = "Ronald! " * 5 +"Ronald!"
print(chant)
good_chant = (chant[-1]!= " ")
print(good_chant)
