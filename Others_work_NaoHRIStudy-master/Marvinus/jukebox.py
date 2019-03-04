"""
Songs and corresponding keys plus timing
"""
qnotelength = 0.05; # quarter note length in seconds

song1 = [ # ode to joy 
('E',1),
('E',1),
('F',1),
('G',1),
('G',1),
('F',1),
('E',1),
('D',1),
('C',1), # C
('C',1),
('D',1),
('E',1),
('E',1),
('D',1),
('D',2), # D

('E',1),
('E',1),
('F',1),
('G',1),
('G',1),
('F',1),
('E',1), # E
('D',1),
('C',1),
('C',1),
('D',1),
('E',1),
('D',1), # D
('C',1), # 
('C',2), # C
]

song2 = [ # old mcdonald had a farm
('F',1),
('F',1),
('F',1),
('C',1),
('D',1),
('D',1),
('C',2), # C

('A',1),
('A',1),
('G',1), 
('G',1), 
('F',3), # F

('C',1),

('F',1),
('F',1),
('F',1),  
('C',1), # C
('D',1),
('D',1),
('C',2), # C

('A',1),
('A',1),
('G',1),
('G',1), # G
('F',4), # F
]

song3 = [ # jingle bells
('E',1),
('E',1),
('E',2),
('E',1),
('E',1),
('E',2),
('E',1),
('G',1),
('C',1),
('D',1),
('E',4), # E
('F',1),
('F',1),
('F',1), # F
('F',1),
('F',1),
('E',1),
('E',1), # E
('E',1),
('E',1),
('D',1),
('D',1), # D
('E',1),
('D',4),
('G',4), # G
]

song4 = [ # mary had a little lamb
('E',1),
('D',1),
('C',1),
('D',1),
('E',1),
('E',1),
('E',2), # E
('D',1),
('D',1),
('D',2),
('E',1),
('E',1),
('E',2), # E
('E',1),
('D',1),
('C',1),
('D',1),
('E',1),
('E',1), # E
('E',1),
('E',1),
('D',1),
('D',1),
('E',1),
('D',1), # D
('C',4), # D
]

song5 = [ # twinkle twinkle
('C',1),
('C',1),
('G',1),
('G',1),
('A',1),
('A',1),
('G',2), # G

('F',1), # F
('F',1),
('E',1),
('E',1), # E
('D',1),
('D',1),
('C',2), # C
]

titles = ['ode to joy', 'old mcdonald had a farm', 'jingle bells', 'mary had a little lamb', 'twinkle twinkle little star']
songslist = [song1, song2, song3, song4, song5]
songslist = [[(note, length * qnotelength) for (note,length) in song] for song in songslist]


