class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def convert(num):
            return str(bin(num)).split('0b')[1]
        def pad(num,maxLen):
            return (maxLen-len(num))*'0' + num
        
        bin_a = convert(a)
        bin_b = convert(b)
        bin_c = convert(c)
        
        maxLen=max(len(bin_a),len(bin_b),len(bin_c))
        bin_a = pad(bin_a,maxLen)[::-1]
        bin_b = pad(bin_b,maxLen)[::-1]
        bin_c = pad(bin_c,maxLen)[::-1]
        print(bin_a,bin_b,bin_c)
        flips = 0
        for i in range(len(bin_a)):
            if bin_c[i] == '0':
                if not bin_a[i] == '0': flips += 1
                if not bin_b[i] == '0': flips += 1
            else:
                if not (bin_a[i] == '1' or bin_b[i] == '1'): flips += 1
        return flips



        

        