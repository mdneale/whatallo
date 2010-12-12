"""'Allo 'Allo"""

from randallo.engine import show

def get_show():
    """Return a Show object for 'Allo 'Allo"""
    
    return show.Show(u'\'Allo \'Allo', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!', [
        # Pilot
        show.Episode(u'The British Are Coming, Pilot', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)#Pilot:_The_British_Are_Coming'),

        # Series 1
        show.Series(u'Series 1', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)', [
            show.Episode(u'Series 1, Episode 1', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)#Series_1.2C_Episode_1'),
            show.Episode(u'Pigeon Post', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)#Pigeon_Post'),
            show.Episode(u'Saville Row to the Rescue', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)#Saville_Row_to_the_Rescue'),
            show.Episode(u'The Execution', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)#The_Execution'),
            show.Episode(u'The Funeral', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)#The_Funeral'),
            show.Episode(u'Red Nick\'s Colonel', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)#Red_Nick.27s_Colonel'),
            show.Episode(u'The Dance of Hitler Youth', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_1)#The_Dance_of_Hitler_Youth'),
        ]),

        # Series 2
        show.Series(u'Series 2', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_2)', [
            show.Episode(u'Six Big Boobies', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_2)#Six_Big_Boobies'),
            show.Episode(u'The Wooing of Widow Artois', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_2)#The_Wooing_of_Widow_Artois'),
            show.Episode(u'The Policeman Cometh', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_2)#The_Policeman_Cometh'),
            show.Episode(u'Swiftly and with Style', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_2)#Swiftly_and_with_Style'),
            show.Episode(u'The Duel', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_2)#The_Duel'),
            show.Episode(u'Herr Flick\'s Revenge', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_2)#Herr_Flick.27s_Revenge'),
        ]),

        # 1985 Christmas Special
        show.Episode(u'The Gateau from the Chateau, 1985 Christmas Special', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_2)#Christmas_Special:_The_Gateau_from_the_Chateau'),

        # Series 3
        show.Series(u'Series 3', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_3)', [
            show.Episode(u'The Nicked Knockwurst', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_3)#The_Nicked_Knockwurst'),
            show.Episode(u'Gruber Does Some Mincing', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_3)#Gruber_Does_Some_Mincing'),
            show.Episode(u'The Sausage in the Wardrobe', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_3)#The_Sausage_in_the_Wardrobe'),
            show.Episode(u'Flight of Fancy', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_3)#Flight_of_Fancy'),
            show.Episode(u'Pretty Maids All in a Row', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_3)#Pretty_Maids_All_in_a_Row'),
            show.Episode(u'The Great Un-Escape', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_3)#The_Great_Un-Escape'),
        ]),

        # Series 4
        show.Series(u'Series 4', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_4)', [
            show.Episode(u'Prisoners of War', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_4)#Prisoners_of_War'),
            show.Episode(u'Camp Dance', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_4)#Camp_Dance'),
            show.Episode(u'Good Staff Are Hard to Find', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_4)#Good_Staff_Are_Hard_to_Find'),
            show.Episode(u'The Flying Nun', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_4)#The_Flying_Nun'),
            show.Episode(u'The Sausages in the Trousers', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_4)#The_Sausages_in_the_Trousers'),
            show.Episode(u'The Jet-Propelled Mother-In-Law', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_4)#The_Jet-Propelled_Mother-In-Law'),
        ]),

        # Series 5
        show.Series(u'Series 5', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)', [
            show.Episode(u'Desperate Doings in the Dungeon', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Desperate_Doings_in_the_Dungeon'),
            show.Episode(u'The Camera in the Potato', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#The_Camera_in_the_Potato'),
            show.Episode(u'Dinner with the General', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Dinner_with_the_General'),
            show.Episode(u'The Dreaded Circular Saw', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#The_Dreaded_Circular_Saw'),
            show.Episode(u'Otherwise Engaged', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Otherwise_Engaged'),
            show.Episode(u'A Marriage of Inconvenience', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#A_Marriage_of_Inconvenience'),
            show.Episode(u'No Hiding Place', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#No_Hiding_Place'),
            show.Episode(u'The Arrival of the Homing Duck', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#The_Arrival_of_the_Homing_Duck'),
            show.Episode(u'Watch the Birdie', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Watch_the_Birdie'),
            show.Episode(u'Ren\u00E9 - Under an Assumed Nose', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Ren.C3.A9_-_Under_an_Assumed_Nose'),
            show.Episode(u'The Confusion of the Generals', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#The_Confusion_of_the_Generals'),
            show.Episode(u'Who\'s for the Vatican?', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Who.27s_for_the_Vatican.3F'),
            show.Episode(u'Ribbing the Bonk', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Ribbing_the_Bonk'),
            show.Episode(u'The Reluctant Millionaires', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#The_Reluctant_Millionaires'),
            show.Episode(u'A Duck for Launch', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#A_Duck_for_Launch'),
            show.Episode(u'The Exploding Bedpan', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#The_Exploding_Bedpan'),
            show.Episode(u'Going Like a Bomb', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Going_Like_a_Bomb'),
            show.Episode(u'Money to Burn', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Money_to_Burn'),
            show.Episode(u'Puddings Can Go Off', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Puddings_Can_Go_Off'),
            show.Episode(u'Land Mines for London', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Land_Mines_for_London'),
            show.Episode(u'Flight to Geneva', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Flight_to_Geneva'),
            show.Episode(u'Train of Events', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Train_of_Events'),
            show.Episode(u'An Enigma Variation', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#An_Enigma_Variation'),
            show.Episode(u'Wedding Bloss', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Wedding_Bloss'),
            show.Episode(u'Down the Drain', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#Down_the_Drain'),
            show.Episode(u'All in Disgeese', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_5)#All_in_Disgeese'),
        ]),

        # Series 6
        show.Series(u'Series 6', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)', [
            show.Episode(u'Desperate Doings in the Graveyard', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)#Desperate_Doings_in_the_Graveyard'),
            show.Episode(u'The Gestapo for the High Jump', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)#The_Gestapo_for_the_High_Jump'),
            show.Episode(u'The Nouvion Oars', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)#The_Nouvion_Oars'),
            show.Episode(u'The Nicked Airmen', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)#The_Nicked_Airmen'),
            show.Episode(u'The Airmen De-Nicked', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)#The_Airmen_De-Nicked'),
            show.Episode(u'The Crooked Fences', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)#The_Crooked_Fences'),
            show.Episode(u'Crabtree\'s Podgeon Pist', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)#Crabtree.27s_Podgeon_Pist'),
            show.Episode(u'Rising to the Occasion', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_6)#Rising_to_the_Occasion'),
        ]),

        # Series 7
        show.Series(u'Series 7', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)', [
            show.Episode(u'A Quiet Honeymoon', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#A_Quiet_Honeymoon'),
            show.Episode(u'An Almighty Bang', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#An_Almighty_Bang'),
            show.Episode(u'Fleeing Monks', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#Fleeing_Monks'),
            show.Episode(u'Up the Crick Without a Piddle', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#Up_the_Crick_Without_a_Piddle'),
            show.Episode(u'The Gestapo Ruins a Picnic', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#The_Gestapo_Ruins_a_Picnic'),
            show.Episode(u'The Spirit of Nouvion', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#The_Spirit_of_Nouvion'),
            show.Episode(u'Leg it to Spain!', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#Leg_It_to_Spain.21'),
            show.Episode(u'Prior Engagements', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#Prior_Engagements'),
            show.Episode(u'Soup and Sausage', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#Soup_and_Sausage'),
            show.Episode(u'Ren\u00E9 of the Gypsies', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_7)#Ren.C3.A9_of_the_Gypsies'),
        ]),

        # 1991 Christmas Special
        show.Episode(u'A Bun in the Oven, 1991 Christmas Special', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)#Christmas_Special:_A_Bun_in_the_Oven'),

        # Series8
        show.Series(u'Series 8', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)', [
            show.Episode(u'Arousing Suspicions', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)#Arousing_Suspicions'),
            show.Episode(u'A Woman Never Lies', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)#A_Woman_Never_Lies'),
            show.Episode(u'Hitler\'s Last Heil', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)#Hitler.27s_Last_Heil'),
            show.Episode(u'Awful Wedded Wife', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)#Awful_Wedded_Wife'),
            show.Episode(u'Firing Squashed', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)#Firing_Squashed'),
            show.Episode(u'A Fishful of Francs', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)#A_Fishful_of_Francs'),
            show.Episode(u'A Swan Song', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_8)#Swan_Song'),
        ]),

        # Series 9
        show.Series(u'Series 9', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_9)', [
            show.Episode(u'Gone with the Windmill', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_9)#Gone_with_the_Windmill'),
            show.Episode(u'A Tour de France', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_9)#A_Tour_de_France'),
            show.Episode(u'Dead Man Marching', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_9)#Dead_Man_Marching'),
            show.Episode(u'Tarts and Flickers', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_9)#Tarts_and_Flickers'),
            show.Episode(u'A Fishy Send-Off', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_9)#A_Fishy_Send-Off'),
            show.Episode(u'A Winkle in Time', u'http://en.wikipedia.org/wiki/\'Allo_\'Allo!_(series_9)#A_Winkle_in_Time'),
        ]),
    ]);
