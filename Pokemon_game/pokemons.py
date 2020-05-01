import random 


class Pokemon:
  def __init__(self,name,lvl,typ,knocked_out,spd):
    self.name = name
    self.lvl = lvl
    self.typ = typ
    self.m_health = self.lvl * 10
    self.c_health = self.m_health
    self.knocked_out = knocked_out
    self.atck = self.lvl * 2
    self.spd = spd

  def __repr__(self):
    return self.name 

  def check_stats(self):
    tmp_name =self.name.replace("Your ","") 
    print(f"""
===================
\n{tmp_name} \nHealth {self.c_health}/{self.m_health}\nLevel {self.lvl}\nSpeed {self.spd}\nDefault attack {self.atck}
""")

  def gain_exp(self):
    self.lvl += 1
    self.m_health += 20
    self.c_health = min(self.c_health + 20, self.m_health)
    print(f"Level of {self.name} increased to level {self.lvl}. Max health got a boost as well and now it's {self.m_health}")
    
  def lose_health(self,damage):
    if self.c_health>0:
      self.c_health -= damage
      if self.c_health<=0:
        self.c_health=0
      else:
        print (f"{self.name} health {self.c_health}/{self.m_health}")
    
    if self.c_health<=0:
      self.knocked_out = True
      Pokemon.knock_out(self)
  
  def gain_health(self):
    heal = 20
    
    if self.c_health < self.m_health:
      self.c_health = min(self.c_health + heal, self.m_health)
      print (f"Health of {self.name} after healing is {self.c_health}/{self.m_health}")
      
      if self.c_health > self.m_health:
        self.c_health = self.m_health
        print (f"Health of {self.name} is maxed out and it is {self.c_health}")
    
    else:
      print (f"You used potion but health of {self.name} is {self.c_health} and didn't need healing!")

  def knock_out(self):
    if self.knocked_out == True:
      print (f"\n{self.name} has been knocked out!\n")

  def revival(self):
    if self.knocked_out == True:
      self.knocked_out = False
      self.c_health = self.m_health
      print (f"{self.name} is back to life with {self.c_health} health")

  def attack(self,enemy):
    damage = self.atck + random.randint(1,5)

    if self.typ == enemy.typ:
      print(self.name, "attacks", enemy.name, "with normal damage of",damage)
      enemy.lose_health(damage)
    
    else:
      damage = damage * power_dict[self.typ][enemy.typ]
      
      if power_dict[self.typ][enemy.typ] == 2:
        pass
        print(f"{self.name} attacks {enemy.name} == > {damage}. {self.typ} against {enemy.typ} is very effective",)
      elif power_dict[self.typ][enemy.typ] == 0.5:
        print(f"{self.name} attacks {enemy.name} == > {damage}. {self.typ} against {enemy.typ} is not very effective",)
        pass

      enemy.lose_health(damage)

