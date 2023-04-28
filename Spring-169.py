from time import time
Times_change_info=0
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
                    Times_of_compression1=0
                    
                    
                    Times1=0
                    
                    
                    INFO4=""
                        
                   
                    
                    count3=0
                    count4=-1
                   
                    Times1=0
                    Times3=0
                    Times_of_compression=0
                    
              

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

                    Times_of_compression=0
                    
                    countraz=0
                    Times=0
                    Times_change_info=2
                    Times_change_info1=0
                    s=""
                    c=2
                    R=0
                    
                    
                    count4=-1
                 
                    INFO3=""
                    INFO2=""

                    ssTimes_change_info=0
                    
                    

                    block=2
                    

                    count_time_of_copression=0
                    countraz=0
                    Times_change_info=2
                    Times_change_info1=0
                    s=""
                                        
                    
                    c=2
                    
                    
                       
                    INFO3=""

                    ssTimes_change_info=0
                        
                    

                    block=0

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
                       
                            
                            

                
           
                    
                            Times_change_info=Times_change_info+1
                            
                
                    
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
                                    INFO__2=INFO2

                                    long_file3=len(INFO2)
                                long_file2=len(INFO2)
                                
                                
                                
                                Long_file=int(INFO2[0:32],2)
                                
                                Times_F=0
                                #print(Long_file)

                                
                                while Times_F!=1:
                                    if Times3==0:
                                            Start_file=INFO2[32:]
                                            size_data3=INFO2[32:]
                                            
                                            if size_data3[0:1]=="0":
                                            	R=1

                                            else:
                                           	 R=0
                                            Start_file=Start_file[1:]
                                            size_data3=size_data3[1:]   
                                            
                                            while size_data3[0:1]!="1":
                                                if size_data3[0:1]=="0":
                                                    Start_file=Start_file[1:]
                                                    size_data3=size_data3[1:]
                                                    
                                                    
                                             
                                            Start_file=Start_file[1:]
                                         
                                            	
                                        #print(INFO2)
                                    	  
                                    

                                    block3=0
                                    INFO3=""
                                    INFO5=""
                                    INFO8=""
                                    
                                    #INFO4=""
                                    
                                    count3+=1
                                    #print(count4)
                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                    #print(len(INFO2))
                                    F=0
                                    B=0
                                    count4=-1
                                 
                                    long_file2=len(INFO2)
                                    #print(INFO2)
                                    
                                 
                                    
                                    long_file3=len(INFO2)
                                        
                                    INFO2=INFO2
                                        #print(INFO2)
                                        
                                     
                                    Multiply_N=int(INFO2[:long_file3-(Long_file-1)],2)
                                    MOD=int(INFO2[long_file3-(Long_file-1):],2)
                                    Multiply_N=((2**Long_file)*Multiply_N)+MOD

                                    INFO_Save=bin(Multiply_N)[2:]
                                    INFO3=INFO_Save
                                        
                                    

                                    
                                    INFO2=INFO3
                                    #print(len(INFO3))
                                    #n = int(INFO2, 2)
                                                                                                    
                                            
                                    #n = int(INFO2, 2)                                                                                     
                                            
                                    #binary_to_data=len(INFO2)
                                    #binary_to_data=(binary_to_data/8)*2
                                    #binary_to_data=str(binary_to_data)
                                    #binary_to_data="%0"+binary_to_data+"x"
                                    #jl=binascii.unhexlify(binary_to_data % n)
                                    #print(len(jl))
                                    #
                                    #
                                    #print(len(jl))
                                    
                                    Times3+=1  
                                    #print(Times3)
                                    if Times3==(2**50000) or R==1:
                                       #print(INFO3)
                                       if R==0:
                                       	INFO3=INFO3
                                       if R==1:
                                       	INFO3=INFO__2
                                    
                                       
                                       
                                       Times3=0
                                       #print(Times3)
                                       Times=1
                                       Times_F=1
                                       	                                                                                            
											                                                                                            
											                                                                                            
                                    
                                    
                                    #print(Times)
                                if Times==1:
                                        

                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(INFO3)
                                        #os.system("pause")
                                        
                                        
                                            
               
                                        n = int(INFO3, 2)
                                        binary_to_data=len(INFO3)
                                        binary_to_data=Long_file*2
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
                        
                        R=0
                       
                        
                        count3=0
                        count4=-1
                       
                        Times1=0
                        Times3=0
                        Times_of_compression=0
                        
              

                        Times=0
                        
                        
                        nameas=name
                        
                        Save_name=len(nameas)

                        long=len(name)
                   
                        name_cut=len(".bin")
                    
                        nameas=name+".bin" 
                        countraz=0
                        Times_change_info=2
                        Times_change_info1=0
                        s=""
                        INFO_5=""
                        
                        
                        
                        c=2
                        
                        
                       
                        INFO3=""
                        INFO_5=""
                        ssTimes_change_info=0
                        
                        

                        block=0

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
                          
                                
                                
                                
                                Times_change_info=Times_change_info+1
                                
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
                                        long_file3=len(INFO2)
                                        INFO__2=INFO2
                                    long_file2=len(INFO2)  
                                    block3=0
                                    INFO3=""
                                    INFO5=""
                                    INFO8=""
                                    INFO4=""
                                    
                                    count3+=1
                                    #print(count4)
                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                    #print(len(INFO2))
                                    F=0
                                    B=0
                                    count4=-1
                                    
                                    long_file2=len(INFO2)
                                    #print(long_file2)
                                    N2=-1
                                    N1=1
                                    N5=0
                                    long2=1
                                    N8=int(INFO2,2)
                                    
                                
                                
                                    long_file14=2**long_file5
                                    while N1!=0:
                                        N2+=1
                                        long_file14
                                        long=len(INFO2)
                                        long2=long-N2
                                        if long2<=0:
                                            B=1
                                            N1=0
                                        if B==0:
                                            N=int(INFO2,2)
                                            if N==0:
                                                B=1
                                                N1=0
                                            if long_file14>0:

                                            	N5=N//long_file14
                                            	N_1=N%long_file14
                                            Bias=bin(N5)[2:]
                                            INFO4=Bias
                                            if Times3==0:
                                                
                                                N10=bin(N8)[2:]
                                            
                                                N10_long=len(N10)
                                                
                                                C3="0"+str(7)+"b"
                                                #print(N10_long)
                                                
                                           
                                            INFO_5=INFO4
                                            
                                            if len(INFO_5)<N8 and B!=1 and N_1<2**long_file5:
                                                N1=0
                                                B=0
                                            
                                        
                                    	#print(N2)
                                    Bias=bin(N5)[2:]
                                    if N5==0:
                                    	B=1
                                    long61=len(Bias)
                                    long62=0
                                    if B==0:
                                    	long62=len(INFO2)
                                    NS=long61
                                    NS1=N8-long62
                                    NS2=NS1-1-long61
                                    Nj=len(bin(N2)[2:])
                                    #print(N2)
                                    if Times3==0:
                                        N9=bin(N8)[2:]
                                        N10_long=len(N9)
                                        C3="0"+str(long_file5-1)+"b"
                                    
                                   

                                    
                                    
                                    
                                    if B==0:
                                        MOD=format(N_1,C3)
                                      
                                        #print(len(MOD))
                                        INFO4=Bias
                                    
                                        INFO3=INFO4
                                        INFO3=INFO3+MOD
                                    else:
                                        R=1
                                   

                                    INFO2=INFO3
                                    #print(int(INFO3,2))
                                       
                                    
                                    #n = int(INFO2, 2)
                                                                                                    
                                            
                                    #n = int(INFO2, 2)                                                                                     
                                            
                                    #binary_to_data=len(INFO2)
                                    #binary_to_data=(binary_to_data/8)*2
                                    #binary_to_data=str(binary_to_data)
                                    #binary_to_data="%0"+binary_to_data+"x"
                                    #jl=binascii.unhexlify(binary_to_data % n)
                                    #print(len(jl))
                                    #
                                    #
                                    #print(len(jl))
                                    
                                    Times3+=1  
                                    if Times3==(2**50000) or R==1:
                                        #print(Bias2)

                                        if R==1:
                                        	INFO3="10"+INFO__2
                                        else:
                                        	INFO3="11"+INFO3
                                        long_file=len(INFO3)
                                        add_bits118=""
                                        count_bits=8-long_file%8
                                        z=0
                                        if count_bits!=8:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                        INFO3=add_bits118+INFO3
                                        Times=1
                                        B1=format(long_file1,'032b')
                                        
                                    
                                        INFO3=B1+INFO3
                                        
                                       
                                        
                                    
                                    
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
                                                                                  														    
                                         



   



            
                     

d=compression()

xw1=d.cryptograpy_unpack()
print(xw1)

xw=d.cryptograpy_compression()
print(xw)
