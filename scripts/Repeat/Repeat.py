# Defines a "repeat" function that takes 2 arguments
def repeat(s,exclaim):
    """
    Docstring for repeat
    
    :param s: string 's' is repeated 3 times
    :param exclaim: boolean 'exclaim' adds exclamation marks if true
    """

    result = s*3
    if exclaim:
        result = result + '!!!'
    return result

def main():
    print(repeat('Yay', False)) # YayYayYay
    print(repeat('Woo Hoo ', True)) # Woo Hoo Woo Hoo Woo Hoo !!!

if __name__ == '__main__':
    main()