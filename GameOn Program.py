#Establish variables
console = ''
genre = ''
select = ''

#GameOn Program
def gameOn(con,gen):
    global select
    #Check for valid inputs
    if con == 'xbox':
        if gen == 'adventure':
            while select != 'y':
            
                print('Rise of the Tomb Raider (2015)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[0])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Red Dead Redemption 2 (2018)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[1])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Control (2019)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[2])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Ori and the Will of the Wisps (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[3])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Star Wars Jedi: Fallen Order (2019)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[4])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''                        

        elif gen == 'puzzle':
            while select != 'y':
            
                print('Inside + Limbo Combo Pack (2016)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[5])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('The Turing Test (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[6])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('The Witness (2016)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[7])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Human Fall Flat (2016)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[8])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Superliminal (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[9])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'rpg':
            while select != 'y':
            
                print('Monster Hunter: World (2018)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[10])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Kingdom Hearts III (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[11])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Fallout 4 (2015)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[12])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Final Fantasy XV (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[13])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('The Witcher 3: Wild Hunt (2016)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[14])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'sports':
            while select != 'y':
            
                print('Madden NFL 20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[15])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('EA Sports FIFA 20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[16])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Rocket League (2015)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[17])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('NBA 2k20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[18])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('NHL 20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[19])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'strategy':
            while select != 'y':
            
                print('Civilization VI (2016)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[20])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Halo Wars 2 (2017)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[21])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Stellaris (2016)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[22])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('XCOM 2 (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[23])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Wargroove (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[24])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''
        

    elif con == 'ps4':
        if gen == 'adventure':
                print('Marvel\'s Spider Man (2018)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[25])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('God of War (2018)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[26])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('The Last of Us Part II (2020)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[27])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Red Dead Redemption 2 (2018)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[28])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Horizon Zero Dawn (2017)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[29])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''  

        elif gen == 'puzzle':
                print('The Talos Principle (2018)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[30])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Tetris Effect (2018)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[31])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('The Last Guardian (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[32])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('The Witness (2016)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[33])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Unravel Two (2018)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[34])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''  

        elif gen == 'rpg':
                print('Persona 5 Royal (2020)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[35])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Final Fantasy XV Royal Edition (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[36])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Bloodborne (2015)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[37])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Nier: Automata (2017)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[38])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Kingdom hearts III (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[39])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''  

        elif gen == 'sports':
            while select != 'y':
            
                print('Madden NFL 20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[40])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('EA Sports FIFA 20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[41])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Rocket League (2015)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[42])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('NBA 2k20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[43])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('NHL 20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[44])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'strategy':
            while select != 'y':
            
                print('Valkyria Chronicles 4 (2018)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[45])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Civilization VI (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[46])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Stellaris (2016)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[47])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('XCOM 2 (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[48])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Tropico 6 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[49])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''
        

    elif con == 'switch':
        if gen == 'adventure':
            while select != 'y':
            
                print('Minecraft Dungeons (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[50])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Mario + Rabbids Kingdom Battle (2017)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[51])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Luigi\'s Mansion 3 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[52])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Animal Crossing: New Horizons (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[53])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Hollow Knight (2017)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[54])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'puzzle':
            while select != 'y':
            
                print('Captain Toad: Treasure Tracker (2014)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[55])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Snipperclips (2017)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[56])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Sushi Striker: The Way of Sushido (2018)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[57])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Lumines Remastered (2018)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[58])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Picross S4 (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[59])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'rpg':
            while select != 'y':
            
                print('The Legend of Zelda: Breath of the Wild (2017)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[60])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Xenoblade Chronicles 2 (2017)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[61])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Pokemon Sword (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[62])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Fire Emblem: Three Houses (2019)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[63])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Dragon Quest XI S: Echoes of an Elusive Age(2017)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[64])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'sports':
            while select != 'y':
            
                print('Mario Tennis Aces (2018)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[65])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Mario and Sonic at the Olympics (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[66])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Rocket League (2015)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[67])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('NBA 2k20 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[68])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Super Mega Baseball 3 (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[69])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'strategy':
            while select != 'y':
            
                print('Valkyria Chronicles 4 (2018)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[70])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Civilization VI (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[71])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Disgaea 5 (2015)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[72])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('The Banner Saga (2014)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[73])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Wargroove (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[74])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''
        

    elif con == 'pc':
        if gen == 'adventure':
            while select != 'y':
            
                print('Pathologic 2 (2018)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[75])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('The Wolf Among Us (2014)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[76])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Sea of Thieves (2018)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[77])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Grand Theft Auto V (2015)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[78])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('No Man\'s Sky (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[79])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'puzzle':
            while select != 'y':
            
                print('Donut County (2018)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[80])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Human Fall Flat (2016)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[81])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Celeste (2018)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[82])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Unravel Two (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[83])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('We Were Here Together (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[84])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'rpg':
            while select != 'y':
            
                print('Stardew Valley (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[85])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Monster Hunter World (2018)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[86])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Fallout 4 (2015)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[87])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Borderlands 3 (2020)\nRated - M')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[88])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Undertale (2015)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[89])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'sports':
                print('Button Soccer League (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[90])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('F1 2020 (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[91])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Rocket League (2015)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[92])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Golf with your Friends (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[93])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Super Mega Baseball 3 (2020)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[94])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''

        elif gen == 'strategy':
                print('Civilization VI (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[95])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Age of Empires II (2013)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[96])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('XCOM 2 (2016)\nRated - T')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[97])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Tropico 6 (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[98])
                        return select
                    elif select == 'n':
                        print('\n')
                        pass
                    else:
                        print('Invalid input')
                select = ''

                print('Northgard (2019)\nRated - E')
                while select != 'y' and select != 'n':
                    select = input('Would you like this game? (y/n) ').lower()
                    if select == 'y':
                        print('\n' + 'Purchase here: ' + links[99])
                        return select
                    elif select == 'n':
                        print('No more games to suggest, please run again with a different console or genre in mind.')
                        select = 'y'
                        return select
                    else:
                        print('Invalid input')
                select = ''
        
#Lists of game links for every console / genre
links = ['https://www.gamestop.com/video-games/xbox-one/games/products/rise-of-the-tomb-raider/10122184.html', 
'https://www.microsoft.com/en-us/p/red-dead-redemption-2/bpswgqbw7r3g?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/control/bz6w9lrpc26w?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/ori-and-the-will-of-the-wisps/9n8cd0xzklp4?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/star-wars-jedi-fallen-order/c2csdtscbz0c?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/inside-limbo-bundle/c1wp25bwlvtf?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/the-turing-test/bs2mmfvlkxrk?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/the-witness/bx1wpt5rjsb2?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/human-fall-flat/bsmzh25v6v46?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/superliminal/9nvr4zqknbsb#activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/monster-hunter-world/bng91pt95lqn?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/kingdom-hearts/c08mw8xhqn9g?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/fallout-4/c3kldkzbhncz?activetab=pivot:overviewtab',
'https://www.gamestop.com/video-games/xbox-one/games/products/final-fantasy-xv/10125320.html',
'https://www.microsoft.com/en-us/p/the-witcher-3-wild-hunt/br765873cqjd?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/madden-nfl-20/bz289tv4qvck?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/ea-sports-fifa-20/bv433v4b23lm?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/rocket-league/c125w9bg2k0v?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/nba-2k20/9p9kn2g4m2w0?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/nhl-20/c2hhtcszrk9g?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/sid-meiers-civilization-vi/9n4rsg99kv1x?activetab=pivot:overviewtab',
'https://www.gamestop.com/video-games/xbox-one/games/products/halo-wars-2/10132023.html',
'https://www.microsoft.com/en-us/p/stellaris-console-edition/bwl72gr7z7gk?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/xcom-2/bqwgbmckrmsq?activetab=pivot:overviewtab',
'https://www.microsoft.com/en-us/p/wargroove/9nrpttj94pck?activetab=pivot:overviewtab',
'https://direct.playstation.com/en-us/games/game/marvels-spider-man-game-of-the-year-edition-ps4.3004313',
'https://direct.playstation.com/en-us/games/game/god-of-war-ps4.3004857',
'https://direct.playstation.com/en-us/games/game/the-last-of-us-part-ii-ps4.3003180',
'https://store.playstation.com/en-us/product/UP1004-CUSA03041_00-REDEMPTION000002',
'https://direct.playstation.com/en-us/games/game/horizon-zero-dawn-complete-edition-ps4.3004493',
'https://store.playstation.com/en-us/product/UP3643-CUSA00910_00-00000000000TALOS',
'https://store.playstation.com/en-us/product/UP0751-CUSA13594_00-TETRISEFFECT0000',
'https://store.playstation.com/en-us/product/UP9000-CUSA03627_00-LASTGUARDIANUS00',
'https://store.playstation.com/en-us/product/UP2124-CUSA00498_00-THEWITNESSPS4PS4',
'https://store.playstation.com/en-us/product/UP0006-CUSA10483_00-COLDWOODPIKE0000',
'https://store.playstation.com/en-us/product/UP0177-CUSA17416_00-PERSONA5R0000000',
'https://store.playstation.com/en-us/product/UP0082-CUSA01633_00-FFXVROYALEDITION',
'https://store.playstation.com/en-us/product/UP9000-CUSA00900_00-BLOODBORNE000000',
'https://store.playstation.com/en-us/product/UP0082-CUSA04551_00-GOTYORHADIGITAL0',
'https://store.playstation.com/en-us/product/UP0082-CUSA12031_00-KINGDOMHEARTSX30',
'https://store.playstation.com/en-us/product/UP0006-CUSA13265_00-MADDENNFL20GAME1',
'https://store.playstation.com/en-us/product/UP0006-CUSA15557_00-FIFAFOOTBALL2020',
'https://store.playstation.com/en-us/product/UP2002-CUSA01163_00-ROCKETLEAGUENA01',
'https://store.playstation.com/en-us/product/UP1001-CUSA16310_00-NBA2K20000000000',
'https://store.playstation.com/en-us/product/UP0006-CUSA15439_00-NHLICEHOCKEY2020',
'https://store.playstation.com/en-us/product/UP0177-CUSA10633_00-BFVALKYRIE000100',
'https://store.playstation.com/en-us/product/UP1001-CUSA15322_00-CIV6BASE00000000',
'https://store.playstation.com/en-us/product/UP4139-CUSA07740_00-STELLARISPS4US00',
'https://store.playstation.com/en-us/product/UP1001-CUSA04552_00-XCOM200000000000',
'https://store.playstation.com/en-us/product/UP2060-CUSA08217_00-TROPICO600000001',
'https://www.nintendo.com/games/detail/minecraft-dungeons-switch/',
'https://www.nintendo.com/games/detail/mario-rabbids-kingdom-battle-switch/',
'https://www.nintendo.com/games/detail/luigis-mansion-3-switch/',
'https://www.nintendo.com/games/detail/animal-crossing-new-horizons-switch/',
'https://www.nintendo.com/games/detail/hollow-knight-switch/',
'https://www.nintendo.com/games/detail/captain-toad-treasure-tracker-switch/',
'https://www.nintendo.com/games/detail/snipperclips-plus-switch/',
'https://www.nintendo.com/games/detail/sushi-striker-the-way-of-sushido-switch/',
'https://www.nintendo.com/games/detail/lumines-remastered-switch/',
'https://www.nintendo.com/games/detail/picross-s4-switch/',
'https://www.nintendo.com/games/detail/the-legend-of-zelda-breath-of-the-wild-switch/',
'https://www.nintendo.com/games/detail/xenoblade-chronicles-2-switch/',
'https://www.nintendo.com/games/detail/pokemon-sword-switch/',
'https://www.nintendo.com/games/detail/fire-emblem-three-houses-switch/',
'https://www.nintendo.com/games/detail/dragon-quest-xi-s-echoes-of-an-elusive-age-definitive-edition-switch/',
'https://www.nintendo.com/games/detail/mario-tennis-aces-switch/',
'https://www.nintendo.com/games/detail/mario-and-sonic-at-the-olympic-games-tokyo-2020-switch/',
'https://www.nintendo.com/games/detail/rocket-league-switch/',
'https://www.nintendo.com/games/detail/nba-2k20-switch/',
'https://www.nintendo.com/games/detail/super-mega-baseball-3-switch/',
'https://www.nintendo.com/games/detail/valkyria-chronicles-4-switch/',
'https://www.nintendo.com/games/detail/sid-meiers-civilization-vi-switch/',
'https://www.nintendo.com/games/detail/disgaea-5-complete-switch/',
'https://www.nintendo.com/games/detail/banner-saga-trilogy-switch/',
'https://www.nintendo.com/games/detail/wargroove-switch/',
'https://store.steampowered.com/app/505230/Pathologic_2/',
'https://store.steampowered.com/app/250320/The_Wolf_Among_Us/',
'https://store.steampowered.com/app/1172620/Sea_of_Thieves/',
'https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/',
'https://store.steampowered.com/app/275850/No_Mans_Sky/',
'https://store.steampowered.com/app/702670/Donut_County/',
'https://store.steampowered.com/app/477160/Human_Fall_Flat/',
'https://store.steampowered.com/app/504230/Celeste/',
'https://store.steampowered.com/app/1225570/Unravel_Two/',
'https://store.steampowered.com/app/865360/We_Were_Here_Together/',
'https://store.steampowered.com/app/413150/Stardew_Valley/',
'https://store.steampowered.com/app/582010/Monster_Hunter_World/',
'https://store.steampowered.com/app/377160/Fallout_4/',
'https://store.steampowered.com/app/397540/Borderlands_3/',
'https://store.steampowered.com/app/391540/Undertale/',
'https://store.steampowered.com/app/1357090/Button_Soccer_League/',
'https://store.steampowered.com/app/1080110/F1_2020/',
'https://store.steampowered.com/app/252950/Rocket_League/',
'https://store.steampowered.com/app/431240/Golf_With_Your_Friends/',
'https://store.steampowered.com/app/988910/Super_Mega_Baseball_3/',
'https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/',
'https://store.steampowered.com/app/239550/Age_of_Empires_II_2013_The_Forgotten/',
'https://store.steampowered.com/app/268500/XCOM_2/',
'https://store.steampowered.com/app/492720/Tropico_6/',
'https://store.steampowered.com/app/466560/Northgard/']

print('Welcome to GameOn - Your personal video game suggester\n')

#Select a valid console
while True:
    console = input('Please enter your preferred video game platform.\nType "Xbox" for the Xbox One, \n"PS4" for the Playstation 4, \n"Switch" for the Nintendo Switch, \nor "PC" for your personal computer\nEnter: ').lower()
    if console == 'xbox' or console == 'ps4' or console == 'switch' or console == 'pc':
        print('\n')
        break
    else:
        print('Invalid input\n')

#Select a valid genre
while True:
    genre = input('Please enter one of the following genres to search for:\nAdventure, Puzzle, RPG, Sports, Strategy\nEnter: ').lower()
    if genre == 'adventure' or genre == 'puzzle' or genre == 'rpg' or genre == 'sports' or genre == 'strategy':
        print('\n')
        break
    else:
        print('Invalid input\n')

gameOn(console, genre)