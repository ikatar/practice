# Game of Hanoi made by Alex Underwood

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_next_node(self, link_node):
    self.link_node = link_node
    
  def get_next_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def get_list_of_items(self):
    pointer = self.top_item
    out_list = []
    while(pointer):
      out_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    return out_list


  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))

print("""

░██████╗████████╗██╗░█████╗░██╗░░██╗░██████╗  ░█████╗░███████╗  ██╗░░██╗░█████╗░███╗░░██╗░█████╗░██╗
██╔════╝╚══██╔══╝██║██╔══██╗██║░██╔╝██╔════╝  ██╔══██╗██╔════╝  ██║░░██║██╔══██╗████╗░██║██╔══██╗██║
╚█████╗░░░░██║░░░██║██║░░╚═╝█████═╝░╚█████╗░  ██║░░██║█████╗░░  ███████║███████║██╔██╗██║██║░░██║██║
░╚═══██╗░░░██║░░░██║██║░░██╗██╔═██╗░░╚═══██╗  ██║░░██║██╔══╝░░  ██╔══██║██╔══██║██║╚████║██║░░██║██║
██████╔╝░░░██║░░░██║╚█████╔╝██║░╚██╗██████╔╝  ╚█████╔╝██║░░░░░  ██║░░██║██║░░██║██║░╚███║╚█████╔╝██║
╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░  ░╚════╝░╚═╝░░░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝

""")
print("\nRules are simple! \nMove weights from left to right without putting bigger values over smaller ones.\nGood luck!")

#Create the Stacks
stacks = []

left_stack=Stack("Left")
middle_stack=Stack("Middle")
right_stack=Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n(3 is recommended number to start with)\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
  
for number in reversed(range(num_disks)):
  left_stack.push(number+1)

num_optimal_moves = (2**num_disks)-1
print("\nThe fastest you can solve this game is in {num_optimal_moves} moves".format(num_optimal_moves=num_optimal_moves))

#Get User Input
def get_input():
  choices=[x.get_name()[0] for x in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {letter} for {name}".format(letter=letter,name=name))
    user_input = input("")

    for i in range(len(stacks)):
      if user_input == choices[i]:
        return stacks[i]
         
#get_input()
#Play the Game
num_user_moves = 0
def print_sticks(x,y,z):
  leftS = x.get_list_of_items()
  middleS = y.get_list_of_items()
  rightS = z.get_list_of_items()
  lists = [leftS,middleS,rightS]
  longest = 0
  for list in lists:
    if len(list) > longest:
      longest = len(list)-1
  for list in lists:
    if len(list) <= longest:
      difference = longest - len(list)
      for i in range(difference+1):
        list.insert(0,"|")
    else:
      continue

  print("\n")
  for i in range(longest+1):
    print (leftS[i],middleS[i],rightS[i])
  print ("L","M","R")
  print("\n")

while right_stack.get_size() != num_disks:
  
  print_sticks(left_stack,middle_stack,right_stack)

  while True:
    print("Which stack do you want to move from?\n")
    from_stack = get_input()
    if from_stack.is_empty() == True:
      print("Invalid move, stack is empty!")
      continue

    print ("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if to_stack.is_empty() == True or int(from_stack.peek())<int(to_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves+=1
      break
    else:
      print("Invalid move! You have to move only onto bigger values or empty stack")


while True:
  print ("\n\nYou completed the game in {x} moves, and the optimal number of moves was {y}".format(x=num_user_moves,y=num_optimal_moves))
  print("""

░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗░██████╗██╗
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░╚█████╗░██║
██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░░╚═══██╗╚═╝
╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░██████╔╝██╗
░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝
""")
  if input("press anything to exit")!="awda2324":
    break






