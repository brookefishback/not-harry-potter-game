#IMPORT RANDOM FOR RANDOM SPELL HP VALUES
import random
import time

#WELCOME MESSAGE
print('Welcome to Not Harry Potter! The ultimate gaming experience.')
time.sleep(2)
print("The players in the game are NOT Harry Potter and NOT Voldemort. There will be magic spells, swords, fireballs and lightning strikes.")
print("As you can imagine, it's going to be....")
time.sleep(3)
print("BLOODY!")
time.sleep(1)
print("GRUESOME!")
time.sleep(1)
print("HORRID!")
time.sleep(1)
print("DIRE!")
time.sleep(1)
print("APPALING!")
time.sleep(1)
print("DREADFUL!")
time.sleep(1)
print("SEVERE!")
time.sleep(1)
print("EXTREME!")
time.sleep(2)
print("Okay, okay... we think you get it. This is going to be unlike any game you've ever played. With the tenacity of NOT Harry Potter vs. the stamina of NOT Voldemort - it's going to be a close battle.")
time.sleep(4)
print("Who will win? Well, only you can decide.")
time.sleep(3)
print("DUN DUN DUNNNNNNNNN!!!!!!")
time.sleep(2)
print("Now let's get to it!")
time.sleep(3)

#ASSIGN PLAYERS 
print("There will be two players.")
time.sleep(2)
print("You are NOT Harry Potter and I am NOT Voldemort")
time.sleep(3)

#NOT HARRY POTTER ATTACKS
print("NOT Harry Potter, your power is casting spells. Check out your options below: ")
time.sleep(3)
print("1. Magic Spell")
time.sleep(1)
print("2. Hit with a Sword")
time.sleep(1)
print("3. Fireball Throw")
time.sleep(1)
print("4. Lightning Strike")
time.sleep(3)

#BEGIN GAME
input("Type yes if you are ready to begin: ")

#CREATE PLAYER CLASS WITH FUNCITONS
class Player(object):

    def __init__(self, health=100):
        """Purpose - is to define health points and associate to player."""
        self.health = health

    def hit(self):
        """Purpose - create a function that randomly assigns health points to a spell and removes value from overall health."""
        spell_power_health_points = random.randrange(4,20,2) 
        self.health = (self.health - spell_power_health_points)

#ASSIGN A HIT
def main():
        """Purpose - create a fuction that assigns a hit to a player."""
        player = Player()
        player2 = Player()
        while player.health > 1 and player2.health > 1: 
            player.hit()
            print('Not Voldemort attacked! Your new health score is...')
            time.sleep(1)
            print(player.health)
            time.sleep(2)
            input('What spell would you like to cast next on Not Voldemort? ')
            time.sleep(1)
            print('Nice Hit!')
            player2.hit()
            print('You attacked Not Voldemort, his new health score is...')
            time.sleep(1)
            print(player2.health)
            time.sleep(2)
        
        if player.health < 1:
            print('You dieeeeed!')
        if player2.health < 1:
            print ('You woooon!!')
    

if __name__ == '__main__':
    main()