print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.      -'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("WELCOME TO THE TREASURE ISLAND GAME")
print("YOUR MISSION IS TO FIND THE TREASURE")
a = input("YOU'RE AT A CROSS ROAD. WHERE DO YOU WNT TO GO ? (TYPE R FOR RIGHT AND L FOR LEFT) :  \n")
if a.lower() == "l":
    print("YOU FELL INTO AN HOLE 'GAMEOVER'")
    print('''
     _________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
 ScS ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||
   / ||--_||_____||_--|| 
  (_(||)-| S123-45 |-(||)_)
    ''')
elif a.lower() == "r":
    b=input("YOU CAME INTO A LAKE. THERE IS A ISLAND IN THE MIDDLE OF THE LAKE. TYPE 'WAIT' TO WAIT FOR THE BOAT AND 'SWIM' TO SWIM ACROSS :\n")
    if b.lower() == "swim":
        print("YOU GET ATTACKED BY AN ANGRY TROUT 'GAMEOVER'")
        print('''
                            o o
                            | |
                           _L_L_
                        }\/__-__\/{
                        }(|~o.o~|){
                        }/ \`-'/ \{
                          _/`U'\_
                         ( .   . )
                        / /     \ 
                        \ |  ,  | /
                         \|=====|/
                          |_.^._|
                          | |"| |
                          ( ) ( )
                          |_| |_|
                      _.-' _j L_ '-._
                     (___.'     '.___)
            ''')
    elif b.lower() == "wait":
        c = input("YOU ARRIVED AT THE ISLAND UNHARMED. THERE A HOUSE WITH 3 DOORS. ONE RED, ONE YELLOW AND ONE BLUE. WHICH COLOUR DO YOU CHOOSE ? \n")
        if c.lower()=="red":
            print("YOU ENTERED A ROOM FULL OF BEASTS 'GAMEOVER'")
            print('''
            "Demon in overalls"
            ,-----.
           ( <> <> )
            )_ W _(
             |||||    A A A
              |||     | | |
           __/)'(\__  `-+-'
          /       //\   |
         | || ___//\ \  |
         | |/||_//\ \ \ |
         | ||||_//|  \ \|
         | ||/\_/\|   \ |
         | |/ /|\ \    \_)
         (_/  \_/  \    K
           |  | |  |    R
           |  | |  |    O
           |()| |()|    G
           |  | |  |    G
           |  | |  |    9
           |__| |__|    8
           \__/ \__/    V
                        ''')


        elif c.lower() == "blue":
            print("YOU ENTERED A ROOM FULL OF BEASTS 'GAMEOVER'")
            print('''
               "Demon in overalls"


               (                 ,&&&.
                )                .,.&&
               (  (              \=__/
                   )             ,'-'.
             (    (  ,,      _.__|/ /|
              ) /\ -((------((_|___/ |
            (  // | (`'      ((  `'--|
          _ -.;_/ ||--._      || \-._/.
         (_;-// | \ \-'.\    <_,\_\`--'|
         ( `.__ _  ___,')      <_,-'__,'
   jrei  `'(_ )_)(_)_)'

                           ''')
        elif c.lower() == "yellow":
            print("YOU found the treasure you win")
            print ('''
   _____ ____ _____
  /    /      \    |
/____ /_________\____|
\    \          /    /
   \  \        /  /
      \ \    / /
        \ \/ /
          \/
                  ''')
