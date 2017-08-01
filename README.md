# homework
homework
# Flag Print w/ loops

def flagMain(): #Main method, includes loops for even, and odd offset stars/stripes
    print "0"   #aslo used for printing the top/bottom of flag
    print "I", "-" * 56, " I"
    for i in range(0,18):
        if (i>9):
            print "=" * 59,"I"
            
        else: 
            
       
       
             if (i%2 == 0):
                starsOdd()
            
             else: starsandStripes()
        
    print "I", "-" *56, " I"    
    
    
    #method for even offset stars   
def starsandStripes():
    
     print " * " * 6, "=" * 40,"I"
        
    
    
    #method for printing odd offset stars/stripes
def starsOdd():
    
    print "  *" * 5,"  ", "=" * 40,"I"
    


 

  
flagMain()
