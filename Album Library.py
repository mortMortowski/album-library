import random
import sys

def main():
    albums = ["AC/DC - Power Up (2020)", "AC/DC - Iron Man 2 (2010)", "AC/DC - Back In Black (1980)", "AC/DC - Highway To Hell (1979)", "AC/DC - High Voltage (1976)", "Alter Bridge - Blackbird (2007)", "Black Sabbath - The End (2016)", "Burzum - Anthology (2002)", "Celtic Frost - Into The Pandemonium (1987)", "Death - Symbolic (1995)", "Electric Wizard - Electric Wizard (1994)", "Foo Fighters - Foo Fighters (1995)", "Green Day - Dookie (1994)", "Guns n Roses - Use Your Illusion I (1991)", "Kreator - Pleasure To Kill (1986)", "Kreator - Endless Pain (1985)", "Kyuss - ...And The Circus Leaves Town (1995)", "Kyuss - Welcome To Sky Valley (1994)", "Kyuss - Blues For The Red Sun (1992)", "Kyuss - Wretch (1991)", "Led Zeppelin - Remasters (1992)", "Lynyrd Skynyrd - The Last Rebel (1993)", "Megadeth - The Sick The Dying And The Dead (2022)", "Megadeth - Cryptic Writings (1997)", "Megadeth - Youthanasia (1994)", "Megadeth - Countdown To Extinction (1992)", "Megadeth - Rust In Peace (1990)", "Megadeth - So Far So Good So What! (1988)", "Megadeth - Peace Sells But Who's Buying? (1986)", "Metallica - Metallica (1991)", "Metallica - ...And Justice For All (1988)", "Metallica - Master Of Puppets (1986)", "Metallica - Ride The Lightning (1984)", "Metallica - Kill 'Em All (1983)", "Motorhead - Hellraiser (2003)", "Motorhead - 1916 (1991)", "Nirvana - Sliver The Best Of The Box (2005)", "Nirvana - Live At Reading (2009)", "Nirvana - Unplugged in New York (1994)", "Nirvana - Nevermind (1991)", "Pearl Jam - Ten (1991)", "Pink Floyd - The Division Bell (1994)", "Pink Floyd - The Dark Side of the Moon (1973)", "Queens Of The Stone Age - Lullabies to Paralyze (2005)", "Red Hot Chili Peppers - Californication (1999)", "Slayer - Christ Illusion (2006)", "Soundgarden - Superunknown (1994)"]
    print("Album Library v.0.1")
    print("1. View all albums")
    print("2. Select random album")
    print("3. Exit")
    option = input("Select option: ")
    if (option == "1"):
        for item in albums:
            print(item)
    elif (option == "2"):
        print(random.choice(albums))
    elif (option == "3"):
        sys.exit()
    else:
        print("No such option. Exiting program...")
    
    input("Press any key to exit")

if __name__ == "__main__":
    main()