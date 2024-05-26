def lower_triangular(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print('*', end=' ')
        print()

def upper_triangular(n):
    for i in range(1, n+1):
        for j in range(1, n+2-i):
            print('*', end=' ')
        print()

def pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print('*', end='')
        print()

def main():
    n = int(input('Enter number of rows: '))
    
    print('\nLower Triangular Pattern:')
    lower_triangular(n)
    
    print('\nUpper Triangular Pattern:')
    upper_triangular(n)
    
    print('\nPyramid Pattern:')
    pyramid(n)

# Run the main function
if __name__ == '__main__':
    main()
