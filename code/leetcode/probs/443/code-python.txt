class Solution:
    def compress(self, A: List[str]) -> int:
        
        write_index = 0
        read_index = 0
        cur_index = 0
        count = 0
        
        while read_index <= len(A):
            if read_index < len(A) and A[read_index] == A[cur_index]:
                count += 1
            else:
                A[write_index] = A[cur_index]
                write_index += 1
                cur_index = read_index
                if count != 1:
                    for digit in str(count):
                        A[write_index] = digit
                        write_index += 1
                count = 1
            read_index += 1

        return write_index