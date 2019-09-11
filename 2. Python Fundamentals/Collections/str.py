# length of string
len("ameer")        # 5

# Concatenation         Join should be preferred
"New" + "found" + "land"        # Newfoundland

colors = ';'.join(['#aefe23', '#234122', '#234122'])

colors          # #aefe23;#234122;#234122

''.join(['New', 'found', 'land'])     # Newfoundland

# Partition
"unforgetable".partition('forget')      # ('un', 'forget', 'able')

origin, _, destination = 'Karachi-Lahore'.partition(':')
origin      # Karachi
destination  # Lahore


# Format
'The age of {0} is {1}'.format('Ameer', 25)     # The age of Ameer is 25

'Current position {longitude} {latitude}'.format(
    longitude=22.9, latitude=11.3)     # Current position 22.9 11.3

pos = (65.2, 23.1, 12.2)
'Galactic postion x={pos[0]} y={pos[1]} z={pos[2]}'.format(
    pos=pos)         # Galactic postion x=65.2 y=23.1 z=12.2
