import profile
import technical

def input():
    tickerinput = 'NFLX'
    return tickerinput

def main():
    profile.Profile(input())
    technical.Scrappy(input())

if __name__ == '__main__':
    main()
