class Solution:
    def toh(self,N,fromm,to,aux):
        #base
        if N == 1:
            print(f"Move disk 1 from rod{fromm} to rod{to}")
            return
        # induction
        self.toh(N-1,fromm,aux,to)
        # moving single disk
        print(f"Move disk {N} from rod{fromm} to rod{to}")
        self.toh(N-1,aux,to,fromm)
        return


sol = Solution()
sol.toh(N=3,fromm=1,to=3,aux=2)