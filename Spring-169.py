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

                                    long_file3=len(INFO2)
                                long_file2=len(INFO2)
                                
                                
                                
                                Long_file=int(INFO2[56:136],2)
                                #print(Long_file)

                                
                                    
                                Byte_Divide=32
                                
                                

                                
                                #print(Long_file)
                                Times_compress=int(INFO2[24:56],2)
                                
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
                                
                                while Finish_file1!=Finish_file2:
                                    if Times3==0:
                                        Start_file=format(N_Start,C1)
                                        INFO2="1"+Start_file
                                        N11=Divide_Number
                                    
                                    	  
                                        N=int(INFO2,2)
                                        N2=0
                                        N3=0
                                        N1=0
                                        N4=0
                                        N5=0
                                        N6=0
                                        N7=0
                                        N8=0
                                        N9=0
                                        
                                        
                                   
                                      
                                    N=-N
                                    #print(N)
                                    N2=N
                                    if N>-1 and N!=0:                   
                                    	N=N//2
                                    	N1=N2%2
                                    if N==0:
                                    	N=0
                                    elif N<0 and N!=0:
                                    	N7=1
                                    elif N>-1 and N!=0:
	                                    if N1==0:
	                                    	N3=N%2
	                                    	N5=N
	                                    	N4=N//2
	                                    	N6=N4%2
	                                    	N8=N4//2
	                                
	                                    	N9=N8%2
	                                    	if N3==0:
	                                    		N=N
	                                    		if N9==1 and N6==0:
	                                    			N=N4-1#//2//!2
	                                    			
	                                    		else:
	                                    			N=N2-1#//2//2
	                                    		
	                                    	else:
	                                    		N=N2-1#//2
	                                    		N=-N
	                                    		N7=0
	                                    else:
	                                    	N=N2-1#//!2
                                    


                                    
                                    Times3+=1  
                                    #print(Times3)
                                    if N>-1 and N<=(2**256) or Times3==(2**80)-1:
                                        #print(Bias2)
                                        if N>-1:
                                        	INFO3=bin(N)[2:]
                                        	INFO3="10"+INFO3
                                        else:
                                        	N=-N
                                        	INFO3=bin(N)[2:]
                                        	if N7==1:
                                        		INFO3="110"+INFO3
                                        	else:
                                        		INFO3="111"+INFO3

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
                                        INFO2="1"+INFO
                                        long_file3=len(INFO2)
                                        if Times3==0:
                                        	N1=1
                                        	N5=0
                                        	N6=0
                                        	N11=2**24
                                        	long=len(INFO2)
                                        	N=int(INFO2,2)
                                        	while N6!=1:
                                        		N11-=1
                                        		#print(N11)
                                        		if N==0:
                                        			N11=1
                                        			N6=1
                                        		if N11==0:
                                        			N11-=1
                                        		N5=N//(N11)
                                        		N1=N%(N11)
                                        		if N1==0 and N5!=0:
                                        			N6=1
                                        #print(N11)
                                        
                                        N=int(INFO2,2)
                                        #print(N)
                                        N2=0
                                        N3=0
                                        N1=0
                                        N4=0
                                        N5=0
                                        N6=0
                                        N7=0
                                        N8=0
                                        N9=0
                                        
                                        
                                   
                                      
                                    N=-N
                                    #print(N)
                                    N2=N
                                    if N>-1 and N!=0:                   
                                    	N=N//2
                                    	N1=N2%2
                                    if N==0:
                                    	N=0
                                    elif N<0 and N!=0:
                                    	N7=1
                                    elif N>-1 and N!=0:
	                                    if N1==0:
	                                    	N3=N%2
	                                    	N5=N
	                                    	N4=N//2
	                                    	N6=N4%2
	                                    	N8=N4//2
	                                
	                                    	N9=N8%2
	                                    	if N3==0:
	                                    		N=N
	                                    		if N9==1 and N6==0:
	                                    			N=N4-1#//2//!2
	                                    			
	                                    		else:
	                                    			N=N2-1#//2//2
	                                    		
	                                    	else:
	                                    		N=N2-1#//2
	                                    		N=-N
	                                    		N7=0
	                                    else:
	                                    	N=N2-1#//!2

                                    #print(N)
                                    Times3+=1  
                                    if N>-1 and N<=(2**256) or Times3==(2**80)-1:
                                        #print(Bias2)
                                        if N>-1:
                                        	INFO3=bin(N)[2:]
                                        	INFO3="10"+INFO3
                                        else:
                                        	N=-N
                                        	INFO3=bin(N)[2:]
                                        	if N7==1:
                                        		INFO3="110"+INFO3
                                        	else:
                                        		INFO3="111"+INFO3

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
                                       B4=format(N11,'024b')
                                       INFO3=B4+B1+B5+INFO3
                                     
                                     
                                      
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
