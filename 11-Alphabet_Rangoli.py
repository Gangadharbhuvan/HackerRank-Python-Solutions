def print_rangoli(size):
    # your code goes here
    l = "".join(list(map(chr, range(97, 123))) )
    k=size-1
    for i in range(2*size-1):
        if(i<size):
            s="-".join(l[k+i:k:-1]+l[k:k+i+1])
            print(s.center(4*size-3,'-'))
            k=k-1
        if(i==size):
            j=(2*size-2)%i
            k=k+2
            s="-".join(l[k+j:k:-1]+l[k:k+j+1])
            print(s.center(4*size-3,'-'))
        if(i>size):
            j=(2*size-2)%i
            k=k+1
            s="-".join(l[k+j:k:-1]+l[k:k+j+1])
            print(s.center(4*size-3,'-'))




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
