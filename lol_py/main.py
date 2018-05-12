from __future__ import print_function, division
import sys
from math import sin, pi
import argparse

def rainbow(freq, i):
    """Creates RGB values, inspired from https://github.com/busyloop/lolcat
    
    Args:
        freq (int): Frequency, more the value; more the colours
        i (int): Current character position, used to set colours at character level
    
    Returns:
        tuple: Contains integers R, G, B
    """
    red = sin(freq * i + 0) * 127 + 128
    green = sin(freq * i + 2*pi/3) * 127 + 128
    blue = sin(freq * i + 4*pi/3) * 127 + 128
    # return "%0x"%(int(red)), "%0x"%(int(green)), "%0x"%(int(blue))
    return int(red), int(green), int(blue)

def print_rainbow_text(text, freq=220, end="\n"):
    """Prints rainbow text
    
    Args:
        text (str/list(str)): String or list of str. Provide list to make the whole
                              paragraph look consistent
        freq (int, optional): Frequency determines rate of colour change. It's a sine wave so 
                              changing values on extremes might not help. Sweet spot is 220,
                              stick to it.
        end (str, optional): Similar to end param in print function
    """
    for i,c in enumerate(text):
        if type(text) != list:
            r,g,b = rainbow(freq, i)
            color2 = "\033[38;2;%d;%d;%dm"%(r,g,b)
            print(color2+c+"\033[0m", end="")
        else:
            for j, cagain in enumerate(c):
                r,g,b = rainbow(freq, i*10 + j)
                color2 = "\033[38;2;%d;%d;%dm"%(r,g,b)
                print(color2+cagain+"\033[0m", end="")
    print(end=end)
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inp-file", help="Input file to read and display. If not provided, reads from stdin", default=None)
    parser.add_argument("--freq", help="Frequency used to affect the rate of colour change.", type=int, default=220)    
    args = parser.parse_args()
    freq = args.freq # 220 best
    if args.inp_file == None:
        text = sys.stdin
    else:        
        text = open(args.inp_file, "r") 
    # colourtxt = "\x1b[{}m{}\x1b[0m".format(str(colour), txt)
    print_rainbow_text(text.readlines(), freq=args.freq)
    try:
        text.close()
    except Exception:
        pass
    print()

if __name__ == "__main__":
    main()