#kivy==2.1.0, StarsoftheSky - Reşat Berk

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader 



         #left edge <=40  - right edge >=7    *[0,40] and [7,47] for white, [8-56] and [15,63] for black   
pawn_pos=[0,8,16,24,32,40,48,56,7,15,23,31,39,47,55,63] #-----for pawn and *king* left-right edge pos reference

castle_pos = [ tuple(range(0,8)), tuple(range(8,16)), tuple(range(16,24)), tuple(range(24,32)), tuple(range(32,40)), 
tuple(range(40,48)), tuple(range(48,56)), tuple(range(56,64))] #-----for castle right-left movement reference

chess_pieces=['pawn-b.png','castle-b.png','elephant-b.png','queen-b.png','knight-b.png','king-b.png'] #----whites eats blacks for reference

button_highlights=[] #----- save as (button, color)
old_pos = [] #----old movement pos
class ChessApp(App):

    def king_event(self, move):

        if move.background_normal =='king-b.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_king_pos = int(button_list[0])

            highlights1 = current_king_pos + 8 #---straight
            highlights2 = current_king_pos - 8 #---back
            highlights3 = current_king_pos - 1 #----left
            highlights4 = current_king_pos + 1 #----right
            highlights5 = current_king_pos + 7 #---left-cross straight
            highlights6 = current_king_pos + 9 #----right-cross straight
            highlights7 = current_king_pos - 7 #---right-cross back
            highlights8 = current_king_pos - 9 #----left-cross back

            if current_king_pos in pawn_pos[:8]: #-----------------------------left edge
                try:
                    if self.buttons.get(str(highlights1)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights2)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights4)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                        self.buttons.get(str(highlights4)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights6)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights6)),self.buttons.get(str(highlights6)).background_color])
                        self.buttons.get(str(highlights6)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights7)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights7)),self.buttons.get(str(highlights7)).background_color])
                        self.buttons.get(str(highlights7)).background_color='#76F7FF'
                except(Exception):
                    pass

            elif current_king_pos in pawn_pos[8:]: #---------------------------right edge
                try:
                    if self.buttons.get(str(highlights1)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights2)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights3)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights5)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights5)),self.buttons.get(str(highlights5)).background_color])
                        self.buttons.get(str(highlights5)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights8)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights8)),self.buttons.get(str(highlights8)).background_color])
                        self.buttons.get(str(highlights8)).background_color='#76F7FF'
                except(Exception):
                    pass

            else:
                try:
                    if self.buttons.get(str(highlights1)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights2)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights3)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights4)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                        self.buttons.get(str(highlights4)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights5)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights5)),self.buttons.get(str(highlights5)).background_color])
                        self.buttons.get(str(highlights5)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights6)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights6)),self.buttons.get(str(highlights6)).background_color])
                        self.buttons.get(str(highlights6)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights7)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights7)),self.buttons.get(str(highlights7)).background_color])
                        self.buttons.get(str(highlights7)).background_color='#76F7FF'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights8)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights8)),self.buttons.get(str(highlights8)).background_color])
                        self.buttons.get(str(highlights8)).background_color='#76F7FF'
                except(Exception):
                    pass

        elif move.background_normal =='king-w.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_king_pos = int(button_list[0])

            highlights1 = current_king_pos - 8 #---straight
            highlights2 = current_king_pos + 8 #---back
            highlights3 = current_king_pos - 1 #----left
            highlights4 = current_king_pos + 1 #----right
            highlights5 = current_king_pos - 9 #---left-cross straight
            highlights6 = current_king_pos - 7 #----right-cross straight
            highlights7 = current_king_pos + 9 #---right-cross back
            highlights8 = current_king_pos + 7 #----left-cross back

            if current_king_pos in pawn_pos[:8]: #-----------------------------left edge
                try:
                    if self.buttons.get(str(highlights1)).background_normal in chess_pieces or self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights2)).background_normal in chess_pieces or self.buttons.get(str(highlights2)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights4)).background_normal in chess_pieces or self.buttons.get(str(highlights4)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                        self.buttons.get(str(highlights4)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights6)).background_normal in chess_pieces or self.buttons.get(str(highlights6)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights6)),self.buttons.get(str(highlights6)).background_color])
                        self.buttons.get(str(highlights6)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights7)).background_normal in chess_pieces or self.buttons.get(str(highlights7)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights7)),self.buttons.get(str(highlights7)).background_color])
                        self.buttons.get(str(highlights7)).background_color='#FFFF75'
                except(Exception):
                    pass

            elif current_king_pos in pawn_pos[8:]: #---------------------------right edge
                try:
                    if self.buttons.get(str(highlights1)).background_normal in chess_pieces or self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights2)).background_normal in chess_pieces or self.buttons.get(str(highlights2)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights3)).background_normal in chess_pieces or self.buttons.get(str(highlights3)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights5)).background_normal in chess_pieces or self.buttons.get(str(highlights5)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights5)),self.buttons.get(str(highlights5)).background_color])
                        self.buttons.get(str(highlights5)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights8)).background_normal in chess_pieces or self.buttons.get(str(highlights8)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights8)),self.buttons.get(str(highlights8)).background_color])
                        self.buttons.get(str(highlights8)).background_color='#FFFF75'
                except(Exception):
                    pass

            else:
                try:
                    if self.buttons.get(str(highlights1)).background_normal in chess_pieces or self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights2)).background_normal in chess_pieces or self.buttons.get(str(highlights2)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights3)).background_normal in chess_pieces or self.buttons.get(str(highlights3)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights4)).background_normal in chess_pieces or self.buttons.get(str(highlights4)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                        self.buttons.get(str(highlights4)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights5)).background_normal in chess_pieces or self.buttons.get(str(highlights5)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights5)),self.buttons.get(str(highlights5)).background_color])
                        self.buttons.get(str(highlights5)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights6)).background_normal in chess_pieces or self.buttons.get(str(highlights6)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights6)),self.buttons.get(str(highlights6)).background_color])
                        self.buttons.get(str(highlights6)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights7)).background_normal in chess_pieces or self.buttons.get(str(highlights7)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights7)),self.buttons.get(str(highlights7)).background_color])
                        self.buttons.get(str(highlights7)).background_color='#FFFF75'
                except(Exception):
                    pass

                try:
                    if self.buttons.get(str(highlights8)).background_normal in chess_pieces or self.buttons.get(str(highlights8)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights8)),self.buttons.get(str(highlights8)).background_color])
                        self.buttons.get(str(highlights8)).background_color='#FFFF75'
                except(Exception):
                    pass



    def queen_event(self, move):

        if move.background_normal =='queen-b.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_queen_pos = int(button_list[0])

            try:
                for h1 in range(current_queen_pos, 64, +9): #--------------highlights left-cross
                    if self.buttons.get(str(h1)).background_normal =='' and self.buttons.get(str(h1)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                        self.buttons.get(str(h1)).background_color='#76F7FF'
                        
                    elif self.buttons.get(str(h1)).background_normal !='' and h1 != current_queen_pos:         #----highlight for enemy before break!
                        if self.buttons.get(str(h1)).background_normal not in chess_pieces and self.buttons.get(str(h1)).background_color == move.background_color: 
                             button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                             self.buttons.get(str(h1)).background_color='#76F7FF'
                        break
            except(Exception):
                pass

            try:
                for h2 in range(current_queen_pos, -1, -9): #--------------left-cross-back
                    if self.buttons.get(str(h2)).background_normal =='' and self.buttons.get(str(h2)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                        self.buttons.get(str(h2)).background_color='#76F7FF'
                            
                    elif self.buttons.get(str(h2)).background_normal !='' and h2 != current_queen_pos:    
                        if self.buttons.get(str(h2)).background_normal not in chess_pieces and self.buttons.get(str(h2)).background_color == move.background_color:
                            button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                            self.buttons.get(str(h2)).background_color='#76F7FF'
                        break
            except(Exception):
                pass

            try:
                for h3 in range(current_queen_pos, 64, +7): #--------------highlights right-cross
                    if self.buttons.get(str(h3)).background_normal =='' and self.buttons.get(str(h3)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                        self.buttons.get(str(h3)).background_color='#76F7FF'
                        
                    elif self.buttons.get(str(h3)).background_normal !='' and h3 != current_queen_pos:         #----highlight for enemy before break!
                        if self.buttons.get(str(h3)).background_normal not in chess_pieces and self.buttons.get(str(h3)).background_color == move.background_color: 
                             button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                             self.buttons.get(str(h3)).background_color='#76F7FF'
                        break
            except(Exception):
                pass

            
            for h4 in range(current_queen_pos, -1, -7): #--------------right-cross-back
                if self.buttons.get(str(h4)).background_normal =='' and self.buttons.get(str(h4)).background_color == move.background_color:
                    button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                    self.buttons.get(str(h4)).background_color='#76F7FF'
                        
                elif self.buttons.get(str(h4)).background_normal !='' and h4 != current_queen_pos:    
                    if self.buttons.get(str(h4)).background_normal not in chess_pieces and self.buttons.get(str(h4)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                        self.buttons.get(str(h4)).background_color='#76F7FF'
                    break

            for h1 in range(current_queen_pos, 64, +8): #--------------highlights for straight
                if self.buttons.get(str(h1)).background_normal =='':
                    button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                    self.buttons.get(str(h1)).background_color='#76F7FF'
                    
                elif self.buttons.get(str(h1)).background_normal !='' and h1 != current_queen_pos:
                    if self.buttons.get(str(h1)).background_normal not in chess_pieces: #highlight for enemy before break!
                        button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                        self.buttons.get(str(h1)).background_color='#76F7FF'
                    break
                
            for h2 in range(current_queen_pos, -1, -8):  #--------------highlights for back
                if self.buttons.get(str(h2)).background_normal =='':
                    button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                    self.buttons.get(str(h2)).background_color='#76F7FF'
                    
                elif self.buttons.get(str(h2)).background_normal !='' and h2 != current_queen_pos:
                    if self.buttons.get(str(h2)).background_normal not in chess_pieces: #highlight for enemy before break!
                        button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                        self.buttons.get(str(h2)).background_color='#76F7FF'
                    break
                

            for r in castle_pos:
                if current_queen_pos in r:  #----------------------highlights for right 
                    for h3 in range(current_queen_pos, r[-1]+1 , 1): 
                        if self.buttons.get(str(h3)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                            self.buttons.get(str(h3)).background_color='#76F7FF'
                        elif self.buttons.get(str(h3)).background_normal !='' and h3 != current_queen_pos:
                            if self.buttons.get(str(h3)).background_normal not in chess_pieces: #highlight for enemy before break!
                                button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                                self.buttons.get(str(h3)).background_color='#76F7FF'
                            break

            for l in castle_pos: 
                if current_queen_pos in l:  #----------------------highlights for left
                    for h4 in range(current_queen_pos, l[0]-1 , -1): 
                        if self.buttons.get(str(h4)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                            self.buttons.get(str(h4)).background_color='#76F7FF'
                        elif self.buttons.get(str(h4)).background_normal !='' and h4 != current_queen_pos:
                            if self.buttons.get(str(h4)).background_normal not in chess_pieces: #highlight for enemy before break!
                                button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                                self.buttons.get(str(h4)).background_color='#76F7FF'
                            break

        elif move.background_normal == 'queen-w.png':   #--------Combine elephant and castle movement here copy-paste!
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_queen_pos = int(button_list[0])

            for h1 in range(current_queen_pos, -1, -8): #--------------highlights for straight
                if self.buttons.get(str(h1)).background_normal =='':
                    button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                    self.buttons.get(str(h1)).background_color='#FFFF75'
                    
                elif self.buttons.get(str(h1)).background_normal !='' and h1 != current_queen_pos:
                    if self.buttons.get(str(h1)).background_normal in chess_pieces: #highlight for enemy before break!
                        button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                        self.buttons.get(str(h1)).background_color='#FFFF75'
                    break
                
            for h2 in range(current_queen_pos, 64, 8):  #--------------highlights for back
                if self.buttons.get(str(h2)).background_normal =='':
                    button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                    self.buttons.get(str(h2)).background_color='#FFFF75'
                    
                elif self.buttons.get(str(h2)).background_normal !='' and h2 != current_queen_pos:
                    if self.buttons.get(str(h2)).background_normal in chess_pieces: #highlight for enemy before break!
                        button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                        self.buttons.get(str(h2)).background_color='#FFFF75'
                    break
                

            for r in castle_pos:
                if current_queen_pos in r:  #----------------------highlights for right 
                    for h3 in range(current_queen_pos, r[-1]+1 , 1): 
                        if self.buttons.get(str(h3)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                            self.buttons.get(str(h3)).background_color='#FFFF75'
                        elif self.buttons.get(str(h3)).background_normal !='' and h3 != current_queen_pos:
                            if self.buttons.get(str(h3)).background_normal in chess_pieces: #highlight for enemy before break!
                                button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                                self.buttons.get(str(h3)).background_color='#FFFF75'
                            break

            for l in castle_pos: 
                if current_queen_pos in l:  #----------------------highlights for left
                    for h4 in range(current_queen_pos, l[0]-1 , -1): 
                        if self.buttons.get(str(h4)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                            self.buttons.get(str(h4)).background_color='#FFFF75'
                        elif self.buttons.get(str(h4)).background_normal !='' and h4 != current_queen_pos:
                            if self.buttons.get(str(h4)).background_normal in chess_pieces: #highlight for enemy before break!
                                button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                                self.buttons.get(str(h4)).background_color='#FFFF75'
                            break

            try:
                for h1 in range(current_queen_pos, -1, -9): #--------------highlights left-cross
                    if self.buttons.get(str(h1)).background_normal =='' and self.buttons.get(str(h1)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                        self.buttons.get(str(h1)).background_color='#FFFF75'
                        
                    elif self.buttons.get(str(h1)).background_normal !='' and h1 != current_queen_pos:         #----highlight for enemy before break!
                        if self.buttons.get(str(h1)).background_normal in chess_pieces and self.buttons.get(str(h1)).background_color == move.background_color: 
                             button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                             self.buttons.get(str(h1)).background_color='#FFFF75'
                        break
            except(Exception):
                pass

            try:
                for h2 in range(current_queen_pos, 64, 9): #--------------left-cross-back
                    if self.buttons.get(str(h2)).background_normal =='' and self.buttons.get(str(h2)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                        self.buttons.get(str(h2)).background_color='#FFFF75'
                            
                    elif self.buttons.get(str(h2)).background_normal !='' and h2 != current_queen_pos:    
                        if self.buttons.get(str(h2)).background_normal in chess_pieces and self.buttons.get(str(h2)).background_color == move.background_color:
                            button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                            self.buttons.get(str(h2)).background_color='#FFFF75'
                        break
            except(Exception):
                pass

            try:
                for h3 in range(current_queen_pos, -1, -7): #--------------highlights right-cross
                    if self.buttons.get(str(h3)).background_normal =='' and self.buttons.get(str(h3)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                        self.buttons.get(str(h3)).background_color='#FFFF75'
                        
                    elif self.buttons.get(str(h3)).background_normal !='' and h3 != current_queen_pos:         #----highlight for enemy before break!
                        if self.buttons.get(str(h3)).background_normal in chess_pieces and self.buttons.get(str(h3)).background_color == move.background_color: 
                             button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                             self.buttons.get(str(h3)).background_color='#FFFF75'
                        break
            except(Exception):
                pass

            
            for h4 in range(current_queen_pos, 64, 7): #--------------right-cross-back
                if self.buttons.get(str(h4)).background_normal =='' and self.buttons.get(str(h4)).background_color == move.background_color:
                    button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                    self.buttons.get(str(h4)).background_color='#FFFF75'
                        
                elif self.buttons.get(str(h4)).background_normal !='' and h4 != current_queen_pos:    
                    if self.buttons.get(str(h4)).background_normal in chess_pieces and self.buttons.get(str(h4)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                        self.buttons.get(str(h4)).background_color='#FFFF75'
                    break
    def elephant_event(self,move):

        if move.background_normal == 'elephant-b.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_elephant_pos = int(button_list[0])

            try:
                for h1 in range(current_elephant_pos, 64, +9): #--------------highlights left-cross
                    if self.buttons.get(str(h1)).background_normal =='' and self.buttons.get(str(h1)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                        self.buttons.get(str(h1)).background_color='#76F7FF'
                        
                    elif self.buttons.get(str(h1)).background_normal !='' and h1 != current_elephant_pos:         #----highlight for enemy before break!
                        if self.buttons.get(str(h1)).background_normal not in chess_pieces and self.buttons.get(str(h1)).background_color == move.background_color: 
                             button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                             self.buttons.get(str(h1)).background_color='#76F7FF'
                        break
            except(Exception):
                pass

            try:
                for h2 in range(current_elephant_pos, -1, -9): #--------------left-cross-back
                    if self.buttons.get(str(h2)).background_normal =='' and self.buttons.get(str(h2)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                        self.buttons.get(str(h2)).background_color='#76F7FF'
                            
                    elif self.buttons.get(str(h2)).background_normal !='' and h2 != current_elephant_pos:    
                        if self.buttons.get(str(h2)).background_normal not in chess_pieces and self.buttons.get(str(h2)).background_color == move.background_color:
                            button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                            self.buttons.get(str(h2)).background_color='#76F7FF'
                        break
            except(Exception):
                pass

            try:
                for h3 in range(current_elephant_pos, 64, +7): #--------------highlights right-cross
                    if self.buttons.get(str(h3)).background_normal =='' and self.buttons.get(str(h3)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                        self.buttons.get(str(h3)).background_color='#76F7FF'
                        
                    elif self.buttons.get(str(h3)).background_normal !='' and h3 != current_elephant_pos:         #----highlight for enemy before break!
                        if self.buttons.get(str(h3)).background_normal not in chess_pieces and self.buttons.get(str(h3)).background_color == move.background_color: 
                             button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                             self.buttons.get(str(h3)).background_color='#76F7FF'
                        break
            except(Exception):
                pass

            
            for h4 in range(current_elephant_pos, -1, -7): #--------------right-cross-back
                if self.buttons.get(str(h4)).background_normal =='' and self.buttons.get(str(h4)).background_color == move.background_color:
                    button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                    self.buttons.get(str(h4)).background_color='#76F7FF'
                        
                elif self.buttons.get(str(h4)).background_normal !='' and h4 != current_elephant_pos:    
                    if self.buttons.get(str(h4)).background_normal not in chess_pieces and self.buttons.get(str(h4)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                        self.buttons.get(str(h4)).background_color='#76F7FF'
                    break

        elif move.background_normal == 'elephant-w.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_elephant_pos = int(button_list[0])

            try:
                for h1 in range(current_elephant_pos, -1, -9): #--------------highlights left-cross
                    if self.buttons.get(str(h1)).background_normal =='' and self.buttons.get(str(h1)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                        self.buttons.get(str(h1)).background_color='#FFFF75'
                        
                    elif self.buttons.get(str(h1)).background_normal !='' and h1 != current_elephant_pos:         #----highlight for enemy before break!
                        if self.buttons.get(str(h1)).background_normal in chess_pieces and self.buttons.get(str(h1)).background_color == move.background_color: 
                             button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                             self.buttons.get(str(h1)).background_color='#FFFF75'
                        break
            except(Exception):
                pass

            try:
                for h2 in range(current_elephant_pos, 64, 9): #--------------left-cross-back
                    if self.buttons.get(str(h2)).background_normal =='' and self.buttons.get(str(h2)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                        self.buttons.get(str(h2)).background_color='#FFFF75'
                            
                    elif self.buttons.get(str(h2)).background_normal !='' and h2 != current_elephant_pos:    
                        if self.buttons.get(str(h2)).background_normal in chess_pieces and self.buttons.get(str(h2)).background_color == move.background_color:
                            button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                            self.buttons.get(str(h2)).background_color='#FFFF75'
                        break
            except(Exception):
                pass

            try:
                for h3 in range(current_elephant_pos, -1, -7): #--------------highlights right-cross
                    if self.buttons.get(str(h3)).background_normal =='' and self.buttons.get(str(h3)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                        self.buttons.get(str(h3)).background_color='#FFFF75'
                        
                    elif self.buttons.get(str(h3)).background_normal !='' and h3 != current_elephant_pos:         #----highlight for enemy before break!
                        if self.buttons.get(str(h3)).background_normal in chess_pieces and self.buttons.get(str(h3)).background_color == move.background_color: 
                             button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                             self.buttons.get(str(h3)).background_color='#FFFF75'
                        break
            except(Exception):
                pass

            
            for h4 in range(current_elephant_pos, 64, 7): #--------------right-cross-back
                if self.buttons.get(str(h4)).background_normal =='' and self.buttons.get(str(h4)).background_color == move.background_color:
                    button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                    self.buttons.get(str(h4)).background_color='#FFFF75'
                        
                elif self.buttons.get(str(h4)).background_normal !='' and h4 != current_elephant_pos:    
                    if self.buttons.get(str(h4)).background_normal in chess_pieces and self.buttons.get(str(h4)).background_color == move.background_color:
                        button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                        self.buttons.get(str(h4)).background_color='#FFFF75'
                    break
           
            
            
    def knight_event(self, move):

        if move.background_normal == 'knight-b.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_knight_pos = int(button_list[0])

            try:
                highlights1 = current_knight_pos +17
                if (self.buttons.get(str(highlights1)).background_normal =='' or self.buttons.get(str(highlights1)).background_normal not in chess_pieces) and self.buttons.get(str(highlights1)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#76F7FF'
            except(Exception):
                pass

            try:
                highlights2 = current_knight_pos +15
                if (self.buttons.get(str(highlights2)).background_normal =='' or self.buttons.get(str(highlights2)).background_normal not in chess_pieces) and self.buttons.get(str(highlights2)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                    self.buttons.get(str(highlights2)).background_color='#76F7FF'
            except(Exception):
                pass

            try:
                highlights3 = current_knight_pos +10
                if (self.buttons.get(str(highlights3)).background_normal =='' or self.buttons.get(str(highlights3)).background_normal not in chess_pieces) and self.buttons.get(str(highlights3)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                    self.buttons.get(str(highlights3)).background_color='#76F7FF'
            except(Exception):
                pass

            try:
                highlights4 = current_knight_pos +6
                if (self.buttons.get(str(highlights4)).background_normal =='' or self.buttons.get(str(highlights4)).background_normal not in chess_pieces) and self.buttons.get(str(highlights4)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                    self.buttons.get(str(highlights4)).background_color='#76F7FF'
            except(Exception):
                pass

            try:
                highlights5 = current_knight_pos -6
                if (self.buttons.get(str(highlights5)).background_normal =='' or self.buttons.get(str(highlights5)).background_normal not in chess_pieces) and self.buttons.get(str(highlights5)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights5)),self.buttons.get(str(highlights5)).background_color])
                    self.buttons.get(str(highlights5)).background_color='#76F7FF'
            except(Exception):
                pass

            try:
                highlights6 = current_knight_pos -10
                if (self.buttons.get(str(highlights6)).background_normal =='' or self.buttons.get(str(highlights6)).background_normal not in chess_pieces) and self.buttons.get(str(highlights6)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights6)),self.buttons.get(str(highlights6)).background_color])
                    self.buttons.get(str(highlights6)).background_color='#76F7FF'
            except(Exception):
                pass

            try:
                highlights7 = current_knight_pos -15
                if (self.buttons.get(str(highlights7)).background_normal =='' or self.buttons.get(str(highlights7)).background_normal not in chess_pieces) and self.buttons.get(str(highlights7)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights7)),self.buttons.get(str(highlights7)).background_color])
                    self.buttons.get(str(highlights7)).background_color='#76F7FF'
            except(Exception):
                pass

            try:
                highlights8 = current_knight_pos -17
                if (self.buttons.get(str(highlights8)).background_normal =='' or self.buttons.get(str(highlights8)).background_normal not in chess_pieces) and self.buttons.get(str(highlights8)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights8)),self.buttons.get(str(highlights8)).background_color])
                    self.buttons.get(str(highlights8)).background_color='#76F7FF'
            except(Exception):
                pass

        elif move.background_normal == 'knight-w.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_knight_pos = int(button_list[0])

            try:
                highlights1 = current_knight_pos -17
                if (self.buttons.get(str(highlights1)).background_normal =='' or self.buttons.get(str(highlights1)).background_normal in chess_pieces) and self.buttons.get(str(highlights1)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#FFFF75'
            except(Exception):
                pass

            try:
                highlights2 = current_knight_pos -15
                if (self.buttons.get(str(highlights2)).background_normal =='' or self.buttons.get(str(highlights2)).background_normal in chess_pieces) and self.buttons.get(str(highlights2)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                    self.buttons.get(str(highlights2)).background_color='#FFFF75'
            except(Exception):
                pass

            try:
                highlights3 = current_knight_pos -10
                if (self.buttons.get(str(highlights3)).background_normal =='' or self.buttons.get(str(highlights3)).background_normal in chess_pieces) and self.buttons.get(str(highlights3)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                    self.buttons.get(str(highlights3)).background_color='#FFFF75'
            except(Exception):
                pass

            try:
                highlights4 = current_knight_pos -6
                if (self.buttons.get(str(highlights4)).background_normal =='' or self.buttons.get(str(highlights4)).background_normal in chess_pieces) and self.buttons.get(str(highlights4)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                    self.buttons.get(str(highlights4)).background_color='#FFFF75'
            except(Exception):
                pass

            try:
                highlights5 = current_knight_pos +6
                if (self.buttons.get(str(highlights5)).background_normal =='' or self.buttons.get(str(highlights5)).background_normal in chess_pieces) and self.buttons.get(str(highlights5)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights5)),self.buttons.get(str(highlights5)).background_color])
                    self.buttons.get(str(highlights5)).background_color='#FFFF75'
            except(Exception):
                pass

            try:
                highlights6 = current_knight_pos +10
                if (self.buttons.get(str(highlights6)).background_normal =='' or self.buttons.get(str(highlights6)).background_normal in chess_pieces) and self.buttons.get(str(highlights6)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights6)),self.buttons.get(str(highlights6)).background_color])
                    self.buttons.get(str(highlights6)).background_color='#FFFF75'
            except(Exception):
                pass

            try:
                highlights7 = current_knight_pos +15
                if (self.buttons.get(str(highlights7)).background_normal =='' or self.buttons.get(str(highlights7)).background_normal in chess_pieces) and self.buttons.get(str(highlights7)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights7)),self.buttons.get(str(highlights7)).background_color])
                    self.buttons.get(str(highlights7)).background_color='#FFFF75'
            except(Exception):
                pass

            try:
                highlights8 = current_knight_pos +17
                if (self.buttons.get(str(highlights8)).background_normal =='' or self.buttons.get(str(highlights8)).background_normal in chess_pieces) and self.buttons.get(str(highlights8)).background_color != move.background_color:
                    button_highlights.append([self.buttons.get(str(highlights8)),self.buttons.get(str(highlights8)).background_color])
                    self.buttons.get(str(highlights8)).background_color='#FFFF75'
            except(Exception):
                pass


    def castle_event(self,move):

        if move.background_normal == 'castle-b.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_castle_pos = int(button_list[0])
        
            for h1 in range(current_castle_pos, 64, +8): #--------------highlights for straight
                if self.buttons.get(str(h1)).background_normal =='':
                    button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                    self.buttons.get(str(h1)).background_color='#76F7FF'
                    
                elif self.buttons.get(str(h1)).background_normal !='' and h1 != current_castle_pos:
                    if self.buttons.get(str(h1)).background_normal not in chess_pieces: #highlight for enemy before break!
                        button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                        self.buttons.get(str(h1)).background_color='#76F7FF'
                    break
                
            for h2 in range(current_castle_pos, -1, -8):  #--------------highlights for back
                if self.buttons.get(str(h2)).background_normal =='':
                    button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                    self.buttons.get(str(h2)).background_color='#76F7FF'
                    
                elif self.buttons.get(str(h2)).background_normal !='' and h2 != current_castle_pos:
                    if self.buttons.get(str(h2)).background_normal not in chess_pieces: #highlight for enemy before break!
                        button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                        self.buttons.get(str(h2)).background_color='#76F7FF'
                    break
                

            for r in castle_pos:
                if current_castle_pos in r:  #----------------------highlights for right 
                    for h3 in range(current_castle_pos, r[-1]+1 , 1): 
                        if self.buttons.get(str(h3)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                            self.buttons.get(str(h3)).background_color='#76F7FF'
                        elif self.buttons.get(str(h3)).background_normal !='' and h3 != current_castle_pos:
                            if self.buttons.get(str(h3)).background_normal not in chess_pieces: #highlight for enemy before break!
                                button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                                self.buttons.get(str(h3)).background_color='#76F7FF'
                            break

            for l in castle_pos: 
                if current_castle_pos in l:  #----------------------highlights for left
                    for h4 in range(current_castle_pos, l[0]-1 , -1): 
                        if self.buttons.get(str(h4)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                            self.buttons.get(str(h4)).background_color='#76F7FF'
                        elif self.buttons.get(str(h4)).background_normal !='' and h4 != current_castle_pos:
                            if self.buttons.get(str(h4)).background_normal not in chess_pieces: #highlight for enemy before break!
                                button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                                self.buttons.get(str(h4)).background_color='#76F7FF'
                            break

        elif move.background_normal == 'castle-w.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            current_castle_pos = int(button_list[0])
        
            for h1 in range(current_castle_pos, -1, -8): #--------------highlights for straight
                if self.buttons.get(str(h1)).background_normal =='':
                    button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                    self.buttons.get(str(h1)).background_color='#FFFF75'
                    
                elif self.buttons.get(str(h1)).background_normal !='' and h1 != current_castle_pos:
                    if self.buttons.get(str(h1)).background_normal in chess_pieces: #highlight for enemy before break!
                        button_highlights.append([self.buttons.get(str(h1)),self.buttons.get(str(h1)).background_color])
                        self.buttons.get(str(h1)).background_color='#FFFF75'
                    break
                
            for h2 in range(current_castle_pos, 64, 8):  #--------------highlights for back
                if self.buttons.get(str(h2)).background_normal =='':
                    button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                    self.buttons.get(str(h2)).background_color='#FFFF75'
                    
                elif self.buttons.get(str(h2)).background_normal !='' and h2 != current_castle_pos:
                    if self.buttons.get(str(h2)).background_normal in chess_pieces: #highlight for enemy before break!
                        button_highlights.append([self.buttons.get(str(h2)),self.buttons.get(str(h2)).background_color])
                        self.buttons.get(str(h2)).background_color='#FFFF75'
                    break
                

            for r in castle_pos:
                if current_castle_pos in r:  #----------------------highlights for right 
                    for h3 in range(current_castle_pos, r[-1]+1 , 1): 
                        if self.buttons.get(str(h3)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                            self.buttons.get(str(h3)).background_color='#FFFF75'
                        elif self.buttons.get(str(h3)).background_normal !='' and h3 != current_castle_pos:
                            if self.buttons.get(str(h3)).background_normal in chess_pieces: #highlight for enemy before break!
                                button_highlights.append([self.buttons.get(str(h3)),self.buttons.get(str(h3)).background_color])
                                self.buttons.get(str(h3)).background_color='#FFFF75'
                            break

            for l in castle_pos: 
                if current_castle_pos in l:  #----------------------highlights for left
                    for h4 in range(current_castle_pos, l[0]-1 , -1): 
                        if self.buttons.get(str(h4)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                            self.buttons.get(str(h4)).background_color='#FFFF75'
                        elif self.buttons.get(str(h4)).background_normal !='' and h4 != current_castle_pos:
                            if self.buttons.get(str(h4)).background_normal in chess_pieces: #highlight for enemy before break!
                                button_highlights.append([self.buttons.get(str(h4)),self.buttons.get(str(h4)).background_color])
                                self.buttons.get(str(h4)).background_color='#FFFF75'
                            break
                    
                        

    def pawn_event(self,move):                                                              

        if move.background_normal == 'pawn-b.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            if int(button_list[0]) > 7 and int(button_list[0]) < 16:
                highlights1=int(button_list[0]) + 8
                highlights2=int(button_list[0]) + 16   #------------------------------first step for pawn -double or one step- 
                highlights3 = int(button_list[0]) + 7 #---left cross
                highlights4 = int(button_list[0]) + 9 #---right cross
                if (self.buttons.get(str(highlights1)).background_normal =='' and self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights4)).background_normal not in chess_pieces
                and self.buttons.get(str(highlights3)).background_normal !='' and self.buttons.get(str(highlights4)).background_normal !=''):
                    if self.buttons.get(str(highlights2)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                    button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#76F7FF'
                    self.buttons.get(str(highlights3)).background_color='#76F7FF'
                    self.buttons.get(str(highlights4)).background_color='#76F7FF'
                    

                elif self.buttons.get(str(highlights1)).background_normal !='' and (self.buttons.get(str(highlights3)).background_normal not in chess_pieces or self.buttons.get(str(highlights4)).background_normal not in chess_pieces):
                    if (self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights4)).background_normal not in chess_pieces 
                    and (self.buttons.get(str(highlights3)).background_normal !='' and self.buttons.get(str(highlights4)).background_normal !='')):
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                        self.buttons.get(str(highlights4)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights3)).background_normal !=''
                        and (self.buttons.get(str(highlights4)).background_normal in chess_pieces or self.buttons.get(str(highlights4)).background_normal =='')):
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights4)).background_normal not in chess_pieces and self.buttons.get(str(highlights4)).background_normal !=''
                        and (self.buttons.get(str(highlights3)).background_normal in chess_pieces or self.buttons.get(str(highlights3)).background_normal =='')):
                        button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                        self.buttons.get(str(highlights4)).background_color='#76F7FF'
                    else:
                        pass



                elif self.buttons.get(str(highlights1)).background_normal == '' and (self.buttons.get(str(highlights3)).background_normal not in chess_pieces or self.buttons.get(str(highlights4)).background_normal not in chess_pieces):
                    if self.buttons.get(str(highlights2)).background_normal =='' or self.buttons.get(str(highlights2)).background_normal !='':
                        if self.buttons.get(str(highlights2)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                            self.buttons.get(str(highlights2)).background_color='#76F7FF'

                        if (self.buttons.get(str(highlights3)).background_normal not in chess_pieces and (self.buttons.get(str(highlights4)).background_normal in chess_pieces or self.buttons.get(str(highlights4)).background_normal =='')
                        and self.buttons.get(str(highlights3)).background_normal !='') :
                            button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                            self.buttons.get(str(highlights3)).background_color='#76F7FF'
                        elif (self.buttons.get(str(highlights4)).background_normal not in chess_pieces and (self.buttons.get(str(highlights3)).background_normal in chess_pieces or self.buttons.get(str(highlights3)).background_normal =='')
                        and self.buttons.get(str(highlights4)).background_normal !='') :
                            button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                            self.buttons.get(str(highlights4)).background_color='#76F7FF'
                
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#76F7FF'


                elif self.buttons.get(str(highlights1)).background_normal == '' and self.buttons.get(str(highlights2)).background_normal !='':
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#76F7FF'

                elif self.buttons.get(str(highlights1)).background_normal !='':
                    pass

                else:
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#76F7FF'
                    self.buttons.get(str(highlights2)).background_color='#76F7FF'

            elif int(button_list[0]) < 64 and int(button_list[0]) >= 15:  #pawn_pos=[0,8,16,24,32,40,48,56,7,15,23,31,39,47,55,63]

                if int(button_list[0]) in pawn_pos[1:8]: #--------------------------left-edge
                    highlights1=int(button_list[0]) + 8    #--straight--
                    highlights2 = int(button_list[0]) + 9 #--right cross--
                    if self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal =='' and self.buttons.get(str(highlights2)).background_normal !='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                    elif self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal !='' and self.buttons.get(str(highlights2)).background_normal !='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                    elif self.buttons.get(str(highlights1)).background_normal !='' and (self.buttons.get(str(highlights2)).background_normal in chess_pieces or self.buttons.get(str(highlights2)).background_normal ==''):
                        pass                                              
                    else:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'


                elif int(button_list[0]) in pawn_pos[9:]: #--------------------------right-edge
                    highlights1=int(button_list[0])+8    #--straight--
                    highlights2 = int(button_list[0])+7 #--left cross--
                    if self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal =='' and self.buttons.get(str(highlights2)).background_normal !='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                    elif self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal !='' and self.buttons.get(str(highlights2)).background_normal !='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                    elif self.buttons.get(str(highlights1)).background_normal !='' and (self.buttons.get(str(highlights2)).background_normal in chess_pieces or self.buttons.get(str(highlights2)).background_normal ==''):
                        pass                                              
                    else:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'

                else:
                    highlights1=int(button_list[0]) + 8    #-------------right-left cross
                    highlights2 = int(button_list[0]) + 9 #--right cross--
                    highlights3 = int(button_list[0]) + 7 #--left cross--
                    if (self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal !=''
                        and self.buttons.get(str(highlights2)).background_normal !='' and self.buttons.get(str(highlights3)).background_normal !=''):
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal ==''
                        and self.buttons.get(str(highlights2)).background_normal !='' and self.buttons.get(str(highlights3)).background_normal !=''):
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights2)).background_normal not in chess_pieces and (self.buttons.get(str(highlights3)).background_normal =='' or self.buttons.get(str(highlights3)).background_normal in chess_pieces) and self.buttons.get(str(highlights1)).background_normal !=''
                        and self.buttons.get(str(highlights2)).background_normal !=''):
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights3)).background_normal =='' and self.buttons.get(str(highlights1)).background_normal ==''
                        and self.buttons.get(str(highlights2)).background_normal !=''):
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights3)).background_normal not in chess_pieces and (self.buttons.get(str(highlights2)).background_normal =='' or self.buttons.get(str(highlights2)).background_normal in chess_pieces) and self.buttons.get(str(highlights1)).background_normal !=''
                        and self.buttons.get(str(highlights3)).background_normal != ''): 
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights2)).background_normal =='' and self.buttons.get(str(highlights1)).background_normal ==''
                        and self.buttons.get(str(highlights3)).background_normal !=''):
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights1)).background_normal ==''
                        and self.buttons.get(str(highlights3)).background_normal !=''):
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                        self.buttons.get(str(highlights3)).background_color='#76F7FF'
                    elif (self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal ==''
                        and self.buttons.get(str(highlights2)).background_normal !=''):
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'
                        self.buttons.get(str(highlights2)).background_color='#76F7FF'
                    elif self.buttons.get(str(highlights1)).background_normal !='':
                        pass
                    else:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#76F7FF'



        elif move.background_normal == 'pawn-w.png':
            button_list = [key for key, value in self.buttons.items() if value == move]
            if int(button_list[0]) > 47 and int(button_list[0]) < 56:
                highlights1=int(button_list[0]) - 8
                highlights2=int(button_list[0]) - 16  #------------------------------first step for pawn -double or one step-
                highlights3 = int(button_list[0]) - 7 #---right cross
                highlights4 = int(button_list[0]) - 9 #---left cross
    
                if self.buttons.get(str(highlights1)).background_normal =='' and self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights4)).background_normal in chess_pieces:
                    if self.buttons.get(str(highlights2)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                    button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#FFFF75'
                    self.buttons.get(str(highlights3)).background_color='#FFFF75'
                    self.buttons.get(str(highlights4)).background_color='#FFFF75'

                elif self.buttons.get(str(highlights1)).background_normal !='' and (self.buttons.get(str(highlights3)).background_normal in chess_pieces or self.buttons.get(str(highlights4)).background_normal in chess_pieces):
                    if self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights4)).background_normal in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                        self.buttons.get(str(highlights4)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights4)).background_normal not in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                    else:
                        button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                        self.buttons.get(str(highlights4)).background_color='#FFFF75'


                elif self.buttons.get(str(highlights1)).background_normal == '' and (self.buttons.get(str(highlights3)).background_normal in chess_pieces or self.buttons.get(str(highlights4)).background_normal in chess_pieces):
                    if self.buttons.get(str(highlights2)).background_normal =='' or self.buttons.get(str(highlights2)).background_normal !='':
                        if self.buttons.get(str(highlights2)).background_normal =='':
                            button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                            self.buttons.get(str(highlights2)).background_color='#FFFF75'
                        if self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights4)).background_normal not in chess_pieces:
                            button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                            self.buttons.get(str(highlights3)).background_color='#FFFF75'
                        else:
                            button_highlights.append([self.buttons.get(str(highlights4)),self.buttons.get(str(highlights4)).background_color])
                            self.buttons.get(str(highlights4)).background_color='#FFFF75'

                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#FFFF75'

                elif self.buttons.get(str(highlights1)).background_normal == '' and self.buttons.get(str(highlights2)).background_normal !='':
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#FFFF75'

                elif self.buttons.get(str(highlights1)).background_normal !='':
                    pass

                else:
                    button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                    button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                    self.buttons.get(str(highlights1)).background_color='#FFFF75'
                    self.buttons.get(str(highlights2)).background_color='#FFFF75'

            elif int(button_list[0]) < 48 and int(button_list[0]) >= 0: 

                if int(button_list[0]) in pawn_pos[:6]: #--------------------------left-edge
                    highlights1=int(button_list[0])-8    #--straight--
                    highlights2 = int(button_list[0])-7 #--right cross--
                    if self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights1)).background_normal in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights1)).background_normal in chess_pieces and self.buttons.get(str(highlights2)).background_normal not in chess_pieces :
                        pass
                    else:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'


                elif int(button_list[0]) in pawn_pos[8:14]: #--------------------------right-edge
                    highlights1=int(button_list[0])-8    #--straight--
                    highlights2 = int(button_list[0])-9 #--left cross--
                    if self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights1)).background_normal in chess_pieces:
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights1)).background_normal in chess_pieces and self.buttons.get(str(highlights2)).background_normal not in chess_pieces :
                        pass
                    else:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'

                else:
                    highlights1=int(button_list[0])-8    #-------------right-left cross
                    highlights2 = int(button_list[0])-7 #--right cross--
                    highlights3 = int(button_list[0])-9 #--left cross--
                    if self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights1)).background_normal !='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal !='':
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights3)).background_normal =='' and self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal !='':
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights2)).background_normal =='' and self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights3)).background_normal in chess_pieces and self.buttons.get(str(highlights2)).background_normal not in chess_pieces and self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights3)),self.buttons.get(str(highlights3)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                        self.buttons.get(str(highlights3)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights3)).background_normal not in chess_pieces and self.buttons.get(str(highlights2)).background_normal in chess_pieces and self.buttons.get(str(highlights1)).background_normal =='':
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        button_highlights.append([self.buttons.get(str(highlights2)),self.buttons.get(str(highlights2)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                        self.buttons.get(str(highlights2)).background_color='#FFFF75'
                    elif self.buttons.get(str(highlights1)).background_normal !='':
                        pass
                    else:
                        button_highlights.append([self.buttons.get(str(highlights1)),self.buttons.get(str(highlights1)).background_color])
                        self.buttons.get(str(highlights1)).background_color='#FFFF75'
                            
                
    def chess_move(self, move):
        try:
            self.sound = SoundLoader.load('move-sound.mp3') #---move-sound.mp3 for pretty
            self.sound2 = SoundLoader.load('notify-sound.mp3')
            self.sound3 = SoundLoader.load('win-sound.mp3')
            button_list = [key for key, value in self.buttons.items() if value == move]
                                     #----this color effect with highlights color -for WHITE #FFFF75 **for black #76F7FF           --black
            if move.background_color ==[1.0, 1.0, 0.4588235294117647, 1.0] or move.background_color ==[0.4627450980392157, 0.9686274509803922, 1.0, 1.0]:
                if move.background_normal =='king-w.png' or move.background_normal =='king-b.png':
                    if move.background_normal =='king-w.png':
                        winner_text = '----->  BLACK WON !  <-----'
                    else:
                        winner_text = '----->  WHITE WON !  <-----'
                    popup_layout = BoxLayout(orientation='vertical')
                    restart_button = Button(text = 'Restart',background_color='#7F90FF', size_hint=(1,0.25))
                    winner = Image(source = 'winner.png')
                    text_label = Label(text=winner_text)
                    restart_button.bind(on_release = self.restart)
                    popup_layout.add_widget(winner)
                    popup_layout.add_widget(restart_button)
                    popup = Popup(title=winner_text, title_color='black',content=popup_layout, size_hint = (0.65,0.65), auto_dismiss=True,
                          background_color = (255,255,255,1),separator_color='black')
                    restart_button.bind(on_touch_down = popup.dismiss)
                    popup.open()
                    self.sound3.play()


                elif old_pos[0].background_normal == 'pawn-b.png' or old_pos[0].background_normal == 'pawn-w.png':
                    if (int(button_list[0]) >= 0 and int(button_list[0]) < 8) or (int(button_list[0]) >= 56 and int(button_list[0]) < 65):
                        popup_layout = GridLayout(rows=2, cols=3)
                        self.butt = {}
                        if old_pos[0].background_normal == 'pawn-w.png':  
                            for j in range(5):
                                edit = chess_pieces[j].replace('-b','-w')
                                buttons = Button(text = '',background_color='#FFFFFF',background_normal=edit, size_hint=(None,None))  
                                self.butt[f'{j}'] = buttons #id
                                buttons.bind(on_release = lambda piece=buttons,move=move : self.replace_piece(piece,move)) 
                                popup_layout.add_widget(buttons)
                        else:
                            for j in range(5):
                                edit = chess_pieces[j]
                                buttons = Button(text = '',background_color='#FFFFFF',background_normal=edit, size_hint=(None,None)) 
                                self.butt[f'{j}'] = buttons #id
                                buttons.bind(on_release = lambda piece=buttons,move=move : self.replace_piece(piece,move)) 
                                popup_layout.add_widget(buttons)
                        
                        popup = Popup(title='Choose one', title_color='black',content=popup_layout, size_hint = (0.4,0.45), auto_dismiss=True,
                        background_color = (255,255,255,1),separator_color='black')
                        buttons.bind(on_touch_down = popup.dismiss)
                        popup.open()
                    else:
                        move.background_normal = old_pos[0].background_normal
                        old_pos[0].background_normal = ''
                        for button,color in button_highlights:
                            button.background_color =color

                        button_highlights.clear()
                        old_pos.clear()

                else:
                    move.background_normal = old_pos[0].background_normal
                    old_pos[0].background_normal = ''
                    for button,color in button_highlights:
                        button.background_color =color

                    button_highlights.clear()
                    old_pos.clear()
                self.sound.play()

            elif (move.background_color !=[1.0, 1.0, 0.4588235294117647, 1.0] or move.background_color != [0.4627450980392157, 0.9686274509803922, 1.0, 1.0])and len(old_pos)>0:
                    for button,color in button_highlights:
                        button.background_color =color  #-----for turn back background color on press empty piece.
                    button_highlights.clear()
                    old_pos.clear()
                    if move.background_normal !='': #----directly turn back and show highlights when touch any piece.
                        return self.chess_move(move)

            elif move.background_normal == 'pawn-b.png' or move.background_normal =='pawn-w.png':
                if move in old_pos:
                    pass  #-----------------if same click twice or over on same piece!
                else:
                    old_pos.append(move)     
                    return self.pawn_event(move)

            elif move.background_normal == 'castle-b.png' or move.background_normal =='castle-w.png':
                if move in old_pos:
                    pass  
                else:
                    old_pos.append(move)  
                    return self.castle_event(move)

            elif move.background_normal == 'knight-b.png' or move.background_normal =='knight-w.png':
                if move in old_pos:
                    pass  
                else:
                    old_pos.append(move)      
                    return self.knight_event(move)

            elif move.background_normal == 'elephant-b.png' or move.background_normal =='elephant-w.png':
                if move in old_pos:
                    pass  
                else:
                    old_pos.append(move)      
                    return self.elephant_event(move)

            elif move.background_normal == 'queen-b.png' or move.background_normal =='queen-w.png':
                if move in old_pos:
                    pass  
                else:
                    old_pos.append(move)      
                    return self.queen_event(move)

            elif move.background_normal == 'king-b.png' or move.background_normal =='king-w.png':
                if move in old_pos:
                    pass  
                else:
                    old_pos.append(move)      
                    return self.king_event(move)
  
        except(Exception):
            pass
     
    def replace_piece(self,piece, move):
        self.sound2.play()
        move.background_normal = piece.background_normal
        old_pos[0].background_normal = ''
        for button,color in button_highlights:
            button.background_color =color

        button_highlights.clear()
        old_pos.clear()

    def restart(self, arg):
        self.sound2.play()
        App.get_running_app().stop() #restart game
        ChessApp().run()

    def layout(self): 
        table = FloatLayout() #ljust(30)
        table_background = Image(source='table_background.png', allow_stretch = True, keep_ratio = False)
        chess_table = GridLayout(cols=8, rows=8, spacing='1dp', size_hint=(0.92,0.92), pos_hint = {'center_x':0.5, 'center_y':0.5})
        labels1 = Label(text = '[b]A{:20}B{:20}C{:20}D{:20}E{:20}F{:20}G{:20}H[/b]'.format('','','','','','',''),
            pos_hint = {'center_y':0.98}, markup = True) #---labels
        labels2 = Label(text = '[b]1\n\n\n\n2\n\n\n\n3\n\n\n\n4\n\n\n\n5\n\n\n\n6\n\n\n\n7\n\n\n\n8[/b]', 
            pos_hint = {'center_x':0.02}, markup = True)
        self.buttons = {} #for button ID
        for i in range(64): #Here is Chess Table
            if i % 2 == 0 and i<8:                       
                if i == 0:
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='castle-b.png')
                elif i ==2:
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='elephant-b.png')
                elif i ==4:
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='king-b.png')
                elif i ==6:
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='knight-b.png')
                else:  
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='')
            elif i % 2 != 0 and i<8:
                if i ==1:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='knight-b.png')
                elif i ==3:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='queen-b.png')
                elif i ==5:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='elephant-b.png')
                elif i ==7:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='castle-b.png')
                else:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='')
       
            elif i % 2 == 0 and i<16:
                table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='pawn-b.png')
            elif i % 2 !=0 and i<16:
                table_buttons = Button(text='', background_color='#9E561B', background_normal ='pawn-b.png')
            elif i % 2 == 0 and i<24:           
                table_buttons = Button(text='', background_color='#9E561B', background_normal ='')
            elif i % 2 != 0 and i<24:
                table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='')
            elif i % 2 == 0 and i<32:
                table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='')
            elif i % 2 !=0 and i<32:
                table_buttons = Button(text='', background_color='#9E561B', background_normal ='')
            elif i % 2 == 0 and i<40:           
                table_buttons = Button(text='', background_color='#9E561B', background_normal ='')
            elif i % 2 != 0 and i<40:
                table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='')
            elif i % 2 == 0 and i<48:
                table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='')
            elif i % 2 !=0 and i<48:
                table_buttons = Button(text='', background_color='#9E561B', background_normal ='')
            elif i % 2 == 0 and i<56:           
                table_buttons = Button(text='', background_color='#9E561B', background_normal ='pawn-w.png')
            elif i % 2 != 0 and i<56:
                table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='pawn-w.png')
            elif i % 2 == 0 and i<64:
                if i ==62:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='knight-w.png')
                elif i ==60:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='king-w.png')
                elif i ==58:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='elephant-w.png')
                elif i ==56:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='castle-w.png')
                else:
                    table_buttons = Button(text='', background_color='#E6CCAB', background_normal ='')
            elif i % 2 !=0 and i<64:
                if i == 63:
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='castle-w.png')
                elif i ==61:
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='elephant-w.png')
                elif i ==59:
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='queen-w.png')
                elif i ==57:
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='knight-w.png')
                else:  
                    table_buttons = Button(text='', background_color='#9E561B', background_normal ='')
                    
            self.buttons[f'{i}'] = table_buttons #id
                
            table_buttons.bind(on_release= lambda move = table_buttons: self.chess_move(move))   
            chess_table.add_widget(table_buttons)
        table.add_widget(table_background)
        table.add_widget(labels1)
        table.add_widget(labels2)
        table.add_widget(chess_table)
        return table #chess_table
        
    def build(self):
        self.icon='iconapp.png'
        return self.layout()

kv=ChessApp().run() 
