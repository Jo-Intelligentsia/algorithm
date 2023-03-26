def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

# bin(5) -> '0b101'
# bin(5)[2:] -> '101'
# bin(int(bin1, 2) + int(bin2, 2))[2:]