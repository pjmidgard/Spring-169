from time import time
import os
import binascii
namez = input("c  for compress or e for extract: ")
#@Author Jurijus Pacalovas
class compression:
    def cryptograpy_unpack(self):
                

        
            
    
                self.name = "@Author: Jurijus Pacalovas"
                print(self.name)
                if namez=="e":
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                           print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit                    
                    namea=""
                    namem=""
                    namema="?"
              
                    
                    
                    Times1=0
                    
                    
                    INFO4=""
                        
                   
                    
                    
                  
                   
                    Times1=0
                    Times3=0
                   
                    
              

                    Times=0
                    
                    
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    
                    Save_name=len(nameas)

              
                    
                    countraz=0
                    Times=0
                
                    
                    s=""
                    
                    
                    
                   
                 
                    INFO3=""
                    INFO2=""

           
                    
                    

              
                    

              
                    countraz=0
             
                   
                    s=""
                                        
                    
                   
                    
                    
                       
                    INFO3=""

         
                        
                    

                 

                    x=0
                    x1=0
                    x2=0
                    x = time()

            
                    
                    with open(nameas, "w") as f4:
                            f4.write(s)
                   
                    with open(name, "rb") as binary_file:

           
                  
                        # Read the whole file at once
                        
                        data = binary_file.read()
                        
                    
                        
                        s=str(data)
                        
            
                  
                        long_file1=len(data)
                        long_file5=len(data)
                        
            
                  
                       
                        if long_file1==0:
                            
                            raise SystemExit

                        Times_Finish=0
                        Times_Plus=0
                        
            
                   
                        while Times_Finish<10:
                       
                            
                            

                
           
                    
                   
                            
                
                    
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary
                                    long_file=len(INFO)
                                    long_file1=len(data)
                                
                                    xc=(long_file1*8)-long_file
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            INFO="0"+INFO
                                            z=z+1

      
                                    
                                    
                                    INFO=INFO+INFO2

                                    if countraz==1:
                                        INFO2=INFO
                            
                                    n = int(INFO2, 2)
                                
                                    binary_to_data=len(INFO2)
                                    binary_to_data=(binary_to_data/8)*2
                                    binary_to_data=str(binary_to_data)
                                    binary_to_data="%0"+binary_to_data+"x"
                             
                                    jl=binascii.unhexlify(binary_to_data % n)
                                    size_of_file_count=len(jl)
                                    
                                    data=jl
                                    Times_Plus=Times_Plus+1
                                    
                                
                                    
                                    if countraz==1:

                                        
                                        
                                        

                                        long_file5=len(data)

                                    INFO=bin(int(binascii.hexlify(data),16))[2:]
                                    long_file=len(INFO)

                                    long_file1=len(data)
                                
                                    xc=(long_file1*8)-long_file
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            INFO="0"+INFO
                                            z=z+1


                                    
                                    INFO2=INFO

                                    long_file3=len(INFO2)
                                long_file2=len(INFO2)
                                
                                
                                
                                Long_file=int(INFO2[24:56],2)
                               # print(Long_file)

                                
                                    
                    
                                
                                

                                
                                #print(Long_file)
                                Times_compress=int(INFO2[56:136],2)
                                #print(Times_compress)
                                
                                Divide_Number=int(INFO2[0:24],2)
                              
                                #print(Divide_Number)
                                C1="0"+str(Long_file*8)+"b"
                                N_Start=0
                                Start_file=""
                                Finish_file=""
                                Finish_file1=""
                                Finish_file2=""
                                
                                Start_file=format(N_Start,C1)
                                Finish_file1=INFO2
                                #print(Start_file)
                              
                                    	#print(Start_file)
                                
                                while Finish_file1!=Finish_file2:
                                    if Times3==0:
                                        Start_file=format(N_Start,C1)
                                        INFO2=Start_file
                                        N11=Divide_Number
                                    
                                    	  
                                        N=int(INFO2,2)
                                        N2=0
                                        N3=0
                                        N1=0
                                        N4=0
                                       
                                        N6=0
                                        N7=0
                                        N8=0
                                        N9=0
                                        
                                    N2=N%2
                                    N3=N%3
                                    
                                    if N2==0 and N3==0:
                                            N//=2
                                    else:
                                            N-=1
                                            
                                    print(N)
                                            
                                        
                                        
                                   
                                      

                                    


                                    
                                    Times3+=1  
                                    Times2=0
                                    #print(Times3)
                                    if N>-1 and N<=(2**256) or Times3==(2**80)-1:
                                        #print(Bias2)
                                       
                                        INFO3=bin(N)[2:]
                                        INFO3="1"+INFO3
                                 
                                        Times2=1
                                       

                                       
                                    
                                    if Times2==1:
                                      
                                       B5=format(Times3,'080b')
                                       B1=format(Long_file,'032b')
                                       
                                       long_file=len(INFO3)
                                       add_bits118=""
                                       count_bits=8-long_file%8
                                       z=0
                                       if count_bits!=8:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                       INFO3=add_bits118+INFO3
                                       B4=format(N11,'024b')
                                       INFO3=B4+B1+B5+INFO3
                                       Finish_file2=INFO3
                                       Times3=0
                                       #print(Times3)
                                       if Finish_file1==Finish_file2:
                                           INFO3=Start_file
                                           Times=1
                                       else:
                                           N_Start=N_Start+Divide_Number
                                           #print(N_Start)
											                                                                                            
											                                                                                            
											                                                                                            
                                    
                                    
                                    #print(Times)
                                if Times==1:
                                        

                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(INFO2)
                                        #os.system("pause")
                                        
                                        
                                            
               
                                        n = int(INFO3, 2)
                                        binary_to_data=len(INFO3)
                                        binary_to_data=(binary_to_data/8)*2
                                        binary_to_data=str(binary_to_data)
                                        binary_to_data="%0"+binary_to_data+"x"
                                        jl=binascii.unhexlify(binary_to_data % n)
                                        #
                                        #
                                        #print(len(jl))
                                            
                                      
                                        Times1=1
                                     
                                            
                                            
                                            #print(Times1)
                                            
                                        if Times1==1:
                                        
                                                Times_Finish=10
                                                if Times_Finish==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)                                                             

                           
    
            
    def cryptograpy_compression(self):                       
                    if namez=="c":
                        name = input("What is name of file? ")
                        if os.path.exists(name):
                           print('Path is exists!')
                        else:
                            print('Path is not exists!')
                            raise SystemExit
                        namea=""
                        namem=""
                        namema="?"
                        
                      
                       
                        
                      
                   
                       
                        Times1=0
                        Times3=0
                   
                        
              

                        Times=0
                        
                        
                        nameas=name
                        
                        Save_name=len(nameas)

                        long=len(name)
                   
                        name_cut=len(".bin")
                    
                        nameas=name+".bin" 
                        countraz=0
               
                       
                        s=""
                        INFO_5=""
                        
                        
                        
                       
                        
                        
                       
                        INFO3=""
                        INFO_5=""
     
                        
                        

                      

                        x=0
                        x1=0
                        x2=0
                        x = time()
                       
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            
                            data = binary_file.read()

                        
                            s=str(data)
                            long_file1=len(data)
                            #print(long_file1)
                            
                            

                          
                            long_file5=len(data)
                            
                            if long_file1>(2**32)-1:
                                print("This file is too big");
                                raise SystemExit
                            if long_file1==0:
                            	raise SystemExit
                            
                            Times_Finish=0
                            
                            Times_Plus=0
                            while Times_Finish<10:
                          
                                
                                
                                
                                
                                
                                countraz=countraz+1

                                with open(nameas, "ab") as f2:
                                    if countraz==1:
                                        INFO=bin(int(binascii.hexlify(data),16))[2:]
                                        long_file=len(INFO)
                                        
                                        long_file1=len(data) 
                                        xc=(long_file1*8)-long_file
                                        z=0
                                        if xc!=0:
                                            while z<xc:
                                                INFO="0"+INFO
                                                z=z+1
                                        INFO2=INFO
                                        
                                        
                                        N=int(INFO2,2)
                                        #print(N)
                                        N2=0
                                        N3=0
                                        N1=0
                                        N4=0
                                       
                                        N6=0
                                        N7=0
                                        N8=0
                                        N9=0
                                                                      
                                    N2=N%6
                                    N3=N%2
                                    N4=N%3
                                    if N2==0:
                                            N//=2
                                    elif N3!=2 and N4==3:
                                        N7=1
                                    else:
                                        if N7==0:
                                            N-=1
                                  
                                    print(N)
                                                                                    
                                   
                                      


                                    #print(N)
                                    Times3+=1  
                                    if N==0 or N7==1 or Times3==(2**80)-1:
                                        #print(Bias2)
                                        if N>-1:
                                        	INFO3=bin(N)[2:]
                                        	INFO3="1"+INFO3
                          

                                        Times=1
                                    #print(Times)
                                    if Times==1:
                                       B5=format(Times3,'080b')
                                       B1=format(long_file1,'032b')
                                       
                                       long_file=len(INFO3)
                                       add_bits118=""
                                       count_bits=8-long_file%8
                                       z=0
                                       if count_bits!=8:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                       INFO3=add_bits118+INFO3
                                    
                                       INFO3=B1+B5+INFO3
                                     
                                     
                                      
                                       n = int(INFO3, 2)
                                       binary_to_data=len(INFO3)
                                       binary_to_data=(binary_to_data/8)*2
                                       binary_to_data=str(binary_to_data)
                                       binary_to_data="%0"+binary_to_data+"x"
                                       jl=binascii.unhexlify(binary_to_data % n)
                                       Times1=1 
                                       if Times1==1:
                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(INFO2)
                                        #os.system("pause")
                                        
                                        
                                            
               

                                        #
                                        #
                                        #print(len(jl))
                                            
                                      
                                        
                                     
                                            
                                            
                                            #print(Times1)
                                            
                                       
                                        
                                                Times_Finish=10
                                                if Times_Finish==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)        
                                                                                  														    
                                         



   



            
                     

d=compression()

xw1=d.cryptograpy_unpack()
print(xw1)

xw=d.cryptograpy_compression()
print(xw)