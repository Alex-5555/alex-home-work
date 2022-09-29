def _h(*a):
    const = 0
    for i in a:
        const = const + i
    return  const



def h(f):
    return f(_h)

#print('pizdez-')   
print(h(2, 2, 2, 555))
#print('-holodez')
# 'pizdez-561-holodez'