class Trainer:
  def __init__(self,name,pokemons_list,potions,c_pokemon):
    self.name = name
    self.pokemons_list = pokemons_list
    self.potions = potions
    self.c_pokemon = c_pokemon

  def __repr__(self):
    return self.name

  def check_pl_stats(self):
    if len(self.pokemons_list) == 0:
      print(f"{self.name} has no pokemnos left ")
    else:
      self.pokemons_list[self.c_pokemon].check_stats()
      print(f"""potions {self.potions}
===================
      """)

  def use_potion(self):
    if self.potions >0:
      self.potions -= 1
      print(f"{self.name} uses potion on {self.pokemons_list[self.c_pokemon].name.replace('Your ','')}")
      self.pokemons_list[self.c_pokemon].gain_health()
    else:
      print ("You've run out of potions")

  def attack_pl(self,enemy):
    if len(enemy.pokemons_list) == 0:
      print (f"{enemy.name} has no pokemons left! You won!")
      return False
    
    else:
      while True:
        enem_cur_pok = enemy.pokemons_list[enemy.c_pokemon]
        cur_pok = self.pokemons_list[self.c_pokemon]
        
        print (f"""\n===========================================
{enem_cur_pok.typ} {enem_cur_pok.name} {enem_cur_pok.c_health}/{enem_cur_pok.m_health} is in front of you!
{cur_pok} has {cur_pok.c_health}/{cur_pok.m_health}
What do you want to do?
===========================================\n""")
        print("\n1) Fight! \n2) Use healing potion \n3) Retreat")
        answ = int(input("\n"))
        
  
        if answ == 1:
          if cur_pok.knocked_out == True:
            print ("This Pokemon has been knocked out and can't attack, pick another one")
            break
          #main battle here 
          else:
            if cur_pok.spd > enem_cur_pok.spd:
              print("\nYour pokemon is faster, it attacks first\n===================FIGHT===================\n")
              cur_pok.attack(enem_cur_pok)
              enem_cur_pok.attack(cur_pok)
            else:
              print("\nEnemy's pokemon is faster, it attacks first\n===================FIGHT===================\n")
              enem_cur_pok.attack(cur_pok)
              cur_pok.attack(enem_cur_pok)

          if enem_cur_pok.knocked_out == True:
            cur_pok.gain_exp()
            enemy.pokemons_list.remove(enem_cur_pok)
            enemy.c_pokemon = 0
            #print(f"{enem_cur_pok} has been returned to the hospital. Again...")
            break
        elif answ == 2:
          Trainer.use_potion(self)
        elif answ == 3:
          break

  def switch_active_pokemon(self):
    old_pos = self.c_pokemon

    print(f"Your current Pokemon is {self.pokemons_list[self.c_pokemon]}")
    count_check = 0 
    for pokemon in range(len(self.pokemons_list)):
      if self.pokemons_list[pokemon].knocked_out == True:
        print (pokemon+1,self.pokemons_list[pokemon].name.replace("Your ",""),"is knocked out")
        count_check += 1
      else:
        print (pokemon+1,self.pokemons_list[pokemon].name.replace("Your ",""),f"{self.pokemons_list[pokemon].c_health}/{self.pokemons_list[pokemon].m_health} lvl {self.pokemons_list[pokemon].lvl}")

    if count_check == 3:
      print ("You lost the battle! As expected ;) ")
      return False

    while True:
      position = int(input("\n")) - 1 

      try:
        if self.pokemons_list[position].knocked_out == True:
          print("This Pokemon has been knocked out, you can't pick it")
        elif position == old_pos:
          print("No changes have been made")
          break
        elif self.pokemons_list[position].knocked_out == False:
          self.c_pokemon = position
          print(self.name,"changed",self.pokemons_list[old_pos],"to",self.pokemons_list[self.c_pokemon])
          break
      except IndexError as e:
        print("Number is out of range")   

# Relathionships between pokemon powers

power_dict = { 
"Fire":{"Water":0.5, "Grass":2},
"Water":{"Fire":2, "Grass":0.5},
"Grass":{"Water":2, "Fire":0.5}
}

# hardcoded Pokemons and parameters for the sake of intersting gameplay 
ash_charmander = Pokemon("Charmander",5,"Fire",False,65)
ash_bulbasaur = Pokemon("Bulbasaur",5,"Grass",False,45)
ash_squirtle = Pokemon("Squirtle",5,"Water",False,43)
ash = Trainer("Ash",[ash_charmander,ash_bulbasaur,ash_squirtle],0,0)

charmander = Pokemon("Your Charmander",3,"Fire",False,65)
bulbasaur = Pokemon("Your Bulbasaur",3,"Grass",False,45)
squirtle = Pokemon("Your Squirtle",3,"Water",False,43)

  
def battle():
  print ("""\n\nWelcome to the training camp where you can battle Pokemons!
You have 3 pokemons to fight with 3 opponents. 
Trainer Ash will fight you so be careful, it's not an easy fight!
I would highly recommend paying attention to stats.
So what is your name again?\n""")
  player_name = input()
  player = Trainer(player_name,[charmander,bulbasaur,squirtle],2,2)
  print(f"\nWelcome {player_name}! What would you like to do?")
  
  while True:
    print("""
1) Fight Ash
2) Compare stats 
3) Switch your current Pokemon
4) Quit
      """)

    answ = int(input("\n"))
    if answ == 1:
      #player.attack_pl(ash)
      if player.attack_pl(ash) == False:
        break
    elif answ == 2:
      print("\n\n\nYour current Pokemon")
      player.check_pl_stats()
      print("Ash's current Pokemon")
      ash.check_pl_stats()
    elif answ == 3:
      #player.switch_active_pokemon()
      if player.switch_active_pokemon() == False:
        break
    elif answ == 4:
      break
  print("Bye!")

battle()